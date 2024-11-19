use::std::io::{self, BufRead};

fn input_nums() -> Vec<usize> {
    let stdin = io::stdin();
    let mut line = String::new();
    stdin.lock().read_line(&mut line).unwrap();
    line.trim()
        .split_whitespace()
        .map(|x| x.parse().unwrap())
        .collect()
}

fn main() {
    let tmp: Vec<usize> = input_nums();
    let n: usize  = tmp[0];
    let nums = input_nums();
    let mut one: usize = 0;
    let mut now: usize = 0;
    let mut ans: usize = 0;
    for i in 0..n {
        if nums[i] == 1 {
            one += 1;
            if now > 0 {
                now -= 1;
            }
        } else {
            now += 1;
        }
        ans = std::cmp::max(ans, now);
    }
    if one == nums.len() {
        println!("{}", one - 1);
    } else {
        println!("{}", ans + one);
    }
    
}

