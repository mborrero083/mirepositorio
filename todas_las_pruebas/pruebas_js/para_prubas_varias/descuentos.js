function calcularPrecioconDescuento(precio,descuento){
    const porcentajepreciocondescuento=100-descuento;
    const preciocondescuento=(precio*porcentajepreciocondescuento)/100 ;
    return preciocondescuento;   
}
function onClickButtonPriceDiscount() {
    const inputPrice = document.getElementById("InputPrice");
    const priceValue = inputPrice.value;
    
    const inputDiscount = document.getElementById("InputDiscount");
    const discountValue = inputDiscount.value;

    const precioConDescuento = calcularPrecioconDescuento(priceValue, discountValue);
    const resultP = document.getElementById("ResultP");
    resultP.innerText = "El precio con descuento son: $" + precioConDescuento;
}
