use std::collections::HashMap;
fn main(){
	let mut x = HashMap::new();
	x.insert(1,"Um");
	x.insert(2,"Dois");
	x.insert(3,"Três");
	for val in x{
		println!("{:?}",val);
	}
	// println!("{:?}",x);  // - Inválido, x foi transferido para o for 
	}