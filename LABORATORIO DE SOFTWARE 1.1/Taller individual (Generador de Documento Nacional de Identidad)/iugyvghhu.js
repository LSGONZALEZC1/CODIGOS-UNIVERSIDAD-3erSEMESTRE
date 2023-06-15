const generarDLI = (nombres, apellidos, diaNacimiento, mesNacimiento, anioNacimiento, ciudadNacimiento, departamentoNacimiento, paisNacimiento, grupoSanguineo, rh, genero) => {
    let dli = '';
  
    // Primera letra del primer apellido
    dli += apellidos.split(' ').map(apellido => apellido.charAt(0)).join('');;
  
    // Tres primeras letras del nombre
    dli += nombres.split(' ').map(nombre => nombre.charAt(0)).join('');

    // Día de nacimiento con dos cifras
    dli += diaNacimiento;


    dli += mesNacimiento.substr(0, 3);


  /*
    // Abreviatura del mes de nacimiento
    switch (mesNacimiento.toLowerCase()) {
      case 'enero':
        dli += '01';
        break;
      case 'febrero':
        dli += '02';
        break;
      case 'marzo':
        dli += '03';
        break;
      case 'abril':
        dli += '04';
        break;
      case 'mayo':
        dli += '05';
        break;
      case 'junio':
        dli += '06';
        break;
      case 'julio':
        dli += '07';
        break;
      case 'agosto':
        dli += '08';
        break;
      case 'septiembre':
        dli += '09';
        break;
      case 'octubre':
        dli += '10';
        break;
      case 'noviembre':
        dli += '11';
        break;
      case 'diciembre':
        dli += '12';
        break;
      default:
        throw new Error('Mes de nacimiento no válido');
    }

    */

    // año
    dli += anioNacimiento;

    // Ciudad
    dli += ciudadNacimiento.substr(0, 3);
  
    // Departamento
    dli += departamentoNacimiento.substr(0, 3);
  
    // País
    dli += paisNacimiento.substr(0, 3);
  
    // Género 
    dli += genero.charAt(0).toUpperCase();
  
    // Grupo sanguíneo y RH
    dli += grupoSanguineo + rh;
  
    // Secuencia
    dli += '1';
  
    return dli;
  };
  
  const dli = generarDLI('Pedro Pablo', 'Perez Prieto', '10', 'Octubre', '1978', 'Guatavita', 'Cundinamarca', 'Colombia', 'AB', '+', 'Masculino');
  
  console.log(dli);