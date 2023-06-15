function confnombre(data){

    x=document.getElementById("nombre").value;
    document.getElementById("confnombre").innerHTML =
    "El nombre: "+ x+" se a guardado ";
}
 /*
function calcularAreaCirculo(radio) {
    return Math.PI * Math.pow(radio, 2);
  }

  calcularAreaCirculo(1);
*/

function areaCirculo() {
  
    /* Área de un círculo */
    this.areaCirculo = function (radio) {
      return Math.PI * Math.pow(radio,2);
    }
  
  }

function raizcuadrada() {
    return Math.SQRT2;
  }
  
  getRoot2();