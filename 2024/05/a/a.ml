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

let get_middle_pages (rules, pages) : int =
  let is_correct (page : int Array.t) =
    let is_correct_pair i j = not (IntPairSet.mem (page.(j), page.(i)) rules) in
    let outer_idxes = Array.init (Array.length page - 1) Fun.id in
    let outer_loop i =
      let inner_idxes = Array.init (Array.length page - i - 1) (( + ) (i + 1)) in
        Array.for_all (is_correct_pair i) inner_idxes
    in
      Array.for_all outer_loop outer_idxes
  in
  let get_middle_page (page : int Array.t) = page.(Int.div (Array.length page) 2) in
    List.filter is_correct pages |> List.map get_middle_page |> List.fold_left ( + ) 0

let _ = get_pages file_name |> get_middle_pages |> string_of_int |> print_endline
