const performance = require('perf_hooks');
function contar(n){
    for (let i =0; i< n; i++){
        console.log(i);
    }
}
let inicio=performance.performance.now();
contar(5);
let=final= performance.performance.now();
let duracion= final-inicio;
console.log(`el algoritmo contor ha durado ${duracion}ms.`)