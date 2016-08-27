#!/usr/bin/rust run

fn tri(num: u64) -> u64 { 
	let smaller = num - 1;

	match smaller {
		0 => num,
		x => tri(x) + num
	}
}

fn test_trinum() {
	let res = tri(7);
	let out_str = format!("tri(7): {}", res);

	println!("{}", out_str)
}

fn fac<'a>(tgt: u64) -> Vec<u64> {
	let mut res = vec!();

	let x = tgt + 1;

	for i in 1..x {
		if (tgt % i == 0) | (i == 1) {
			res.push(i);
		}
	};

	res
}

fn test_fac() {
	let res = fac(6);
	let res_len = res.len();
	let out_str = format!("fac(6, 6): {:?}, len: {}", res, res_len);
	println!("{}", out_str);
}

fn main() {
	test_trinum();
	test_fac();
}

