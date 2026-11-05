const test: u32 = 10;

fn main() {
    let x = 'A';
    let y = false;
    let b = true;
    let z = if x == 'A' {"zs"} else {"zs"};
    let o = "teste1";
    let _p = "teste2";
    let f = 5;
    let g = 3;
    let p: &str = "ab";
    let
	a
	=
	10;
	let
	c:
	i32
	=
	90;

    println!("Hello, world {}!",x);
    println!("Hello, world! 2: Electric boogaloo {}",y);
    if x == 'a' {println!("Hello, world! 3: The problem is another {}",z)};
    println!("f/g = {}",f/g);
    if false{println!("verdadeiro");} else{(println!("falso"));}
    println!("{}",teste());
    println!("{}", format!("{} {}",o,f));
    let ih = &z;
    let ij = &ih;
    let mut zo = z.to_string();
    zo.push('b');
    println!("{} {} {}",zo,ih,ij);
    println!("{}",f + g);
    y == b;
    g & f;
}
fn teste() -> i32{
    32
}