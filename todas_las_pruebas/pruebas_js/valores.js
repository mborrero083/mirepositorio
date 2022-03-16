function perimetrocuadrado(lado){
    return lado*4;
}

function areacuadrado(lado){
    return lado*lado;
}

function CalcularPerimetroCuadrado(){
    const input= document.getElementById("InputCuadrado");
    const value=input.value;
    const perimetro=perimetrocuadrado(value);
    alert(perimetro);
}
function CalcularAreaCuadrado(){
    const input= document.getElementById("InputCuadrado");
    const value=input.value;
    const area=areacuadrado(value);
    alert(area);
}