open Stdio

let file_name =
  Printf.sprintf
    "tests/%s.txt"
    (if Array.length Sys.argv = 1 then "input" else Array.get Sys.argv 1)

let get_memory file_name = In_channel.read_all file_name

let get_answer memory =
  let mul_regex = Str.regexp "mul([0-9]+,[0-9]+)" in
  let rec process_mult memory idx =
    try
      let _ = Str.search_forward mul_regex memory idx in
      let mul_str = Str.matched_string memory in
      let open_paren = String.index mul_str '(' in
      let comma = String.index mul_str ',' in
      let close_paren = String.index mul_str ')' in
      let num1 =
        int_of_string (String.sub mul_str (open_paren + 1) (comma - open_paren - 1))
      in
      let num2 =
        int_of_string (String.sub mul_str (comma + 1) (close_paren - comma - 1))
      in
        (num1 * num2) + process_mult memory (Str.match_end ())
    with
    | Not_found -> 0
  in
    process_mult memory 0

let _ = get_memory file_name |> get_answer |> string_of_int |> print_endline
