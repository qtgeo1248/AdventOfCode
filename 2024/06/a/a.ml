open Stdio

let file_name =
  Printf.sprintf
    "tests/%s.txt"
    (if Array.length Sys.argv = 1 then "input" else Array.get Sys.argv 1)

let dirs = Array.of_list [ (-1, 0); (0, 1); (1, 0); (0, -1) ]
let range i j = Array.init (j - i) (( + ) i)
let range_from_zero n = range 0 n

let get_map (file_name : string)
  : (int * int) * (int * int * int) * (int * int, unit) Hashtbl.t
  =
  let rows = In_channel.read_lines file_name |> Array.of_list in
  let h, w = (Array.length rows, String.length (Array.get rows 0)) in
  let blocks = Hashtbl.create 100 in
  let loop_string i guard j =
    match rows.(i).[j] with
    | '^' -> (i, j, 0)
    | '>' -> (i, j, 1)
    | 'v' -> (i, j, 2)
    | '<' -> (i, j, 3)
    | '#' ->
      Hashtbl.replace blocks (i, j) ();
      guard
    | _ -> guard
  in
  let loop_rows guard i = Array.fold_left (loop_string i) guard (range_from_zero w) in
  let guard = Array.fold_left loop_rows (-1, -1, -1) (range_from_zero h) in
    ((h, w), guard, blocks)

let run_sim ((h, w), guard, blocks) =
  let seen = Hashtbl.create 100 in
  let rec walk (i, j, dir) =
    let dy, dx =
      Hashtbl.replace seen (i, j) ();
      Array.get dirs dir
    in
    let i', j' = (i + dy, j + dx) in
      if i' < 0 || i' >= h || j' < 0 || j' >= w
      then ()
      else if Hashtbl.mem blocks (i', j')
      then walk (i, j, (dir + 1) mod 4)
      else walk (i', j', dir)
  in
    walk guard;
    Hashtbl.length seen

let _ = file_name |> get_map |> run_sim |> string_of_int |> print_endline
