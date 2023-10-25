### Задание 1. level stone
стоит сменить var на let ведь мы современные и живем в 2023 веке и сменить имена переменных, перенести переменные в разные строки кода, убрать повторное объявление первой переменной. и надо навести эстетику в оформлении функции
```
let FirstPrompt = prompt('var one'),
    SecondPrompt = prompt('var two');
    
if (FirstPrompt === SecondPrompt) {
    console.log('equally');
}
else {
    console.log('no equally');
}

let World = 'world';
FirstPrompt = FirstPrompt + World;
```
### Задание 2. level iron
мда ну тут треш полный, а не исходник кнчн... для 10 строчек вывода такой кошмар создавать :((
```
let ColourFruits = {
    'apple': 'green',
    'strawberry': 'red',
    'blueberry': 'blue',
    'raspberry': 'light red',
    'lemon': 'yellow'
} 

fruit = Object.keys(ColourFruits)
colour = Object.values(ColourFruits)

for (let key in fruit) {
    console.log(fruit[key]);
}
    
for (let key in fruit) {
    console.log(fruit[key] + ' ' + colour[key]);
}
```

### Задание 3. level gold
c днем расстановки пробелов и табуляции. код стал длиннее, но зато понятнее
```
let CountPeople = prompt ('Введите кол-во человек ', undefined);

if (!isNaN(parseFloat(CountPeople))) {
    CountPeople = parseFloat(CountPeople);
}
else {
    CountPeople = 0;
}

while(CountPeople === 0) {
    let CountPeople = prompt ('Введите кол-во человек ', undefined);
    if (!isNaN(parseFloat(CountPeople))) {
        CountPeople = parseFloat(CountPeople);
    }
    else {
        CountPeople = 0;
    }
}

let salary = prompt ('Введите зарплату на человека ', undefined);

if (!isNaN(parseFloat(salary))) {
    salary=parseFloat(salary);
}
else {
    salary = 0;
}

while (CountPeople === 0) {
    let salary = prompt('Введите зарплату на человека ', undefined);
    if (!isNaN(parseFloat(salary))) {
        salary = parseFloat(salary)
    } else {
        salary = 0;
    }
}

alert('Затраты на ЗП: ' + CountPeople * salary);
```

### Задание 4
ну мы выключили транслитерацию (как слышим, так и пишем, но другими буквами) и включили нормальный переводчик с русского на английский
```
let ClassStudent = [
    {FIO: 'Петров А.А.', Rating: 5 },
    {FIO: 'Иванов Б.Б.', Rating: 3.4 },
    {FIO: 'Сидоров Г.Г.', Rating: 9 },
    {FIO: 'Немолодой Д.Д', Rating: 2 },
    {FIO: 'Молодой Е.Е', Rating: 3.4 }
];

let MeanRating = 0,
    count = 0,
    BadStudent = [];

for (let indexStudent = 0; indexStudent < ClassStudent.length; indexStudent++) {

    if (ClassStudent[indexStudent].Rating > 5) {
        console.log('Это значение учитываться не будет оно не соответствует допустимым значениям');
    }

    if (ClassStudent[indexStudent].Rating < 0) {
        console.log('Это значение учитываться не будет оно не соответствует допустимым значениям');
    }

    if (! (ClassStudent[indexStudent].Rating <= 5 && ClassStudent[indexStudent].Rating >= 0 )) {
        continue;
    }

    if (ClassStudent[indexStudent].Rating < 4) {
        BadStudent.push(ClassStudent[indexStudent]);
    }

    MeanRating += ClassStudent[indexStudent].Rating;
    count += 1;
}

MeanRating = MeanRating / count;
console.log('Средняя оценка: ' + MeanRating);
console.log('Плохие студенты: ');

if (BadStudent.length === 0) {
    console.log('Таких нет');
}

BadStudent.forEach((index) => { console.log('Фио: ' + index.FIO + '; Оценка: ' + index.Rating) });
```

### Задание 5
ну например в задании 2, можно изменить названия переменных на более осмысленные
```
let apple = 123,
    sliva = '100',
    cherry = true;
```
=>>
```
let number = 123,
    NumberAsString = '100',
    BoolValue = true;
```
