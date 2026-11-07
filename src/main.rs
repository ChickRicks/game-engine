fn main(){
    let mut x = "Str".to_string();
    let y = &mut x;
    y.push('1');
    y.push_str("aaaa");
    println!("{}",y);
    x = "Str".to_string();
    let z = &x;
    let w = &x;
    let v = &x;
    println!("{} {}",z,v);
}