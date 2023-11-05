### задание 1
файл index.html
```
<!DOCTYPE html>
<html lang="ru">
    <head>
        <meta charset="UTF-8"/>
        <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
        <title>lab8</title>
    </head>
    <body style="height: 100%;">
        <input class="buttons" type="button" id="Crimson" value="малиновый">
        <input class="buttons" type="button" id="BlueViolet" value="фиолетовый">
        <input class="buttons" type="button" value="темно-синий">
    </body>
    <script src="app.js"></script>
</html>
```
файл app.js
```
document.addEventListener("DOMContentLoaded", () => {
    let button = document.getElementsByClassName("buttons")
    let body = document.querySelector("body")
    console.log(body);

    for (let i = 0 ; i < button.length ; i++) {
        button[i].addEventListener("click", function() {
            if (button[i].getAttribute("id") == "Crimson") {
                console.log(body);
                body.style['background-color'] = "Crimson";
            }
            else if (button[i].getAttribute("id") == "BlueViolet") {
                body.style['background-color'] = "BlueViolet";
            }
            else {
                body.style['background-color'] = "Navy";
            }
        })
    }
})
```
работа страницы

начальное состояние

![start](https://github.com/OlgaShep/web_lab_aib_frontend/blob/main/labs/Lab_08_events_js/solution/foto/start.PNG)

кнопка 1, малиновый

![vkl_crimson](https://github.com/OlgaShep/web_lab_aib_frontend/blob/main/labs/Lab_08_events_js/solution/foto/vkl_crimson.PNG)

кнопка 2, фиолетовый

![vkl_blueviolet](https://github.com/OlgaShep/web_lab_aib_frontend/blob/main/labs/Lab_08_events_js/solution/foto/vkl_blueviolet.PNG)

кнопка 3, темно-синий

![vkl_navy](https://github.com/OlgaShep/web_lab_aib_frontend/blob/main/labs/Lab_08_events_js/solution/foto/vkl_navy.PNG)

### задание 2
основной файл index.html
```
<!DOCTYPE html>
<html lang="ru">
    <head>
        <meta charset="UTF-8"/>
        <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
        <link rel="stylesheet" href="style.css" />
        <title>lab8</title>
    </head>
    <body>
        <div class="color-box">
        <div>
            <label for="redInput">Red:</label>
            <input type="number" id="redInput" min="0" max="255">
            <label for="greenInput">Green:</label>
            <input type="number" id="greenInput" min="0" max="255">
            <label for="blueInput">Blue:</label>
            <input type="number" id="blueInput" min="0" max="255">
        </div>
            <div id="colorSquare" class="color-square"> </div>
        </div>
    </body>
    <script src="app.js"></script>
</html>
```
файл style.css cодержащий стили
```
        .color-box {
            display: flex;
            align-items: center;
        }
        .color-square {
            width: 300px;
            height: 300px;
            border: 3px solid black;
            margin-left: 30px;
        }
```
файл app.js содержащий функцию, благодаря которой тут всё работает
```
const redInput = document.getElementById('redInput');
const greenInput = document.getElementById('greenInput');
const blueInput = document.getElementById('blueInput');
const colorSquare = document.getElementById('colorSquare');

function changeBackgroundColor() {
    const red = redInput.value || 0;
    const green = greenInput.value || 0;
    const blue = blueInput.value || 0;

    if (red >= 0 && red <= 255 && green >= 0 && green <= 255 && blue >= 0 && blue <= 255) {
        const rgbColor = `rgb(${red}, ${green}, ${blue})`;
        colorSquare.style.backgroundColor = rgbColor;
    } else {
        colorSquare.style.backgroundColor = 'white';
    }
}

redInput.addEventListener('input', changeBackgroundColor);
greenInput.addEventListener('input', changeBackgroundColor);
blueInput.addEventListener('input', changeBackgroundColor);

changeBackgroundColor();
```
здесь показана работа страницы, если мы установим значения "red 122, green 23, blue 85". мы можем изменять значения, вводя другие числа
![задание 2](https://github.com/OlgaShep/web_lab_aib_frontend/blob/main/labs/Lab_08_events_js/solution/foto/task2.PNG)

### задание 3
основной файл index.html
```
<!DOCTYPE html>
<html lang="ru">
    <head>
        <meta charset="UTF-8"/>
        <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
        <link rel="stylesheet" href="style.css" />
        <title>lab8</title>
    </head>
    <body>
        <div class="color-box">
        <div>
            <label for="redInput">Red:</label>
            <input type="number" id="redInput" min="0" max="255">
            <label for="greenInput">Green:</label>
            <input type="number" id="greenInput" min="0" max="255">
            <label for="blueInput">Blue:</label>
            <input type="number" id="blueInput" min="0" max="255">
        </div>
            <div id="colorSquare" class="color-square"> </div>
        </div>
        <div class="color-box">
        <button id="generateButton">Сгенерировать</button>
        </div>
        <div class="color-area" id="colorArea"></div>
    </body>
    <script src="app.js"></script>
</html>
```
файл style.css cодержащий стили
```
        .color-box {
            display: flex;
            align-items: center;
        }
        .color-square {
            width: 300px;
            height: 300px;
            border: 3px solid black;
            margin-left: 30px;
        }
        .color-area {
            width: 100%;
            min-height: 300px;
            display: flex;
            flex-wrap: wrap;
        }
        .color-block {
            width: 100px;
            height: 100px;
            margin: 10px;
        }
```
файл app.js содержащий функцию
```
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
        alert('Неверное значение цвета'); // это всплывающее окно нужно на случай, если пользователь введет число больше 255
    }
}
```
итоговая страница
![задание 3](https://github.com/OlgaShep/web_lab_aib_frontend/blob/main/labs/Lab_08_events_js/solution/foto/task3.PNG)
### задание 4
основной файл index.html оставим без изменений (как в задании 3)

В файл style.css cодержащий стили в стиль для .color-block добавим cursor: pointer;. Остальное оставим как в задании 3
````
.color-block {
            width: 100px;
            height: 100px;
            margin: 10px;
            cursor: pointer;
        }
````
файл app.js содержащий функцию
````
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
````
итоговая страница
![задание 4](https://github.com/OlgaShep/web_lab_aib_frontend/blob/main/labs/Lab_08_events_js/solution/foto/task4.PNG)