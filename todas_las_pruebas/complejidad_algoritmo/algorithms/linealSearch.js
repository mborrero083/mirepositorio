function linearSearch(arreglo, clave) { 
    for (let indice = 0; indice < arreglo.length; indice++) { // O(n)
      if (arreglo[indice] === clave) { // O(1)
        return indice; // O(1)
      }
    }
    return -1; // O(1)
  }