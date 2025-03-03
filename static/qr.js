const colorInput = document.getElementById("color");
const bgcolorInput = document.getElementById("bgcolor");
const qrDots = document.querySelector("#vector path");
const qr = document.querySelector("#qr");

colorInput.addEventListener("input", function () {
    const colorValue = colorInput.value;
    const bgColorValue = bgcolorInput.value;

    if (colorValue === bgColorValue) {
        colorInput.value = "black"; 
    }

    const fillColor = isValidColor(colorInput.value) ? colorInput.value : "black";
    qrDots.setAttribute("fill", fillColor);
});

bgcolorInput.addEventListener("input", function () {
    const colorValue = colorInput.value;
    const bgcolorValue = bgcolorInput.value;

    if (colorValue === bgcolorValue) {
        bgcolorInput.value = "#eceff7";
    }

    const fillColor = isValidColor(bgcolorInput.value) ? bgcolorInput.value : "#eceff7";
    qr.style.backgroundColor = fillColor;
});

function isValidColor(value) {
    const s = new Option().style;
    s.color = value;
    return s.color !== '';
}
