#!/usr/bin/rust run

extern mod extra;

use std::uint::*;

fn tri(num: uint) -> uint { 
	let smaller = num - 1;

	match smaller {
		0 => num,
		x => tri(x) + num
	}
}

fn test_trinum() {
	let res = tri(7);
	let out_str = fmt!("tri(7): %?", res);

	println(out_str)
}

fn fac(tgt: uint) -> ~[uint] {
	let mut res = ~[];

	for range(1u, tgt+1) |i| {
		if ((tgt % i == 0) | (i == 1)) { res.push(i); }
	}

	res
}

fn test_fac() {
	let res = fac(6);
	let res_len = res.len();
	let out_str = fmt!("fac(6, 6): %?, len: %?", res, res_len);
	println(out_str);
}

fn main() {
	test_trinum();
	test_fac();
}

