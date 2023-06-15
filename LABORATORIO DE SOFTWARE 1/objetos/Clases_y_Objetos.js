class Persona{
    constructor(nombre, apellido, edad, nacionalidad){
        this.nombre=nombre;
        this.apellido=apellido;
        this.edad=edad;
        this.nacionalidad=nacionalidad;
    }

    Presentacion(){
        return "Hola, soy "+this.nombre+" "+this.apellido+", tengo "+this.edad+" años y soy "+this.nacionalidad+".";
    }

}

class Doctor extends Persona{
    constructor(nombre, apellido, edad, nacionalidad, especialidad){
        super(nombre, apellido, edad, nacionalidad);
        this.especialidad=especialidad;
    }
    
    Especializacion(){
        return "Soy doctor/a especializad@ en "+this.especialidad+".";
    }
}

class Ingeniero extends Persona{
    constructor(nombre, apellido, edad, nacionalidad, tipo){
        super(nombre, apellido, edad, nacionalidad);
        this.tipo=tipo;
    }

    Campo(){
        return "Soy ingenier@ de "+this.tipo+".";
    }
}

class Docente extends Persona{
    constructor(nombre, apellido, edad, nacionalidad, materia){
        super(nombre, apellido, edad, nacionalidad);
        this.materia=materia;
    }

    Materia(){
        return "Soy docente de "+this.materia+".";
    }
}

class Otro extends Persona{
    constructor(nombre, apellido, edad, nacionalidad, ocupacion){
        super(nombre, apellido, edad, nacionalidad);
        this.ocupacion=ocupacion;
    }

    Ocupacion(){
        return "Soy un/a "+this.ocupacion+".";
    }
}

let personas=[
    new Persona("amira", "gonzalez", 24, "Mexicana"),
    new Doctor ("lorena", "mendoza", 28, "Argentina", "neurologia"),
    new Ingeniero ("enrique", "hernandez", 35, "chileno", "civil"),
    new Docente ("erika", "benavidez", 29, "colombiana", "estadistica"),
    new Otro ("jose", "arevalo", 38, "colombiano", "abogado")
]

personas.forEach(persona =>{
    document.getElementById("demo").innerHTML += persona.Presentacion()

    if (persona instanceof Doctor)
        document.getElementById("demo").innerHTML += persona.Especializacion()
    else if (persona instanceof Ingeniero)
        document.getElementById("demo").innerHTML += persona.Campo()
    else if (persona instanceof Docente)
        document.getElementById("demo").innerHTML += persona.Materia()
    else if (persona instanceof Otro)
        document.getElementById("demo").innerHTML += persona.Ocupacion()

    document.getElementById("demo").innerHTML += "<br>"
})