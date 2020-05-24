use std::io::{self, BufRead};

struct Foo {
    n: u128,
    target_term: u128,
}

fn find_term_by_real_len(a_len: u128, b_len: u128, target_len: u128, target_term: u128) -> Foo {
    let mut curr_term = 1;
    let mut patt_len = 1;
    let mut prev2_patt_len;
    let mut prev1_patt_len = 1;
    let mut left_block_len: u128;
    let mut right_block_len: u128 = a_len;
    let mut full_block_len: u128 = b_len;
    loop {
        if curr_term == 1 {
            if target_term == 0 || curr_term == target_term {
                if target_len <= a_len {
                    return Foo {
                        n: target_len,
                        target_term: curr_term,
                    };
                }
            }
            curr_term += 1;
            continue;
        } else if curr_term == 2 {
            if target_term == 0 || curr_term == target_term {
                if target_len <= b_len {
                    return Foo {
                        n: target_len,
                        target_term: curr_term,
                    };
                }
            }
            // set block size
            right_block_len = a_len;
            full_block_len = b_len;

            // set pattern len
            prev1_patt_len = 1;
            patt_len = 1;
            curr_term += 1;
            continue;
        }
        // set L/R block size
        left_block_len = right_block_len;
        right_block_len = full_block_len;
        
        // pattern len calc
        prev2_patt_len = prev1_patt_len;
        prev1_patt_len = patt_len;
        patt_len = prev2_patt_len + prev1_patt_len;

        // get current full block size
        full_block_len = 0;
        full_block_len += prev2_patt_len * a_len;
        full_block_len += prev1_patt_len * b_len;
        
        // println!("Target len: {} Real len: {}, RBS: {}, LBS: {}, Curr Term: {}", target_len, full_block_len, right_block_len, left_block_len, curr_term);
        // println!("patt_len: {}, prev1_patt_len: {}, prev2_patt_len: {}", patt_len, prev1_patt_len, prev2_patt_len);
        // println!("============================================================");
        if target_term == 0 || curr_term == target_term {
            if target_len <= left_block_len {
                return Foo {
                    n: target_len,
                    target_term: curr_term - 2,
                };
            } else if target_len <= full_block_len {
                return Foo {
                    n: target_len - left_block_len,
                    target_term: curr_term - 1,
                };
            }
        } else if curr_term > target_term {
            eprintln!("RIP");
            std::process::exit(1);
        }
        curr_term += 1;
    }
}

pub fn solve(a: &str, b: &str, n: u128) -> u128 {
    let a_len = a.len() as u128;
    let b_len = b.len() as u128;
    if n <= a_len {
        let ans = a.chars().nth((n-1) as usize).unwrap();
        println!("{}", ans);
        return ans.to_digit(10).unwrap() as u128;
    } else if n <= b_len {
        let ans = b.chars().nth((n-1) as usize).unwrap();
        println!("{}", ans);
        return ans.to_digit(10).unwrap() as u128;
    }

    let mut tmp_info = Foo {
        n,
        target_term: 0,
    };
    // println!("Target Term: {}, n: {}, pattern len: {}, stop: {}", tmp_info.target_term, tmp_info.n, tmp_info.target_pattern_len, tmp_info.stop);
    loop {
        // tmp_info = find_term_by_pattern_len(a_len, b_len, tmp_info.target_pattern_len, tmp_info.n);
        tmp_info = find_term_by_real_len(a_len, b_len, tmp_info.n, tmp_info.target_term);
        // println!("Target Term: {}, n: {}", tmp_info.target_term, tmp_info.n);
        if tmp_info.target_term <= 2 {
            break;
        }
    }

    let ans = match tmp_info.target_term {
        1 => {
            a.chars().nth((tmp_info.n-1) as usize).unwrap()
        },
        _ => {
            b.chars().nth((tmp_info.n-1) as usize).unwrap()
        }
    };

    println!("{}", ans);
    ans.to_digit(10).unwrap() as u128
}

fn parse_line(line: String) {
    let mut triplets = line.split_whitespace();
    let a = triplets.next().unwrap();
    let b = triplets.next().unwrap();
    let n = triplets.next().unwrap().parse::<u128>().unwrap();
    solve(a, b, n);
    // assert_eq!(solve(a, b, n), 1u64);
}

fn main() {
    let stdin = io::stdin();
    let mut iterator = stdin.lock().lines();
    let line1 = iterator.next().unwrap().unwrap();
    let num_entries = line1.parse::<u128>().unwrap();
    for _i in 0..num_entries {
        let line = iterator.next().unwrap().unwrap();
        parse_line(line);
    }
    // let a = "1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679";
    // let b = "8214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196";
    // let mut total: u128 = 0;
    // for n in 0..18 {
    //     let ans = 10u128.pow(n) * solve(a, b, (127 + (19 * n as u128)) * 7u128.pow(n));
    //     total += ans;
    //     println!("Ans: {}", ans);
    // }
    // println!("Total: {}", total);
}
