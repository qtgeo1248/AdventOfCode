open Stdio

let file_name =
  Printf.sprintf
    "tests/%s.txt"
    (if Array.length Sys.argv = 1 then "input" else Array.get Sys.argv 1)

module IntPair = struct
  type t = int * int

  let compare (x1, y1) (x2, y2) =
    match Int.compare x1 x2 with
    | 0 -> Int.compare y1 y2
    | res -> res
end

module IntPairSet = Set.Make (IntPair)
module IntSet = Set.Make (Int)

let ( ++ ) f g x = f (g x)

let get_pages (file_name : string) : IntPairSet.t * int Array.t list =
  let parse_rule (rule_raw : string) : int * int =
    match String.split_on_char '|' rule_raw with
    | l :: r :: _ -> (int_of_string l, int_of_string r)
    | _ -> raise (Invalid_argument "Text file formatted incorrectly")
  in
  let process_rules (rules_raw : string) : IntPairSet.t =
    let rules_processed = String.split_on_char '\n' rules_raw |> List.map parse_rule in
      List.fold_right IntPairSet.add rules_processed IntPairSet.empty
  in
  let process_pages (pages_raw : string) : int Array.t list =
    String.split_on_char '\n' pages_raw
    |> List.map (Array.of_list ++ List.map int_of_string ++ String.split_on_char ',')
  in
  let lines = In_channel.read_all file_name |> String.trim in
    match Str.split (Str.regexp "\n\n") lines with
    | rules_raw :: pages_raw :: _ -> (process_rules rules_raw, process_pages pages_raw)
    | _ -> raise (Invalid_argument "Text file formatted incorrectly")

let range i j = Array.init (j - i) (( + ) i)
let range_from_zero n = range 0 n

let add_to_list_table table key value =
  match Hashtbl.find_opt table key with
  | None -> Hashtbl.add table key (IntSet.singleton value)
  | Some values -> Hashtbl.replace table key (IntSet.add value values)

let get_violations (rules : IntPairSet.t) (page : int Array.t) =
  let violations = Hashtbl.create 100 in
  let add_violation i j =
    if IntPairSet.mem (page.(j), page.(i)) rules
    then add_to_list_table violations page.(j) page.(i)
    else ()
  in
  let outer_loop i = Array.iter (add_violation i) (range (i + 1) (Array.length page)) in
    Array.iter outer_loop (range_from_zero (Array.length page - 1));
    violations

let fix_page (violations : (int, IntSet.t) Hashtbl.t) (page : int Array.t) =
  let rec swap_back i =
    match Hashtbl.find_opt violations page.(i) with
    | None -> ()
    | Some cur_vios ->
      if IntSet.cardinal cur_vios = 0
      then ()
      else (
        let cur = page.(i) in
        let prev = page.(i - 1) in
          Array.set page (i - 1) cur;
          Array.set page i prev;
          Hashtbl.replace violations cur (IntSet.remove prev cur_vios);
          swap_back (i - 1))
  in
    Array.iter swap_back (range_from_zero (Array.length page))

let filter_and_fix (rules : IntPairSet.t) (page : int Array.t) =
  let violations = get_violations rules page in
    if Hashtbl.length violations > 0
    then (
      fix_page violations page;
      true)
    else false

let get_middle_page (page : int Array.t) = page.(Int.div (Array.length page) 2)

let get_middle_pages (rules, pages) : int =
  List.filter (filter_and_fix rules) pages
  |> List.map get_middle_page
  |> List.fold_left ( + ) 0

let _ = get_pages file_name |> get_middle_pages |> string_of_int |> print_endline
