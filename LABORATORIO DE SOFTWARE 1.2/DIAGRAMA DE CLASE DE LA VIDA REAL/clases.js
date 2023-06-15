class Personas{
    constructor(nombre, edad, nacionalidad){
        this.nombre=nombre;
        this.edad=edad;
        this.nacionalidad=nacionalidad;
    }
    presentacion(){
        return "Me llamo "+this.nombre+", tengo "+this.edad+" años y soy de "+this.nacionalidad+".\n"
    }
}

class Trabajador extends Personas{
    constructor(nombre, edad, nacionalidad, codigo, cargo, salario_mes){
        super(nombre,edad,nacionalidad);
        this.codigo=codigo;
        this.cargo=cargo;
        this.salario_mes=salario_mes;
    }
    identificacion(){
        return "Trabajador\n\nMi codigo de trabajador es "+this.codigo+", mi cargo en la empresa es "+this.cargo+" y gano un promedio de "+this.salario_mes+" mensuales.\n"
    }
    salario_promedio_año(){
        return "Me gano un promedio de "+this.salario_mes*12+" en el año.\n"
    }
}

class Cliente extends Personas{
    constructor (nombre, edad, nacionalidad, num_contacto, direccion){
        super(nombre,edad,nacionalidad);
        this.num_contacto=num_contacto;
        this.direccion=direccion;
    }
    informacion(){
        return "Cliente\n\nNumero de contacto: "+this.num_contacto+"\nDireccion: "+this.direccion;
    }
}


let Personas = [
    new Trabajador("Nikolas Andrade", 25, "Colombia", 3659861425, "Operario", 1350000),
    new Cliente("Andrea Rojas", 34, "Colombia", 3652487596, "Calle 10 # 5-51")
]

Personas.forEach(persona => {
    document.getElementById("demo").innerHTML += Personas.presentacion()
    if (Personas instanceof Trabajador)
        document.getElementById("demo").innerHTML += Personas.identificacion() + Personas.salario_promedio_año()
    else if (Personas instanceof Cliente)
        document.getElementById("demo").innerHTML += Personas.informacion()
    
        document.getElementById("demo").innerHTML += "<br>"
});