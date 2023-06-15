class Carrito{
    constructor(){
      this.productos = [];
    }
    
    agregarProducto(producto){
        this.productos.push(producto);
    }
    
    obtenerPrecioTotal(){
      return this.productos.reduce((total, p) => total + p.precio, 0);
    }
  }
  
  const carrito = new Carrito();
  cart.agregarProducto({nombre: 'naranja', precio: 1.25});
  cart.agregarProducto({nombre: 'limon', precio: 1.75});
  console.log(carrito.obtenerPrecioTotal());
  //3
  
  const carrito2 = new Carrito();
  console.log(carrito2.obtenerPrecioTotal());
  //0