const redInput = document.getElementById('redInput');
const greenInput = document.getElementById('greenInput');
const blueInput = document.getElementById('blueInput');
const generateButton = document.getElementById('generateButton');
const colorArea = document.getElementById('colorArea');

generateButton.addEventListener('click', generateColorBlock);

function generateColorBlock() {
    const red = redInput.value || 0;
    const green = greenInput.value || 0;
    const blue = blueInput.value || 0;

    if (red >= 0 && red <= 255 && green >= 0 && green <= 255 && blue >= 0 && blue <= 255) {
        const rgbColor = `rgb(${red}, ${green}, ${blue})`;

        const colorBlock = document.createElement('div');
        colorBlock.style.backgroundColor = rgbColor;
        colorBlock.className = 'color-block';
        colorArea.appendChild(colorBlock);

        const colorBlocks = colorArea.querySelectorAll('.color-block');
        if (colorBlocks.length > 15) {
            colorArea.removeChild(colorBlocks[0]);
        }
        const colorSquare = document.getElementById('colorSquare');
        colorSquare.style.backgroundColor = rgbColor;
    }
    else {
        alert('Неверное значение цвета');
    }
}
