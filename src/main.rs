fn main(){
	struct Teste2 {
		x: u32,
		y: u64,
		z: f64
	}
	let _w = Teste2{
		x: 5,
		y: 10,
		z: 6.9
	};
	let mut u = Teste2{
		x: 10,
		y: 7,
		z: 10.23
	};
	//w.x = 10; - Inválido: w não é uma variável mutável.
	u.y = 80; // Válido, u é mutável.
	println!("{} {} {}",u.x,u.y,u.z);
}