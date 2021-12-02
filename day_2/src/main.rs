use std::fs;

fn main() {
  part_1();
  part_2();
}

fn part_1(){
    let contents = fs::read_to_string("input.txt")
         .expect("error");
    let split = contents.split("\n");
    let mut depth =0;
    let mut horizontal = 0;
    for item in split {
        let mut dir_L = item.split(" ");
        let dir = dir_L.next().unwrap();
        let x: i32 = dir_L.next().as_mut().unwrap().parse().unwrap();

        if dir == "forward" {
          horizontal = horizontal + x;
        } else if dir== "up" {
          depth = depth -x;
        } else if dir== "down" {
          depth = depth + x;
        } else {
          println!("Parse error on: {}",dir);
        }
        
    }
    println!("Part 1:{}",depth*horizontal)
}

fn part_2(){
  let contents = fs::read_to_string("input.txt")
       .expect("error");
  let split = contents.split("\n");
  let mut depth =0;
  let mut horizontal = 0;
  let mut aim = 0;
  for item in split {
      let mut dir_L = item.split(" ");
      let dir = dir_L.next().unwrap();
      let x: i32 = dir_L.next().as_mut().unwrap().parse().unwrap();

      if dir == "forward" {
        horizontal = horizontal + x;
        depth = (depth) + (aim*x);
      } else if dir== "up" {
        aim = aim -x;
      } else if dir== "down" {
        aim = aim + x;
      } else {
        println!("Parse error on: {}",dir);
      }
      
  }
  println!("Part 1:{}",depth*horizontal)
}


