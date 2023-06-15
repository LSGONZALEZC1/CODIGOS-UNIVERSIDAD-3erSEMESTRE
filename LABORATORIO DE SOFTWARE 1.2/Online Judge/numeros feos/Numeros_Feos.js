function esNumeroFeo(n) {
    while (n % 2 == 0) {
      n /= 2;
    }
    while (n % 3 == 0) {
      n /= 3;
    }
    while (n % 5 == 0) {
      n /= 5;
    }
    return n === 1;
  }
  function buscarNumeroFeo(n) {
    let contador = 0;
    let i = 1;
    while (contador < n) {
      if (esNumeroFeo(i)) {
        contador++;
      }
      i++;
    }
    return i - 1;
  }
  console.log(`El número feo 1500 es ${buscarNumeroFeo(1500)}`);
  