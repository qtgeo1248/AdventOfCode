open Stdio

let file_name =
  Printf.sprintf
    "tests/%s.txt"
    (if Array.length Sys.argv = 1 then "input" else Array.get Sys.argv 1)

let offsets = [ List.to_seq [ (1, 1); (-1, -1) ]; List.to_seq [ (1, -1); (-1, 1) ] ]

(* Composition *)
let ( ++ ) f g x = f (g x)
let pair_add (y1, x1) (y2, x2) = (y1 + y2, x1 + x2)
let matrix_get matrix (row, col) = Array.get (Array.get matrix row) col
let array_sum = Array.fold_left ( + ) 0
let matrix_sum = array_sum ++ Array.map array_sum

let get_word_search file_name =
  file_name
  |> In_channel.read_lines
  |> List.map (Array.of_seq ++ String.to_seq)
  |> Array.of_list

let find_xmas (word_search : char Array.t Array.t) : int =
  let is_ms str = str = "MS" || str = "SM" in
  let is_xmas (row : int) (col : int) (offsets : (int * int) Seq.t list) : bool =
    try
      List.map (Seq.map (matrix_get word_search ++ pair_add (row, col))) offsets
      |> List.map String.of_seq
      |> List.for_all is_ms
    with
    | Invalid_argument _ -> false
  in
  let count_cell row col elem =
    if elem <> 'A' then 0 else is_xmas row col offsets |> Bool.to_int
  in
    word_search |> Array.mapi (Array.mapi ++ count_cell) |> matrix_sum

let _ = file_name |> get_word_search |> find_xmas |> string_of_int |> print_endline
