let Caja = []
let CajaFitness = []

for(let i=0; i<100; i++){
    
    let Tablero = [,,,,,,,,]
    for(let i=0; i<8; i++){
        Tablero [i] = [0,0,0,0,0,0,0,0]
    }//tablero
    
    for(let i=0; i<8; i++){
        let x = Math.floor(Math.random() * 8);
        Tablero [i][x] = 1
    }//reinas aleatorias
    //8 alelos=1 cromosoma

    //console.log(Tablero)

    Caja.push(Tablero)
    //push sirve para guardar elementos, para esto se crea primero la caja
    
}

console.log("Caja que contiene los 100 Tableros")
console.log(Caja)



for(let i=0; i<100; i++){
    //contador para saber cuantas veces chocan las reinas
    //esto es para encontrar el fitness
    let choqueArriba=0
    let choqueAbajo=0
    
    let choqueIzquierdaArriba=0
    let choqueDerechaArriba=0
    
    let choqueIzquierdaAbajo=0
    let choqueDerechaAbajo=0
    
  
    for(let x=0; x<8; x++){
        for(let y=0; y<8; y++){
            if (Caja [i][x][y] == 1){
                let Xcopia = x
                let Ycopia = y
                //se usa Xcopia para no cambiar el original
    
    
                //VERTICAL
    
                //arriba
                while(Xcopia>=0)/*la condicion*/{
                    if (Caja [i][Xcopia][y] == 1 && Xcopia!=x){
                       // console.log("se encontro que la reina en la ubicacion ["+i+"]["+x+"]["+y+"] choca con otra reina arriba suyo")
                        choqueArriba+=1
                    }//evaluar la nueva posicion 
                    Xcopia -= 1 //la operacion se coloca al final
                }
    
                //abajo
                Xcopia =  x //se reinicio Xcopia
                while(Xcopia<8){
                    if (Caja [i][Xcopia][y] == 1 && Xcopia!=x){
                        //console.log("se encontro que la reina en la ubicacion ["+i+"]["+x+"]["+y+"] choca con otra reina abajo suyo")
                        choqueAbajo+=1   
                    }//evaluar la nueva posicion 
                    Xcopia += 1
                }
               
    
                Xcopia = x
    
                //DIAGONAL
                //IzquierdaArriba
                while(Xcopia>=0 && Ycopia>=0){
                    if (Caja [i][Xcopia][Ycopia] == 1 && Xcopia!=x && Ycopia!=y){
                        //console.log("se encontro que la reina en la ubicacion ["+i+"]["+x+"]["+y+"] choca con otra reina diagonal izquierda arriba suyo")
                        choqueIzquierdaArriba+=1
                    }
                    Xcopia -= 1
                    Ycopia -= 1
                }
    
                //DerechaArriba
                Xcopia = x
                Ycopia = y
                while(Xcopia>=0 && Ycopia<=7){
                    if (Caja [i][Xcopia][Ycopia] == 1 && Xcopia!=x && Ycopia!=y){
                        //console.log("se encontro que la reina en la ubicacion ["+i+"]["+x+"]["+y+"] choca con otra reina diagonal derecha arriba suyo")
                        choqueDerechaArriba+=1
                    }
                    Xcopia -= 1
                    Ycopia += 1
                }
    
                //IzquierdaAbajo
                Xcopia = x
                Ycopia = y
                while(Xcopia<=7 && Ycopia>=0){
                    if (Caja [i][Xcopia][Ycopia] == 1 && Xcopia!=x && Ycopia!=y){
                        //console.log("se encontro que la reina en la ubicacion ["+i+"]["+x+"]["+y+"] choca con otra reina diagonal izquierda abajo suyo")
                        choqueIzquierdaAbajo+=1
                    }
                    Xcopia += 1
                    Ycopia -= 1
                }
    
                //DerechaAbajo
                Xcopia = x
                Ycopia = y
                while(Xcopia<=7 && Ycopia<=7){
                    if (Caja [i][Xcopia][Ycopia] == 1 && Xcopia!=x && Ycopia!=y){
                        //console.log("se encontro que la reina en la ubicacion ["+i+"]["+x+"]["+y+"] choca con otra reina diagonal derecha abajo suyo")
                        choqueDerechaAbajo+=1
                    }
                    Xcopia += 1
                    Ycopia += 1
                }   
    
            }//llama al tablero y revisa si hay un 1
        }
    }//for recorre filas


    console.log(choqueAbajo+choqueArriba+choqueDerechaAbajo)
   // CajaFitness.push(choqueAbajo+choqueArriba+choqueDerechaAbajo+choqueDerechaArriba+choqueIzquierdaAbajo+choqueIzquierdaArriba)//Guarda en la caja la cantidad de choques y los suma (esto por cada tablero)
}

console.log("CajaFitness que contiene el total de choques (esto por cada tablero)")
console.log(CajaFitness)

//EVOLUCION

let Menor1=99
let Posicion_Tablero1
let Posicion_Tablero2

for(let i=0; i<100; i++){

if(CajaFitness[i]<Menor1){
    Menor1=CajaFitness[i]
    Posicion_Tablero1=i
}

}//for cajafitnes 1


Menor1=99//se reinicia el valor de menor
for(let i=0; i<100; i++){

    if(CajaFitness[i]<Menor1 && i!=Posicion_Tablero1){
        Menor1=CajaFitness[i]
        Posicion_Tablero2=i
    }
    
}//for cajafitnes 2

console.log("Posicion de los 2 tableros con menor Fitness")

console.log(Posicion_Tablero1)
console.log(Caja[Posicion_Tablero1])

console.log(Posicion_Tablero2)
console.log(Caja[Posicion_Tablero2])


let Tableros_seleccionados=[Caja[Posicion_Tablero1], Caja[Posicion_Tablero2]]//se creo un nuevo arreglo  y se guardaron los 2 tableros con menor fitnes
Caja=[]//se vacio la caja
let Guardar_Cromosoma=[[],[]]


for(let i=0; i<2; i++){
    for(let x=0; x<8; x++){
        for(let y=0; y<8; y++){
            if(Tableros_seleccionados[i][x][y] == 1){
                Guardar_Cromosoma[i].push(y)
            }
        }
    }
}


console.log("Se guarda el cromosoma de los 2 tableros")
console.log(Guardar_Cromosoma)


console.log("Se dividen los 2 cromosomas de los tableros a la mitad")

let Dividir_Cromosoma1 = Guardar_Cromosoma[0].slice(0, 4)
console.log(Dividir_Cromosoma1)

let Dividir_Cromosoma2 = Guardar_Cromosoma[1].slice(4, 8)
console.log(Dividir_Cromosoma2)






//console.log(choqueAbajo) muestra la cantidad de choques abajo



/*
            //HORIZONTAL

            //izquierda
            while(Ycopia>=0){
                if (Tablero [x][Ycopia] == 1 && Ycopia!=y){
                    console.log("se encontro que la reina en["+x+"]["+y+"] choca con otra reina izquierda suyo")
                    choqueIzquierda+=1
                }
                Ycopia -= 1
            }


            en este caso no es necesario horizontal por que solo se creo una reina por fila
*/


//= asignacion
//== comparacio