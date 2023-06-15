// Crear un array de 1000 palabras aleatorias separadas por espacios
let palabras = [];
for (let i = 0; i < 1000; i++) {
  let palabra = "";
  let longitud = Math.floor(Math.random() * 10) + 1; // generar aleatoriamente la longitud de la palabra entre 1 y 10
  for (let j = 0; j < longitud; j++) {
    let codigoCaracter = Math.floor(Math.random() * 26) + 97; // generar aleatoriamente el código ASCII para letras minúsculas
    let caracter = String.fromCharCode(codigoCaracter);
    palabra += caracter;
  }
  palabras.push(palabra);
}

// Crear un objeto para almacenar los anagramas
let anagramas = {};

// Loop a través de cada palabra en el array y ordenar sus caracteres alfabéticamente para formar una nueva cadena
// Luego, agregar la palabra original al array correspondiente en el objeto "anagramas", usando la cadena ordenada como clave
for (let i = 0; i < palabras.length; i++) {
  let ordenado = palabras[i].split("").sort().join("");
  if (anagramas[ordenado] === undefined) {
    anagramas[ordenado] = [];
  }
  anagramas[ordenado].push(palabras[i]);
}

console.log("Anagramas")

// Recorrer el objeto "anagramas" y mostrar en consola los arrays que contengan más de una palabra
for (let clave in anagramas) {
  if (anagramas[clave].length > 1) {
    console.log(anagramas[clave]);
  }0
}
