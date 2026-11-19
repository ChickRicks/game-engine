fn main(){
	struct teste2 {
		x: u32,
		y: u64,
		z: f64
	}
	let w = teste2{
		x: 5,
		y: 10,
		z: 6.9
	};
	let u = teste2{
		x: 10,
		y: 7,
		z: 10.23
	};
	//w.x = 10; - Inválido: w não é uma variável mutável.
	u.y = 80; // Válido, u é mutável.
}