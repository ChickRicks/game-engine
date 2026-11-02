fn main() {
    let x = 'A';
    let y = false;
    let _b = true;
    let z = if x == 'A' {'Z'} else {'d'};
    let _o = "teste1";
    let _p = "teste2";
    let f = 5;
    let g = 3;

    println!("Hello, world {}!",x);
    println!("Hello, world! 2: Electric boogaloo {}",y);
    if x == 'a' {println!("Hello, world! 3: The problem is another {}",z)};
    println!("f/g = {}",f/g);
    if false{println!("verdadeiro");} else{(println!("falso"));}
    for i in x..=z{
        println!("{}",i);
    }
    println!("{}",teste())
}
fn teste() -> i32{
    32
}

