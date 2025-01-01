open Stdio

let file_name =
  Printf.sprintf
    "tests/%s.txt"
    (if Array.length Sys.argv = 1 then "input" else Array.get Sys.argv 1)

let ( ++ ) f g x = f (g x)

let get_reports file_name : int list list =
  let parse_line (line : string) : int list =
    String.split_on_char ' ' line |> List.map int_of_string
  in
    file_name |> In_channel.read_lines |> List.map parse_line

let get_answer (reports : int list list) : int =
  let rec is_safe is_incr (report : int list) =
    match report with
    | x :: y :: rest ->
      (match (x < y, Int.abs (x - y), is_incr) with
       | false, _, Some true -> false
       | true, _, Some false -> false
       | head_incr, diff, _ ->
         1 <= diff && diff <= 3 && is_safe (Some head_incr) (y :: rest))
    | _ -> true
  in
    List.map (Bool.to_int ++ is_safe None) reports |> List.fold_left ( + ) 0

let _ = get_reports file_name |> get_answer |> string_of_int |> print_endline
