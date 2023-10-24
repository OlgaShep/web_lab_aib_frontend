### задание 1 Работа с переменными
код html
```
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <title>JS</title>
</head>
<body>
<script>
    let apple = 10;
    alert(apple);
    console.log(apple);
    let conditions = "stroka";
    alert(conditions);
    console.log(conditions);
    console.log('Good game is ' + condition);
</script>
</body>
</html>
```

##### окно появляющееся из-за alert(apple)
![alert_apple](https://github.com/OlgaShep/web_lab_aib_frontend/blob/main/labs/Lab_06_intro_js/solution/foto/alert_apple_zadanie1.PNG)
##### окно появляющееся из-за alert(conditions)
![alert_conditions](https://github.com/OlgaShep/web_lab_aib_frontend/blob/main/labs/Lab_06_intro_js/solution/foto/alert_condition_zadanie1.PNG)
##### вывод в console
![console](https://github.com/OlgaShep/web_lab_aib_frontend/blob/main/labs/Lab_06_intro_js/solution/foto/consolelog_zadanie1.PNG)

#### Вопросы
1. Через какой оператор Вы объявили переменую? 
* через оператор let
2. Какие доступны операторы для объявления переменных? В чём их отличия?
* let - самый крутой крч 
* const - нельзя изменить значение переменной
* var - устаревший вариант. допускает повторное объявление, не может быть блочной или локальной внутри цикла. переменная var считается объявленной самого начала исполнения функции вне зависимости от того, в каком месте функции реально находятся их объявления (при условии, что она не находится во вложенной функции). поэтому принято их писать в начале кода программы.
3. Что происходит при вызове alert()?
* выводится значение переменной в всплывающем окне с просьбой подтвердить действие
4. Как Вы думаете для чего может использоваться console.log()
* для того чтобы было легче понть где ошибки, тк если использовать просто alert(), то вывод не фиксируется в консоли. или для другой работы в консоли

### задание 2 Магия конкатенации
код
```
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <title>JS</title>
</head>
<body>
<script>
    let apple = 123,
        sliva = '100',
        cherry = true;
    console.log(apple);
    console.log(sliva);
    console.log(cherry);
    console.log(apple + apple);
    console.log(sliva + sliva);
    console.log(cherry + cherry);
    console.log(apple + sliva);
    console.log(apple + cherry);
    console.log(sliva + cherry);
</script>
</body>
</html>
```
##### вывод в console
![console_zadanie2](https://github.com/OlgaShep/web_lab_aib_frontend/blob/main/labs/Lab_06_intro_js/solution/foto/consolelog_zadanie2.PNG)

### задание 3 работа с массивами
код
```
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <title>JS</title>
</head>
<body>
<script>
let array = []
for (let i=0; i<10; i++)
    array.push(Math.floor( -15 + 50 * Math.random()));
console.log(array);
array = array.filter(num => num >= 0);
console.log(array);
</script>
</body>
</html>
```
##### вывод в console
![console_zadanie3](https://github.com/OlgaShep/web_lab_aib_frontend/blob/main/labs/Lab_06_intro_js/solution/foto/consolelog_zadanie3.PNG)

### задание 4 Работа с функциями
код
```
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <title>JS</title>
</head>
<body>
<script>

    function getRandomInt(max, min) {
    return Math.floor(min + Math.random() * max);
    }
let pip = getRandomInt(25, -5)
console.log(pip);

let array = []
for (let i=0; i<10; i++)
    array.push(Math.floor( -15 + 50 * Math.random()));
console.log(array);

    function mass2(array, number){
    let new_array = array.map(element => element * number);
    return new_array;
    }

let array2 = mass2(array, pip);
console.log(array2);

let random_word = function() {
  let alphabet = 'йцукенгшщзхъфывапролджэячсмитьбю';
  let word = '';
  for (let i = 0; i < 7; i++) {
    let index = Math.floor(Math.random() * alphabet.length);
    word += alphabet[index];
  }
  return word;
};

console.log(random_word());
</script>
</body>
</html>
```
##### вывод в console
![console_zadanie4](https://github.com/OlgaShep/web_lab_aib_frontend/blob/main/labs/Lab_06_intro_js/solution/foto/consolelog_zadanie4.PNG)

### задание 5 Работа с объектами
код
```
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <title>JS</title>
</head>
<body>
<script>
 let obect = {};
    obect.firstName = 'Olga';
    obect.surname = 'Shepeleva';
    obect.patronymic = 'Romanovna';
    obect.birthday = '21.11.2003';
    obect.hobby = 'sleep';
    obect.group = 'АСБ-037';
obect.get_inform = function () {
    let year = this.birthday.substring(6,10);
    let age = 2023 - year;
    let inf = 'FIO: ' + this.surname + ' ' + this.firstName + ' ' + this.patronymic + ' ' + age + ' '  + year + ' hobby - ' + this.hobby;
    return inf;
    }
alert(obect.get_inform());
console.log(obect.get_inform());

let obect2 = {
    'Лю Цзяна': 10000000,
    'Лю Янбин': 10000000,
    'Ху': 1000000,
    'Цяо': 10000000,
    'Пархоменко': 200000,
    'Шепелева': 500000,
    'Макаревич': 100000,
    'Гисс': 150000,
    'Ким': 200000,
    'Боровинчкий': 1,
    };
let salary = 0;
for (let key in obect2){
    salary += obect2[key];
    }
console.log(salary);
</script>
</body>
</html>
```
##### вывод метода get_inform в alert
![alert_zadani5](https://github.com/OlgaShep/web_lab_aib_frontend/blob/main/labs/Lab_06_intro_js/solution/foto/alert_zadani5.PNGG)
##### вывод в console
![console_zadanie5](https://github.com/OlgaShep/web_lab_aib_frontend/blob/main/labs/Lab_06_intro_js/solution/foto/consolelog_zadanie5.PNG)