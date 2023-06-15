let Caja = []
let CajaFitness = []
let boleano = false

for(let i=0; i<10; i++){
    
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

console.log("Caja que contiene los 10 Tableros")
console.log(Caja)

while(boleano == false)/*Se usa para repetir todo hasta encontrar al menos 0 en el fitnes*/{
    for(let i=0; i<10; i++){

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
    
        CajaFitness.push(choqueAbajo+choqueArriba+choqueDerechaAbajo+choqueDerechaArriba+choqueIzquierdaAbajo+choqueIzquierdaArriba)//Guarda en la caja la cantidad de choques y los suma (esto por cada tablero)
    }
    
    console.log("CajaFitness que contiene el total de choques (esto por cada tablero)")
    console.log(CajaFitness)
    
    //EVOLUCION
    
    let Menor1=99
    let Posicion_Tablero1
    let Posicion_Tablero2
    
    for(let i=0; i<10; i++){
    
        if(CajaFitness[i]<Menor1){
            Menor1=CajaFitness[i]
            Posicion_Tablero1=i
        }
    
    }//for cajafitnes 1


    if(Menor1==0){
        console.log("Tablero de fitness cero")
        console.log(Caja[Posicion_Tablero1])
        boleano=true
        continue
    }

    
    Menor1=99//se reinicia el valor de menor
    for(let i=0; i<10; i++){
    
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
    CajaFitness=[]//se vacia la CajaFitness
    let Guardar_Cromosoma=[[],[]] 
    
    for(let i=0; i<2; i++){
        for(let x=0; x<8; x++){
            for(let y=0; y<8; y++){
                if(Tableros_seleccionados [i][x][y] == 1){
                    Guardar_Cromosoma[i].push(y)
                }
            }
        }
    }
      
    console.log("Se guarda el cromosoma de los 2 tableros")
    // console.log(Guardar_Cromosoma)
    
    
    // console.log("Se dividen los 2 cromosomas de los tableros a la mitad")

    let Dividir_Cromosoma1 = Guardar_Cromosoma[0].slice(0, 4)
    // console.log(Dividir_Cromosoma1)
    
    let Dividir_Cromosoma2 = Guardar_Cromosoma[1].slice(4)
    // console.log(Dividir_Cromosoma2)
    
    let Dividir_Cromosoma3 = Guardar_Cromosoma[0].slice(4)
    // console.log(Dividir_Cromosoma3)

    let Dividir_Cromosoma4 = Guardar_Cromosoma[1].slice(0, 4)
    // console.log(Dividir_Cromosoma4)
 
    
    let Unir_Mitades = Dividir_Cromosoma1.concat(Dividir_Cromosoma2)

    let Unir_Mitades2 = Dividir_Cromosoma3.concat(Dividir_Cromosoma4)
    
    // console.log("Se unen ambas mitades y se crea un nuevo cromosoma")
    // console.log(Unir_Mitades)

    // console.log("Se unen las otrasx mitades y se crea un nuevo cromosoma")
    // console.log(Unir_Mitades2)

    let Tablero = [,,,,,,,,]
    for(let i=0; i<8; i++){
        Tablero [i] = [0,0,0,0,0,0,0,0]
    }//tablero

    for(let i=0; i<8; i++){
        let x = Unir_Mitades[i];
        Tablero [i][x] = 1
    }//reinas 

    let Tablero2 = [,,,,,,,,]
    for(let i=0; i<8; i++){
        Tablero2 [i] = [0,0,0,0,0,0,0,0]
    }//tablero

    for(let i=0; i<8; i++){
        let x = Unir_Mitades2[i];
        Tablero2 [i][x] = 1
    }//reinas 

    // CajaCromosoma.push(Tablero)
    // CajaCromosoma.push(Tablero2)

    let CajaCromosoma=[Tablero, Tablero2]
    console.log("Caja Cromosoma")
    console.log(CajaCromosoma)

    for(let i=0; i<2; i++){

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
                if (CajaCromosoma [i][x][y] == 1){
                    let Xcopia = x
                    let Ycopia = y

                    //se usa Xcopia para no cambiar el original
        
        
                    //VERTICAL
        
                    //arriba
                    while(Xcopia>=0)/*la condicion*/{
                        if (CajaCromosoma [i][Xcopia][y] == 1 && Xcopia!=x){
                           // console.log("se encontro que la reina en la ubicacion ["+i+"]["+x+"]["+y+"] choca con otra reina arriba suyo")
                            choqueArriba+=1
                        }//evaluar la nueva posicion 
                        Xcopia -= 1 //la operacion se coloca al final
                    }
        
                    //abajo
                    Xcopia =  x //se reinicio Xcopia
                    while(Xcopia<8){
                        if (CajaCromosoma [i][Xcopia][y] == 1 && Xcopia!=x){
                            //console.log("se encontro que la reina en la ubicacion ["+i+"]["+x+"]["+y+"] choca con otra reina abajo suyo")
                            choqueAbajo+=1   
                        }//evaluar la nueva posicion 
                        Xcopia += 1
                    }
                          
                    Xcopia = x
        
                    //DIAGONAL
                    //IzquierdaArriba
                    while(Xcopia>=0 && Ycopia>=0){
                        if (CajaCromosoma [i][Xcopia][Ycopia] == 1 && Xcopia!=x && Ycopia!=y){
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
                        if (CajaCromosoma [i][Xcopia][Ycopia] == 1 && Xcopia!=x && Ycopia!=y){
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
                        if (CajaCromosoma [i][Xcopia][Ycopia] == 1 && Xcopia!=x && Ycopia!=y){
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
                        if (CajaCromosoma [i][Xcopia][Ycopia] == 1 && Xcopia!=x && Ycopia!=y){
                            //console.log("se encontro que la reina en la ubicacion ["+i+"]["+x+"]["+y+"] choca con otra reina diagonal derecha abajo suyo")
                            choqueDerechaAbajo+=1
                        }
                        Xcopia += 1
                        Ycopia += 1
                    }   
        
                }//llama al tablero y revisa si hay un 1
            }
        }//for recorre filas
    
        CajaFitness.push(choqueAbajo+choqueArriba+choqueDerechaAbajo+choqueDerechaArriba+choqueIzquierdaAbajo+choqueIzquierdaArriba)//Guarda en la caja la cantidad de choques y los suma (esto por cada tablero)
    }

    console.log("CajaFitness que contiene el total de choques de los tableros de Caja Cromosoma")
    console.log(CajaFitness)

    let Respuesta
    if(CajaFitness[0]<CajaFitness[1]){
        Respuesta=Unir_Mitades
    }

    else if(CajaFitness[1]<CajaFitness[0]){
        Respuesta=Unir_Mitades2
    }

    else{
        Respuesta=Unir_Mitades
    }

    
    CajaFitness=[]//se vacia la CajaFitness

    //MUTACION
    
    for(let i=0; i<10; i++){
    
        //se seleccionan 2 alelos al azar en el nuevo cromosoma que se creo
       // console.log("Se seleccionan 2 alelos al azar en el nuevo cromosoma que se creo")
        let Seleccionar_Alelo1 = Math.floor(Math.random() * 8);
        let Seleccionar_Alelo2 = Math.floor(Math.random() * 8);

        while(Seleccionar_Alelo2==Seleccionar_Alelo1){
            Seleccionar_Alelo2 = Math.floor(Math.random() * 8); 
        }
    
        //posicion del alelo
        // console.log(Seleccionar_Alelo1)
        // console.log(Seleccionar_Alelo2)
    
        //let Guardar_Alelo1 = Respuesta[Seleccionar_Alelo1]
        //let Guardar_Alelo2 = Respuesta[Seleccionar_Alelo2]
    
        //alelo en la poscion
        // console.log(Guardar_Alelo1)
        // console.log(Guardar_Alelo2)
    
        //Respuesta[Seleccionar_Alelo1] = Guardar_Alelo2
        //Respuesta[Seleccionar_Alelo2] = Guardar_Alelo1
    
        Respuesta[Seleccionar_Alelo1] = Seleccionar_Alelo2
        //se intercambiaron los alelos de posicion
        // console.log(Unir_Mitades[Seleccionar_Alelo1])
        // console.log(Unir_Mitades[Seleccionar_Alelo2])
    
        //Cromosoma con los alelos cambiados
        // console.log("Nuevo 10 cromosoma con los alelos cambiados")
        // console.log(Unir_Mitades)
    
        let Tablero = [,,,,,,,,]
        for(let i=0; i<8; i++){
            Tablero [i] = [0,0,0,0,0,0,0,0]
        }//tablero
    
        for(let i=0; i<8; i++){
            let x = Respuesta[i];
            Tablero [i][x] = 1
        }//reinas 
    
        Caja.push(Tablero)
    }
    
    console.log("Nuevos 10 tableros con los nuevos cromosomas")
    console.log(Caja)
}







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
//== comparacion