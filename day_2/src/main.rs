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
        let mut dir_l = item.split(" ");
        let dir = dir_l.next().unwrap();
        let x: i32 = dir_l.next().as_mut().unwrap().parse().unwrap();

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
      let dir_l = item.split(" ").collect::<Vec<&str>>();
      let dir:&str = dir_l[0];
      let x: i32 = dir_l[1].parse().unwrap();

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


