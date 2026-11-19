const _x: i32 = -1;
fn main(){
	let result = soma_iter(100,0);
	println!("{}",result);
}

fn soma_iter(n: u64, acc: u64) -> u64 {
    if n == 0 { acc } else { soma_iter(n - 1, acc + n) }
}