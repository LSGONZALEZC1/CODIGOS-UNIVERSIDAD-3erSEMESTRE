class Animal{
    constructor(nombre, tipo, voz){
        this.nombre=nombre;
        this.tipo=tipo;
        this.voz=voz;
    }
    presentarse(){
        return "hola me llamo "+this.nombre;
    }

    especificar(){
        return " soy un/a " + this.tipo;
    }

    hablar(){
        return " y hago " + this.voz;
    }

} 


   
class Terrestre extends Animal{
    constructor(nombre, tipo, voz, especie){
        super(nombre, tipo, voz);
        this.especie=especie;
    }

    tipo_especie(){
        return " soy terrestre de especie "+this.especie;
    }
}



class Acuatico extends Animal{
    constructor(nombre, tipo, voz, habitad){
        super(nombre, tipo, voz);
        this.habitad=habitad;
    }

    tipo_habitad(){
        return " soy acuatico y mi habitad es "+this.habitad;
    }
}
/*
let animales = new Animal("toby", "perro", "guau")


let animalterrestre = new Terrestre("toby", "perro", "guau", "canino")


document.getElementById("demo").innerHTML=animales.presentarse()+animales.especificar()+animales.hablar()+
"<br>"+animalterrestre.presentarse()+animalterrestre.especificar()+animalterrestre.hablar()+animalterrestre.tipo_especie()



let animales = [new Terrestre("toby", "perro", "guau", "canino"), new Acuatico("dory", "pez", "glu glu", "oceano")]
animales.forEach(animal=>{
    document.getElementById("demo").innerHTML+=animal.presentarse()+animal.especificar()+animal.hablar()+"<br>"

})
*/

let animales = [
    new Terrestre("Toby", "Perro", "Guau", "Canino"),
    new Acuatico("Dory", "Pez", "Glu Glu", "Oceano")
]

animales.forEach(animal => {
    document.getElementById("demo").innerHTML += animal.presentarse() + animal.especificar() + animal.hablar()
    if (animal instanceof Acuatico)
        document.getElementById("demo").innerHTML += animal.tipo_habitad()
    else if (animal instanceof Terrestre)
        document.getElementById("demo").innerHTML += animal.tipo_especie()

    document.getElementById("demo").innerHTML += "<br>"
})