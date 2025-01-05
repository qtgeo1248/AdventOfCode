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
  let turning_points : (int * int * int, unit) Hashtbl.t = Hashtbl.create 100 in
  let tried : (int * int, unit) Hashtbl.t = Hashtbl.create 100 in
  let succeeded : (int * int, unit) Hashtbl.t = Hashtbl.create 100 in
  let step (i, j, dir) =
    let dy, dx = Array.get dirs dir in
      (i + dy, j + dx)
  in
  let rec try_block guard block =
    if Hashtbl.mem tried block
    then ()
    else (
      Hashtbl.add blocks block ();
      walk (Hashtbl.copy turning_points) guard true (fun () ->
        Hashtbl.add succeeded block ());
      Hashtbl.remove blocks block;
      Hashtbl.add tried block ())
  and walk turning_points ((i, j, dir) as guard) is_trial cycle =
    let i', j' = step guard in
      if i' < 0 || i' >= h || j' < 0 || j' >= w
      then ()
      else if Hashtbl.mem turning_points guard
      then cycle ()
      else if Hashtbl.mem blocks (i', j')
      then (
        Hashtbl.replace turning_points guard ();
        walk turning_points (i, j, (dir + 1) mod 4) is_trial cycle)
      else (
        if not is_trial then try_block guard (i', j') else ();
        walk turning_points (i', j', dir) is_trial cycle)
  in
    walk turning_points guard false (fun () -> raise Stack_overflow);
    Hashtbl.length succeeded

let _ = file_name |> get_map |> run_sim |> string_of_int |> print_endline
