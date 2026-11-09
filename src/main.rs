use std::collections::HashMap;
fn main(){
	let mut x = HashMap::new();
	x.insert(1,"Um");
	x.insert(2,"Dois");
	x.insert(3,"Três");
	for (chave,valor) in &x{
		println!("{} {}", chave, valor); // Printa chave valor\n para cada valor de x
	}
}