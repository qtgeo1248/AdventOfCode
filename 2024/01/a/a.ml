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

let get_answer (lists : int list * int list) : int =
  let sorted_ls, sorted_rs = pair_map (List.sort Int.compare) lists in
    List.map2 ( - ) sorted_ls sorted_rs |> List.map Int.abs |> List.fold_left ( + ) 0

let _ = get_lists file_name |> get_answer |> string_of_int |> print_endline
