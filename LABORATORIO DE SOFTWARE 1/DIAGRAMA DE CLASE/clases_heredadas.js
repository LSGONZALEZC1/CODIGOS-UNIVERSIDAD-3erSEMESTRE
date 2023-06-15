class Persona{
    constructor(nombre, apellido, edad, nacionalidad){
        this.nombre=nombre;
        this.apellido=apellido;
        this.edad=edad;
        this.nacionalidad=nacionalidad;
    }

    Presentacion(){
        return "Hola, me llamo "+this.nombre+" "+this.apellido+", tengo "+this.edad+" años y soy "+this.nacionalidad+".";
    }

}

class Estudiante extends Persona{
    constructor(nombre, apellido, edad, nacionalidad, cod_estudiante){
        super(nombre, apellido, edad, nacionalidad);
        this.cod_estudiante=cod_estudiante;
    }

    Identificacion_est(){
       return "Mi codigo de estudiante es "+this.cod_estudiante+"."; 
    }

}

class Colegio extends Estudiante{
    constructor(nombre, apellido, edad, nacionalidad, cod_estudiante, nom_colegio, grado_academico){
        super (nombre, apellido, edad, nacionalidad, cod_estudiante);
        this.nom_colegio=nom_colegio;
        this.grado_academico=grado_academico;
    }

    Info_colegio(){
        return "Estudio en el colegio "+this.nom_colegio+" y estoy en el grado "+this.grado_academico+".";
    }
}

class Instituto extends Estudiante{
    constructor(nombre, apellido, edad, nacionalidad, cod_estudiante, nom_instituto, nom_curso){
        super(nombre, apellido, edad, nacionalidad, cod_estudiante);
        this.nom_instituto=nom_instituto;
        this.nom_curso=nom_curso;
    }

    Info_instituto(){
        return "Estudio "+this.nom_curso+" en el intituto "+this.nom_instituto+".";
    }
}

class Universidad extends Estudiante{
    constructor(nombre, apellido, edad, nacionalidad, cod_estudiante, nom_universidad, nom_carrera, semestre_actual){
        super(nombre, apellido, edad, nacionalidad, cod_estudiante);
        this.nom_universidad=nom_universidad;
        this.nom_carrera=nom_carrera;
        this.semestre_actual=semestre_actual
    }
    Info_universidad(){
        return "Estoy en "+this.semestre_actual+" semestre de "+this.nom_carrera+" en la universidad "+this.nom_universidad+".";
    }
}

class Profesional extends Persona{
    constructor(nombre, apellido, edad, nacionalidad, num_tarjeta_profesional){
        super(nombre, apellido, edad, nacionalidad);
        this.num_tarjeta_profesional=num_tarjeta_profesional;
    }

    Identificacion_prof(){
        return "Mi numero de tarjeta profesional es "+this.num_tarjeta_profesional+".";
    }
}

class Ingeniero extends Profesional{
    constructor(nombre, apellido, edad, nacionalidad, num_tarjeta_profesional, area){
        super(nombre, apellido, edad, nacionalidad, num_tarjeta_profesional);
        this.area=area;
    }

    Area_ingenieria(){
        return "Soy ingenier@ "+this.area+".";
    }
}

class Doctor extends Profesional{
    constructor(nombre, apellido, edad, nacionalidad, num_tarjeta_profesional, especialidad){
        super(nombre, apellido, edad, nacionalidad, num_tarjeta_profesional);
        this.especialidad=especialidad;
    }

    Especializacion(){
        return "Soy doctor/a especializad@ en "+this.especialidad+".";  
    }
}

class Docente extends Profesional{
    constructor(nombre, apellido, edad, nacionalidad, num_tarjeta_profesional, materia){
        super(nombre, apellido, edad, nacionalidad, num_tarjeta_profesional);
        this.materia=materia;
    }

    Materia(){
        return "Soy docente de "+this.materia+".";
    }
}

class Abogado extends Profesional{
    constructor(nombre, apellido, edad, nacionalidad, num_tarjeta_profesional, tipo){
        super(nombre, apellido, edad, nacionalidad, num_tarjeta_profesional);
        this.tipo=tipo;
    }

    Tipo_abogado(){
        return "Soy abogad@ "+this.tipo+".";
    }
}

class Otro extends Persona{
    constructor(nombre, apellido, edad, nacionalidad, ocupacion){
        super(nombre, apellido, edad, nacionalidad);
        this.ocupacion=ocupacion;
    }

    Ocupacion(){
        return "Soy "+this.ocupacion+".";
    }
}


let personas=[
    new Persona ("aura", "castaño", 57, "colombiana"), 
    new Estudiante ("alvaro", "ramirez", 28, "mexicano", 5487269855),
    new Colegio ("andrea", "castillo", 16, "colombiana", 1542686693, "llano verde", 11),
    new Instituto ("andres", "lopez", 35, "español", 1542688875, "Tecnico Ocupacional", "contabilidad"),
    new Universidad ("david", "rocha", 19, "chileno", 6578963225, "Pontifica Bolivariana", "psicologia", 5),
    new Profesional ("esteban", "campo", 24, "español", 2543666978),
    new Ingeniero ("yessica", "obando", 34, "colombiana", 2225446966, "civil"),
    new Doctor ("alejandra", "hoyos", 29, "argentina", 1555453633, "neurologia"),
    new Docente ("juan", "gomez", 38, "chileto", 4555778896, "filosofia"),
    new Abogado ("erika", "benavidez", 45, "mexicana", 5556668875, "de familia"),
    new Otro ("blanca", "ramirez", 58, "colombiana", "trabajadora independiente")
]

personas.forEach(persona =>{
    document.getElementById("demo").innerHTML += persona.Presentacion()

    if (persona instanceof Estudiante)
        document.getElementById("demo").innerHTML += persona.Identificacion_est()
    else if (persona instanceof Colegio)
        document.getElementById("demo").innerHTML += persona.Info_colegio()
    else if (persona instanceof Instituto)
        document.getElementById("demo").innerHTML += persona.Info_instituto()
    else if (persona instanceof Universidad)
        document.getElementById("demo").innerHTML += persona.Info_universidad()
    else if (persona instanceof Profesional)
        document.getElementById("demo").innerHTML += persona.Identificacion_prof()
    else if (persona instanceof Ingeniero)
        document.getElementById("demo").innerHTML += persona.Area_ingenieria()
    else if (persona instanceof Doctor)
        document.getElementById("demo").innerHTML += persona.Especializacion()
    else if (persona instanceof Docente)
        document.getElementById("demo").innerHTML += persona.Materia()
    else if (persona instanceof Abogado)
        document.getElementById("demo").innerHTML += persona.Tipo_abogado()
    else if (persona instanceof Otro)
        document.getElementById("demo").innerHTML += persona.Ocupacion()


    document.getElementById("demo").innerHTML += "<br>"
    document.getElementById("demo").innerHTML += "<br>"
})