open Stdio

let file_name =
  Printf.sprintf
    "tests/%s.txt"
    (if Array.length Sys.argv = 1 then "input" else Array.get Sys.argv 1)

let slopes = [ (1, 1); (1, 0); (1, -1); (0, 1); (0, -1); (-1, 1); (-1, 0); (-1, -1) ]
let idxes = List.to_seq [ 0; 1; 2; 3 ]
let xmas = "XMAS"

(* Composition *)
let ( ++ ) f g x = f (g x)
let matrix_get matrix (row, col) = Array.get (Array.get matrix row) col
let array_sum = Array.fold_left ( + ) 0
let matrix_sum = array_sum ++ Array.map array_sum

let get_word_search file_name =
  file_name
  |> In_channel.read_lines
  |> List.map (Array.of_seq ++ String.to_seq)
  |> Array.of_list

let find_xmas (word_search : char Array.t Array.t) : int =
  let is_xmas row col (dy, dx) =
    try
      Seq.map (fun i -> (row + (i * dy), col + (i * dx))) idxes
      |> Seq.map (matrix_get word_search)
      |> String.of_seq
      |> ( = ) xmas
    with
    | Invalid_argument _ -> false
  in
  let count_cell row col elem =
    if elem <> 'X'
    then 0
    else List.map (Bool.to_int ++ is_xmas row col) slopes |> List.fold_left ( + ) 0
  in
    word_search |> Array.mapi (Array.mapi ++ count_cell) |> matrix_sum

let _ = file_name |> get_word_search |> find_xmas |> string_of_int |> print_endline
