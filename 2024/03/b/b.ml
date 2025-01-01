open Stdio

let file_name =
  Printf.sprintf
    "tests/%s.txt"
    (if Array.length Sys.argv = 1 then "input" else Array.get Sys.argv 1)

let get_memory file_name = In_channel.read_all file_name

let get_answer memory =
  let mul_regex = Str.regexp "mul([0-9]+,[0-9]+)\|don't()" in
  let do_regex = Str.regexp "do()" in
  let rec process_mult memory to_do idx =
    try
      if to_do
      then (
        let _ = Str.search_forward mul_regex memory idx in
        let matched_str = Str.matched_string memory in
          match String.get matched_str 0 with
          | 'm' ->
            let open_paren = String.index matched_str '(' in
            let comma = String.index matched_str ',' in
            let close_paren = String.index matched_str ')' in
            let num1 =
              int_of_string
                (String.sub matched_str (open_paren + 1) (comma - open_paren - 1))
            in
            let num2 =
              int_of_string (String.sub matched_str (comma + 1) (close_paren - comma - 1))
            in
              (num1 * num2) + process_mult memory to_do (Str.match_end ())
          | 'd' -> process_mult memory false (Str.match_end ())
          | _ -> raise Not_found)
      else (
        let _ = Str.search_forward do_regex memory idx in
          process_mult memory true (Str.match_end ()))
    with
    | Not_found -> 0
  in
    process_mult memory true 0

let _ = get_memory file_name |> get_answer |> string_of_int |> print_endline
