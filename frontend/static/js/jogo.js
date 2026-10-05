const botaoAbrirInventario = document.getElementById(
    "abrir-inventario"
);

const popupInventario = document.getElementById(
    "popup-inventario"
);

const botaoFecharInventario = document.getElementById(
    "fechar-inventario"
);


botaoAbrirInventario.addEventListener("click", () => {

    popupInventario.hidden = false;

});


botaoFecharInventario.addEventListener("click", () => {

    popupInventario.hidden = true;

});