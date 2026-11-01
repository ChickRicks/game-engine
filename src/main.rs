fn main() {
    let x = 'a';
    let y = false;
    let z = if x == 'a' {'b'} else {'d'};
    println!("Hello, world {}!",x);
    println!("Hello, world! 2: Electric boogaloo {}",y);
    if x == 'a' {println!("Hello, world! 3: The problem is another {}",z)};
}
