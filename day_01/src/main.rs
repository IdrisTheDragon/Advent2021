use std::fs;

fn main() {
  part_1();
  part_2();
}

fn part_1(){
    let contents = fs::read_to_string("example.txt")
         .expect("error");
    let mut count = 0;
    let mut prev = -1;
    let split = contents.split("\n");
    for item in split {
        let x: i32 = item.parse().unwrap();
        if prev == -1 {
        } else if x > prev {
            count = count+1;
        }
        prev = x;
    }
    println!("Part 1:{}",count)
}

fn part_2(){
    let contents = fs::read_to_string("input.txt")
         .expect("error");
    let mut count = 0;
    let mut prev = -1;
    let split = contents.split("\n");
    let mut a = [0,0,0];
    let mut i = 2;
    for item in split {
        let x: i32 = item.parse().unwrap();
        i = i+1;
        if i == 3 {
            i = 0;
        }
        a[i] = x;
        let sum = a[0] + a[1] + a[2];
        if a[2] == 0 {
          continue
        }
        if prev == -1 {
        }else if sum > prev {
            count = count+1;
        }
        prev = sum;
    }
    println!("Part 2:{}",count)
}

