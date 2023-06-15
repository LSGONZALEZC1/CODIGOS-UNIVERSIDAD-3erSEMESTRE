class Pila {
    constructor() {
      this.items = [];
    }
  
    // Agrega un elemento a la pila
    push(elemento) {
      this.items.push(elemento);
    }
  
    // Elimina y devuelve el elemento en la cima de la pila
    pop() {
      if (this.items.length === 0) {
        return null;
      }
      return this.items.pop();
    }
  
    // Devuelve el elemento en la cima de la pila sin eliminarlo
    peek() {
      if (this.items.length === 0) {
        return null;
      }
      return this.items[this.items.length - 1];
    }
  
    // Devuelve el tamaño de la pila
    size() {
      return this.items.length;
    }
  }
  
  // Crear una pila con los personajes de la MCU
  const pilaMCU = new Pila();
  pilaMCU.push({ nombre: 'Iron Man', peliculas: 3 });
  pilaMCU.push({ nombre: 'Capitán América', peliculas: 4 });
  pilaMCU.push({ nombre: 'Thor', peliculas: 5 });
  pilaMCU.push({ nombre: 'Hulk', peliculas: 2 });
  pilaMCU.push({ nombre: 'Viuda Negra', peliculas: 7 });
  pilaMCU.push({ nombre: 'Ojo de Halcón', peliculas: 3 });
  pilaMCU.push({ nombre: 'Rocket Raccoon', peliculas: 3 });
  pilaMCU.push({ nombre: 'Groot', peliculas: 3 });
  pilaMCU.push({ nombre: 'Dr. Strange', peliculas: 2 });
  pilaMCU.push({ nombre: 'Pantera Negra', peliculas: 2 });
  pilaMCU.push({ nombre: 'Spider-Man', peliculas: 3 });
  
  // a. Determinar en qué posición se encuentran Rocket Raccoon y Groot
  function posicionRocketYGroot(pila) {
    let posicionRocket = null;
    let posicionGroot = null;
    let posicion = 1;
    while (pila.size() > 0) {
      const personaje = pila.pop();
      if (personaje.nombre === 'Rocket Raccoon') {
        posicionRocket = posicion;
      }
      if (personaje.nombre === 'Groot') {
        posicionGroot = posicion;
      }
      posicion++;
    }
    console.log(`Rocket Raccoon está en la posición ${posicionRocket}`);
    console.log(`Groot está en la posición ${posicionGroot}`);
  }
  posicionRocketYGroot(pilaMCU);
  
  // b. Determinar los personajes que participaron en más de 5 películas de la saga
  function personajesMasDe5Peliculas(pila) {
    const personajes = [];
    while (pila.size() > 0) {
      const personaje = pila.pop();
      if (personaje.peliculas > 5) {
        personajes.push({ nombre: personaje.nombre, peliculas: personaje.peliculas });
      }
    }
    console.log('Personajes con más de 5 películas:');
    personajes.forEach((p) => console.log(`${p.nombre} (${p.peliculas} películas)`));
  }
  personajesMasDe5Peliculas(pilaMCU);
  
  // c. Determinar en cuántas películas participó la Viuda Negra (Black Widow)
  function peliculasViudaNegra(pila) {
    let peliculas = null;
    while (pila.size() > 0) {
      const personaje = pila.pop();
      if (personaje.nombre === 'Viuda Negra') {
        peliculas = personaje.peliculas;
      }
    }
    console.log(`La Viuda Negra participó en ${peliculas} películas`);
  }
  peliculasViudaNegra(pilaMCU);
  
  // d. Mostrar todos los personajes cuyos nombres empiezan con C, D y G
  function personajesPorInicial(pila, inicial) {
    const personajes = [];
    while (pila.size() > 0) {
      const personaje = pila.pop();
      if (personaje.nombre.charAt(0) === inicial) {
        personajes.push(personaje.nombre);
      }
    }
    console.log(`Personajes que empiezan con ${inicial}: ${personajes.join(', ')}`);
  }
  personajesPorInicial(pilaMCU, 'C');
  personajesPorInicial(pilaMCU, 'D');
  personajesPorInicial(pilaMCU, 'G');