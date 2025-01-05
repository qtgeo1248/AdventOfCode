open Stdio

let file_name =
  Printf.sprintf
    "tests/%s.txt"
    (if Array.length Sys.argv = 1 then "input" else Array.get Sys.argv 1)

let get_equations file_name =
  let parse_line line =
    let parts = Str.split (Str.regexp ": ") line in
    let total = int_of_string (List.nth parts 0) in
    let ops = List.map int_of_string (Str.split (Str.regexp " ") (List.nth parts 1)) in
      (total, ops)
  in
    In_channel.read_lines file_name |> List.map parse_line

let rec is_valid (total, ops) =
  match ops with
  | [] -> true
  | [ res ] -> res = total
  | x :: y :: res -> is_valid (total, (x + y) :: res) || is_valid (total, (x * y) :: res)

let get_calibration equations =
  List.filter is_valid equations
  |> List.fold_left (fun sum -> fun (total, _) -> sum + total) 0

let _ = file_name |> get_equations |> get_calibration |> string_of_int |> print_endline
