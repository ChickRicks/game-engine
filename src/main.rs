fn main() {
    let x = 'a';
    let y = false;
    let z = if x == 'a' {'b'} else {'d'};
    let f = 5;
    let g = 3;
    println!("Hello, world {}!",x);
    println!("Hello, world! 2: Electric boogaloo {}",y);
    if x == 'a' {println!("Hello, world! 3: The problem is another {}",z)};
    println!("f/g = {}",f/g);
    if (f){println!("verdadeiro");} else{(println!("falso"));}
}
