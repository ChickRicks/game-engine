fn main(){
	let x: i32 = -9;
	let y: u32 = 10;
	// println!("{}",x + y); - Inválido, x é i32 enquanto y é u32.
	println!("{}",x + y as i32); // Válido, y é tratado como i32 temporariamente. Printa 1.
}