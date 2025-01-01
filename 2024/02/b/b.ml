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
  let rec is_safe_with_removal
            (is_incr : bool option)
            (report : int list)
            (remove_idx : int)
    =
    match (report, remove_idx) with
    | _ :: rest, 0 -> is_safe_with_removal is_incr rest (-1)
    | x :: _ :: rest, 1 -> is_safe_with_removal is_incr (x :: rest) (-1)
    | x :: y :: rest, _ ->
      (match (x < y, 1 <= Int.abs (x - y) && Int.abs (x - y) <= 3, is_incr) with
       | _, false, _ -> false
       | false, _, Some true -> false
       | true, _, Some false -> false
       | head_incr, true, _ ->
         is_safe_with_removal (Some head_incr) (y :: rest) (remove_idx - 1))
    | _ -> true
  in
  let is_safe (report : int list) =
    let idxes = Array.init (List.length report + 1) (fun i -> i - 1) in
      Array.exists (is_safe_with_removal None report) idxes
  in
    List.map (Bool.to_int ++ is_safe) reports |> List.fold_left ( + ) 0

let _ = get_reports file_name |> get_answer |> string_of_int |> print_endline
