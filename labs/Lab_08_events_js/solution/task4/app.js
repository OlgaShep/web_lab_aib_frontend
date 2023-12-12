const redInput = document.getElementById('redInput');
const greenInput = document.getElementById('greenInput');
const blueInput = document.getElementById('blueInput');
const generateButton = document.getElementById('generateButton');
const colorArea = document.getElementById('colorArea');
const colorSquare = document.getElementById('colorSquare');
let savedColor = null;

generateButton.addEventListener('click', generateColorBlock);
colorArea.addEventListener('click', changeBackgroundColor);

function generateColorBlock() {
    const red = redInput.value || 0;
    const green = greenInput.value || 0;
    const blue = blueInput.value || 0;

    if (red >= 0 && red <= 255 && green >= 0 && green <= 255 && blue >= 0 && blue <= 255) {
        const rgbColor = `rgb(${red}, ${green}, ${blue})`;

        colorSquare.style.backgroundColor = rgbColor;

        const colorBlock = document.createElement('div');
        colorBlock.style.backgroundColor = rgbColor;
        colorBlock.className = 'color-block';
        colorBlock.style.border = '2px solid black';

        colorArea.appendChild(colorBlock);

        const colorBlocks = colorArea.querySelectorAll('.color-block');
        if (colorBlocks.length > 15) {
            colorArea.removeChild(colorBlocks[0]);
        }

        savedColor = rgbColor;
    } else {
        alert('Неверное значение цвета');
    }
}

function changeBackgroundColor(event) {
    const target = event.target;

    if (target.classList.contains('color-block')) {
        if (target !== colorSquare) {
            document.body.style.backgroundColor = target.style.backgroundColor;
        }
    } else if (target !== colorSquare) {
        document.body.style.backgroundColor = savedColor;
    }
}