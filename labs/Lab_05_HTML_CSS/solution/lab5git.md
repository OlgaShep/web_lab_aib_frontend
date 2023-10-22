### как выглядит страница компьютерной версии
![комп верс](https://github.com/OlgaShep/web_lab_aib_frontend/blob/main/labs/Lab_05_HTML_CSS/solution/comp_lab5.png)
### как выглядит страница мобильной версии
![мобил верс](https://github.com/OlgaShep/web_lab_aib_frontend/blob/main/labs/Lab_05_HTML_CSS/solution/mobil_lab5.png)
### файл html
```
<!DOCTYPE html>
<html lang="ru">
<html>
<head>
    <title>GenshinFood</title>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <link rel="stylesheet" href="style_lab5.css"/>
    <script src="JavaScript.js"></script>
</head>
<body>

<header>
    <nav>
        <li><a href="#main">Содержимое</a></li>
        <article id="main"></srticle>
            <li><a href="https://genshin.hoyoverse.com/ru/home" target="_blank">Официальный сайт</a></li>
    </nav>
    <p class="logocenter">
        <img src="Genshin-Impact_Logo01.png" width="170" alt="Логотип организации">
    </p>
</header>
<main>
    <h1>Каталог еды Genshin Impact</h1>
    <h2>Новые блюда</h2>
    <div class="main-catalog">
        <div class="item">
            <img src="foto_food/NEWPoslepoludennyychay.png" alt="Послеполуденный чай">
            <p>&#11088;&#11088;&#11088; <br>Послеполуденный чай</p>
        </div>
        <div class="item">
            <img src="foto_food/NEWfarshirovannyepomidoryponaboneski.png" alt="Фаршированные помидоры по-набонэски">
            <p>&#11088;&#11088;&#11088; <br>Фаршированные помидоры по-набонэски</p>
        </div>
        <div class="item">
            <img src="foto_food/NEWkrepsyuzett.png" alt="Креп-сюзетт">
            <p>&#11088;&#11088;&#11088; <br>Креп-сюзетт</p>
        </div>
        <div class="item">
            <img src="foto_food/NEWkofeynyybavarua.png" alt="Кофейный баваруа">
            <p>&#11088;&#11088;&#11088; <br>Кофейный баваруа</p>
        </div>
        <div class="item">
            <img src="foto_food/IskushenieAdepta.png" alt="Искушение адепта">
            <p>&#11088;&#11088;&#11088;&#11088;&#11088; <br>Искушение адепта</p>
        </div>
        <div class="item">
            <img src="foto_food/Blyudobezbudushchego.png" alt="Блюдо без будущего">
            <p>&#11088;&#11088;&#11088; <br>Блюдо без будущего</p>
        </div>
    </div>
    <h2>Популярные товары</h2>
    <div class="promo-catalog">
        <div class="item2">
            <img src="foto_food/Vsepogodnayakrasota.png" alt="Всепогодная красота">
            <p>&#11088; <br>Всепогодная красота</p>
        </div>
        <div class="item2">
            <img src="foto_food/Vechnayavera.png" alt="Вечная вера">
            <p>&#11088; <br>Вечная вера</p>
        </div>
        <div class="item2">
            <img src="foto_food/LepyeshkaMora.png" alt="Лепешка Мора">
            <p>&#11088; <br>Лепешка Мора</p>
        </div>
        <div class="item2">
            <img src="foto_food/tsyplyenokvmedovomsouse.png" alt="Цыпленок в медовом соусе">
            <p>&#11088;&#11088; <br>Цыпленок в медовом соусе</p>
        </div>
        <div class="item2">
            <img src="foto_food/Lapshaudon.png" alt="Лапша Удон">
            <p>&#11088;&#11088; <br>Лапша Удон</p>
        </div>
        <div class="item2">
            <img src="foto_food/Snegnagorne.png" alt="Снег на горне">
            <p>&#11088;&#11088;&#11088; <br>Снег на горне</p>
        </div>
        <div class="item2">
            <img src="foto_food/OdnazhdyvMondshtadte.png" alt="Однажды в Мондштадте">
            <p>&#11088;&#11088;&#11088; <br>Однажды в Мондштадте</p>
        </div>
        <div class="item2">
            <img src="foto_food/Udivitelnyyson.png" alt="Удивительный сон">
            <p>&#11088;&#11088;&#11088; <br>Удивительный сон</p>
        </div>
        <div class="item2">
            <img src="foto_food/SHarikiskrevetkoy.png" alt="Вкусные шарики с креветкой">
            <p>&#11088;&#11088;&#11088; <br>Вкусные шарики с креветкой</p>
        </div>
        <div class="item2">
            <img src="foto_food/myasnayapitstsasgribami.png" alt="Мясная пицца с грибами">
            <p>&#11088;&#11088;&#11088;&#11088; <br>Мясная пицца с грибами</p>
        </div>
        <div class="item2">
            <img src="foto_food/KartofelnyeoladiVolchilapki.png" alt="Картофельные оладьи Волчьи лапки">
            <p>&#11088;&#11088;&#11088;&#11088; <br>Картофельные оладьи "Волчьи лапки"</p>
        </div>
        <div class="item2">
            <img src="foto_food/Nefritovyemeshochki.png" alt="Нефритовые мешочки">
            <p>&#11088;&#11088;&#11088;&#11088; <br>Нефритовые мешочки</p>
        </div>
</main>
<footer>
    <p>лабораторная №5. сделала Шепелева Оля АСБ-3-037</p>
</footer>
</body>
</html>
```
### файл стилей style_lab5.css
```
header {
width:100%;
background: AliceBlue;
height: 110px;
position: fixed;
margin-bottom: 0px;
}
main {
padding-top: 100px;
}
.logocenter {
    text-align: center;
}
h1, h2, p {
font-family: franklin gothic medium;
}
nav {
float: right;
margin-right: 50px;
line-height: 30px;
}
a, p{
color: Navy;
}
.item {
background: AliceBlue;
width: 440px;
height: 300px;
margin-bottom: 10px;
margin-left: 25px;
}
.item2 {
background: AliceBlue;
width: 40%;
height: 300px;
margin-bottom: 10px;
margin-left:5%;
}
img {
width: 200px;
}
.main-catalog {
text-align: center;
align-item: center;
display: flex;
flex-wrap: wrap;
padding-left: 12px;
padding-right: 12px;
margin-top: 20px;
margin-bottom: 20px;
}
.promo-catalog {
text-align: center;
align-item: center;
display: flex;
flex-wrap: wrap;
padding-left: 12px;
padding-right: 12px;
margin-top: 20px;
margin-bottom: 20px;
}
@media (min-width: 1280px) {
.item2{
width:20%;
margin-bottom: 30px;
margin-left:4%;
}
}
```
файл JavaScript.js ничего не содержит