open Stdio

let file_name =
  Printf.sprintf
    "tests/%s.txt"
    (if Array.length Sys.argv = 1 then "input" else Array.get Sys.argv 1)

let pair_map f (a, b) = (f a, f b)

let get_lists file_name : int list * int list =
  let get_parts (line : string) : int * int =
    let parts = String.split_on_char ' ' line in
      (List.nth parts 0, List.nth (List.rev parts) 0) |> pair_map int_of_string
  in
  let accum_list_pair (ls, rs) (l, r) = (l :: ls, r :: rs) in
    file_name
    |> In_channel.read_lines
    |> List.map get_parts
    |> List.fold_left accum_list_pair ([], [])

let incr_table (table : (int, int * int) Hashtbl.t) (is_left : bool) (num : int) : unit =
  let count_l, count_r =
    match Hashtbl.find_opt table num with
    | None -> (0, 0)
    | Some (l, r) -> (l, r)
  in
  let incr_l = if is_left then 1 else 0 in
  let incr_r = if is_left then 0 else 1 in
    Hashtbl.replace table num (count_l + incr_l, count_r + incr_r)

let get_answer ((ls, rs) : int list * int list) : int =
  let counts = Hashtbl.create 100 in
  let add_result num (count_l, count_r) sum = sum + (num * count_l * count_r) in
    List.iter (incr_table counts true) ls;
    List.iter (incr_table counts false) rs;
    Hashtbl.fold add_result counts 0

let _ = print_endline (get_lists file_name |> get_answer |> string_of_int)
