use std::io::{self, BufRead};


fn input_nums() -> Vec<i64> {
    let stdin = io::stdin();
    let mut line = String::new();
    stdin.lock().read_line(&mut line).unwrap();
    line.trim()
        .split_whitespace()
        .map(|x| x.parse().unwrap())
        .collect()
}

// 快速幂函数
fn fpow(mut x: i64, mut y: i64, z: i64) -> i64 {
    let mut res = 1;
    while y > 0 {
        if y & 1 == 1 {
            res = res * x % z;
        }
        x = x * x % z;
        y >>= 1;
    }
    res
}

fn main() {
    let nums: Vec<i64> = input_nums();
    const MOD: i64 = 1_000_000_007;
    let n: i64 = nums[0];
    let m: i64 = nums[1];
    let k: i64 = nums[2];
    // 根据 k 的值判断输出
    let result = if k == 1 {
        fpow(m, n, MOD) // k = 1 的情况
    } else if k == n {
        fpow(m, (n + 1) / 2, MOD) // k = n 的情况
    } else if k > n {
        fpow(m, n, MOD) // k > n 的情况
    } else if k % 2 == 1 {
        fpow(m, 2, MOD) // k 为奇数的情况
    } else {
        m // k 为偶数的情况
    };

    // 输出结果
    println!("{}", result);
}





