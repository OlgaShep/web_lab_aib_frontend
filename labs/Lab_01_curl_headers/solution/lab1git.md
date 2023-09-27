```
Admin@MSI MINGW64 ~
$ git clone https://github.com/OlgaShep/web_lab_aib_frontend.git
Cloning into 'web_lab_aib_frontend'...
remote: Enumerating objects: 129, done.
remote: Counting objects: 100% (56/56), done.
remote: Compressing objects: 100% (35/35), done.
remote: Total 129 (delta 28), reused 40 (delta 21), pack-reused 73
Receiving objects: 100% (129/129), 5.74 MiB | 12.24 MiB/s, done.
Resolving deltas: 100% (38/38), done.
```

## начнем с example
```
Admin@MSI MINGW64 ~
$ curl example.com
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  1256  100  1256    0     0   2746      0 --:--:-- --:--:-- --:--:--  2803<!doctype html>
<html>
<head>
    <title>Example Domain</title>

    <meta charset="utf-8" />
    <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <style type="text/css">
    body {
        background-color: #f0f0f2;
        margin: 0;
        padding: 0;
        font-family: -apple-system, system-ui, BlinkMacSystemFont, "Segoe UI", "Open Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;

    }
    div {
        width: 600px;
        margin: 5em auto;
        padding: 2em;
        background-color: #fdfdff;
        border-radius: 0.5em;
        box-shadow: 2px 3px 7px 2px rgba(0,0,0,0.02);
    }
    a:link, a:visited {
        color: #38488f;
        text-decoration: none;
    }
    @media (max-width: 700px) {
        div {
            margin: 0 auto;
            width: auto;
        }
    }
    </style>
</head>

<body>
<div>
    <h1>Example Domain</h1>
    <p>This domain is for use in illustrative examples in documents. You may use this
    domain in literature without prior coordination or asking for permission.</p>
    <p><a href="https://www.iana.org/domains/example">More information...</a></p>
</div>
</body>
</html>
```
## запрос с использованием www.
```
Admin@MSI MINGW64 ~
$ curl www.example.com 
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  1256  100  1256    0     0   2335      0 --:--:-- --:--:-- --:--:--  2369<!doctype html>
<html>
<head>
    <title>Example Domain</title>

    <meta charset="utf-8" />
    <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <style type="text/css">
    body {
        background-color: #f0f0f2;
        margin: 0;
        padding: 0;
        font-family: -apple-system, system-ui, BlinkMacSystemFont, "Segoe UI", "Open Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;

    }
    div {
        width: 600px;
        margin: 5em auto;
        padding: 2em;
        background-color: #fdfdff;
        border-radius: 0.5em;
        box-shadow: 2px 3px 7px 2px rgba(0,0,0,0.02);
    }
    a:link, a:visited {
        color: #38488f;
        text-decoration: none;
    }
    @media (max-width: 700px) {
        div {
            margin: 0 auto;
            width: auto;
        }
    }
    </style>
</head>

<body>
<div>
    <h1>Example Domain</h1>
    <p>This domain is for use in illustrative examples in documents. You may use this
    domain in literature without prior coordination or asking for permission.</p>
    <p><a href="https://www.iana.org/domains/example">More information...</a></p>
</div>
</body>
</html>

Admin@MSI MINGW64 ~
$ curl http://example.com
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  1256  100  1256    0     0   2755      0 --:--:-- --:--:-- --:--:--  2809<!doctype html>
#далее вывод такой же как и при использовании curl www.example.com
```
## с такими запросами - сайт не найден
```
Admin@MSI MINGW64 ~
$ https://example.ru
bash: https://example.ru: No such file or directory
Admin@MSI MINGW64 ~
$ https://example.com
bash: https://example.com: No such file or directory
```
## -k (или --insecure): Отключает проверку сертификата SSL/TLS. Это полезно, когда необходимо выполнить запрос на сервер с самоподписанным или недействительным сертификатом SSL/TLS. 
```
Admin@MSI MINGW64 ~
$ curl -k www.example.com  
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  1256  100  1256    0     0   3031      0 --:--:-- --:--:-- --:--:--  3078<!doctype html>
<html>
<head>
    <title>Example Domain</title>

    <meta charset="utf-8" />
    <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <style type="text/css">
    body {
        background-color: #f0f0f2;
        margin: 0;
        padding: 0;
        font-family: -apple-system, system-ui, BlinkMacSystemFont, "Segoe UI", "Open Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;

    }
    div {
        width: 600px;
        margin: 5em auto;
        padding: 2em;
        background-color: #fdfdff;
        border-radius: 0.5em;
        box-shadow: 2px 3px 7px 2px rgba(0,0,0,0.02);
    }
    a:link, a:visited {
        color: #38488f;
        text-decoration: none;
    }
    @media (max-width: 700px) {
        div {
            margin: 0 auto;
            width: auto;
        }
    }
    </style>
</head>

<body>
<div>
    <h1>Example Domain</h1>
    <p>This domain is for use in illustrative examples in documents. You may use this
    domain in literature without prior coordination or asking for permission.</p>
    <p><a href="https://www.iana.org/domains/example">More information...</a></p>
</div>
</body>
</html>
```
## с использованием опции -s мы можем вывести информацию без заголовков
```
Admin@MSI MINGW64 ~
$ curl -s www.example.com
<!doctype html>
<html>
<head>
    <title>Example Domain</title>

    <meta charset="utf-8" />
    <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <style type="text/css">
    body {
        background-color: #f0f0f2;
        margin: 0;
        padding: 0;
        font-family: -apple-system, system-ui, BlinkMacSystemFont, "Segoe UI", "Open Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;

    }
    div {
        width: 600px;
        margin: 5em auto;
        padding: 2em;
        background-color: #fdfdff;
        border-radius: 0.5em;
        box-shadow: 2px 3px 7px 2px rgba(0,0,0,0.02);
    }
    a:link, a:visited {
        color: #38488f;
        text-decoration: none;
    }
    @media (max-width: 700px) {
        div {
            margin: 0 auto;
            width: auto;
        }
    }
    </style>
</head>

<body>
<div>
    <h1>Example Domain</h1>
    <p>This domain is for use in illustrative examples in documents. You may use this
    domain in literature without prior coordination or asking for permission.</p>
    <p><a href="https://www.iana.org/domains/example">More information...</a></p>
</div>
</body>
</html>
```
## -I -w выводит общую информацию + заголовки
вывод дополнен номером порта с помощью  "%{remote_port}\n"
№ порта это 80, находится ниже остальной информации
```
Admin@MSI MINGW64 ~
$    curl -I -w "%{remote_port}\n" http://example.com
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0   648    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0HTTP/1.1 200 OK
Content-Encoding: gzip #сущность заголовка, используемая для сжатия медиа-типа.
Accept-Ranges: bytes # позволяет серверу указать, что он принимает запросы диапазона для ресурса. здесь принимет запросы bytes
Age: 406121 #передает оценку отправителя количества времени, прошедшего с того момента, как ответ (или его повторная проверка) был сгенерирован на исходном сервере. в секундах
Cache-Control: max-age=604800 #спользуется для указания директив, которым ДОЛЖНА подчиняться вся система кэширования
Content-Type: text/html; charset=UTF-8 #кодировка
Date: Tue, 19 Sep 2023 17:56:55 GMT #текущая дата на сервере
Etag: "3147526947" #хэш ресурса
Expires: Tue, 26 Sep 2023 17:56:55 GMT #выводит дату/время, по истечении которой ответ сервера считается устаревшим.
Last-Modified: Thu, 17 Oct 2019 07:18:26 GMT #указывает дату и время, когда исходный сервер полагает, что вариант был последний раз изменен.
Server: ECS (sec/976A)  #сервер
X-Cache: HIT #Заголовок означает, что контент расположен на CDN (Content Delivery Network), а не на одном сервере.
Content-Length: 648 #Заголовок с информацией о длине контента в символах.

80
```
## на последней строчке - значение хоста ресурса, получен благодаря  "%{url_effective}\n" 
```
Admin@MSI MINGW64 ~
$    curl -I -w "%{url_effective}\n" http://example.com 
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0   648    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0HTTP/1.1 200 OK
Content-Encoding: gzip
Accept-Ranges: bytes
Age: 407272
Cache-Control: max-age=604800
Content-Type: text/html; charset=UTF-8
Date: Tue, 19 Sep 2023 18:16:06 GMT
Etag: "3147526947"
Expires: Tue, 26 Sep 2023 18:16:06 GMT
Last-Modified: Thu, 17 Oct 2019 07:18:26 GMT
Server: ECS (sec/976A)
X-Cache: HIT
Content-Length: 648

http://example.com/  
```
## вывод только информации о формате данных (+заголовки)
```
Admin@MSI MINGW64 ~
$    curl -I http://example.com | grep -iE "content-type"

  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0   648    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
Content-Type: text/html; charset=UTF-8
```
## код ответа и его значение
```
Admin@MSI MINGW64 ~ 
$    curl -I http://example.com | head -n 1 
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0   648    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
HTTP/1.1 200 OK
```
## протокол по которому осуществляется запрос 
```
Admin@MSI MINGW64 ~
$    curl -I http://example.com | awk 'NR==1{print $2}' 
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0   648    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
200
```
## вывод только заголовков
```
Admin@MSI MINGW64 ~ 
$    curl -I http://example.com | grep -iE "x-some-header|other-header"
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0   648    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
```
## вывод текущей даты
```
Admin@MSI MINGW64 ~ 
$ curl -I -s www.example.com | grep -i "Date"
Date: Tue, 19 Sep 2023 19:10:48 GMT
```
## выводит дату/время, по истечении которой ответ сервера считается устаревшим.
```
Admin@MSI MINGW64 ~ 
$ curl -I -s www.example.com | grep -i "Expires"
Expires: Tue, 26 Sep 2023 19:12:28 GMT
```
## выводит сервер
```
Admin@MSI MINGW64 ~ 
$ curl -I -s www.example.com | grep -i "Server"
Server: ECS (sec/96EE)
```
## cache-control 
диктует правила, которые определяют, 
будут ли эти ресурсы загружены из локального кэша данного пользователя, 
или браузер должен отправить запрос на сервер для получения новых ресурсов
Директива ответа max-age=N указывает, что ответ остается свежим в течение N секунд после его создания.
```
Admin@MSI MINGW64 ~
$ curl -I -s www.example.com | grep -i "Cache-Control"
Cache-Control: max-age=604800
```
## аналогично введем запросы для сайта ргупс, самый полный ответ позволяет получить запрос https:
```
Admin@MSI MINGW64 ~
$ curl https://www.rgups.ru
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:--  0:00:01 --:--:--     0<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="
            width=device-width,
            initial-scale=1,
            minimum-scale=1,
            maximum-scale=1,
            user-scalable=0
        ">
        <meta name='yandex-verification' content='4c3682ac42d25e77' />
        <!-- <meta name="google-site-verification" content="eeFosgSGnvQC54hw4ovCoioYdb2wBAaDkpcMX76ZwdE" /> -->
    <title>Главная</title>

    <!-- Styles -->

    <!--link rel="stylesheet" href="/site/templates//styles/main.css"-->
    <link rel="stylesheet" href="/site/templates/design/css/fonts.css">
    <link rel="stylesheet" href="/site/templates/design/css/reset.css">
    <link rel="stylesheet" href="/site/templates/design/css/bootstrap.min.css">
<!--    <link rel="stylesheet" href="/site/templates//design/css/bootstrap-theme.min.css">-->

                <link rel="stylesheet" href="/site/templates/design/css/default.css">
                <link rel="stylesheet" href="/site/templates/design/css/template.css">
                <link rel="stylesheet" href="/site/templates/design/css/pages.css?v=2">
        <link rel="stylesheet" href="/site/templates/design/css/responsive.css">

    <link rel="stylesheet" href="/site/templates/design/css/libs/fancybox.css">
    <link rel="stylesheet" href="/site/templates/design/css/libs/jquery-ui.min.css">
        <link rel="stylesheet" href="/site/templates/design/css/plugins/tooltip-box.css">
    <link rel="stylesheet" href="/site/templates/design/css/ajax-loader.css">


    <link rel="shortcut icon" href="/site/templates/design/images/favicon.ico">

    <!-- Fonts -->
    <!-- <link href='https://fonts.googleapis.com/css?family=Roboto:400,300,400italic,300italic,500,500italic,700,700italic&subset=latin,cyrillic' rel='stylesheet' type='text/css'>
    <link href='https://fonts.googleapis.com/css?family=Roboto+Slab:400,300,700&subset=latin,cyrillic' rel='stylesheet' type='text/css'> -->

        <!-- VK api -->
    <script src="https://vk.com/js/api/openapi.js?137" type="text/javascript"></script>

</head>

<body>


                <div class="navbar navbar-fixed-top">



                <div class=container>
                        <div class="languages">
                                <a class="languages__language" href="/en/" title="Английская версия">
                                        <img src="/site/templates/design/images/langs__en.jpg" alt="Английская версия">EN</a>
                                </div>
                        <div class=navbar-header>
                                <button class="navbar-toggle collapsed" type="button" data-toggle="collapse" data-target="#top-navbar" aria-controls="top-navbar" aria-expanded="false">
                                        <span class="sr-only">Переключить навигацию</span>
                                        <span class="icon-bar"></span>
                                        <span class="icon-bar"></span>
                                        <span class="icon-bar"></span>
                                </button>
                        </div>

                                                <nav class="collapse navbar-collapse" id="top-navbar">
                                <ul class="nav navbar-nav">
                                                    <li class="dropdown ">
                        <a href="#">Университет</a>
                        <ul class="dropdown-menu">
                                                                <li><a href="/sved-obr/">Сведения об образовательной организации</a></li>
                                                                <li><a href="/university/uchreditel-rgups-1224/">Учредитель</a></li>
                                                                <li><a href="/university/missiia-universiteta/">Миссия университета</a></li>
                                                                <li><a href="/university/osnovnye-svedeniia-1630/">Общая информация</a></li>
                                                                <li><a href="/university/universitet-segodnia-478/">Университет сегодня</a></li>
                                                                <li><a href="/university/struktura-i-organy-upravleniia-1632/">Структура</a></li>
                                                                <li><a href="/university/dokumenty/">Документы</a></li>
                                                                <li><a href="/university/vakansii-1528/">Вакансии</a></li>
                                                                <li><a href="/university/trudoustroistvo/">Трудоустройство</a></li>
                                                                <li><a href="/university/struktura-i-organy-upravleniia-1632/profsoiuz/">Профсоюз</a></li>
                                                                <li><a href="/university/istoriia-universiteta-rukovodi-131/">История</a></li>
                                                                <li><a href="/university/web-resursy-rgups-vysshie-uchebnye-157/">web-ресурсы</a></li>
                                                                <li><a href="/university/besprovodnaia-set-wifi-1078/">Беспроводная сеть (wifi)</a></li>
                                                                <li><a href="/university/virtual-nye-ekskursii-1092/">Виртуальный тур</a></li>
                                                                <li><a href="/university/struktura-i-organy-upravleniia-1632/strukturnye-podrazdeleniia/mezhdunarodnaia-deiatel-nost-576/">Международная деятельность</a></li>
                                                                <li><a href="/university/ekologicheskaia-politika/">Экологическая политика</a></li>
                                                                <li><a href="/university/kontaktnaia-informatciia-rgups-353/">Контактная информация</a></li>
                                                    </ul>
                    </li>
                                    <li class="dropdown ">
                        <a href="#">Образование</a>
                        <ul class="dropdown-menu">
                                                                <li><a href="/oop/aspirantura/">Аспирантура</a></li>
                                                                <li><a href="/oop/magistratura/">Магистратура</a></li>
                                                                <li><a href="/oop/spetcialitet/">Специалитет</a></li>
                                                                <li><a href="/oop/bakalavriat/">Бакалавриат</a></li>
                                                                <li><a href="/oop/spo/">Среднее профессиональное образование (СПО)</a></li>
                                                                <li><a href="/education/litcei/svedeniia-ob-obrazovatel-noi-organizatcii/obrazovanie/">Среднее общее образование (Лицей)</a></li>
                                                                <li><a href="/university/struktura-i-organy-upravleniia-1632/strukturnye-podrazdeleniia/tcentr-razvitiia-karery/otdel-dovuzovskoi-podgotovki/">Довузовская подготовка/подкурсы</a></li>
                                                                <li><a href="/university/struktura-i-organy-upravleniia-1632/strukturnye-podrazdeleniia/tcentr-razvitiia-karery/otdel-dopolnitel-noi-tcelevoi-podgotovki/">Целевая подготовка</a></li>
                                                                <li><a href="/education/dopolnitel-noe-professional-noe-obrazovanie/">Дополнительное профессиональное образование</a></li>
                                                                <li><a href="/education/voennoe-obuchenie/">Военное обучение</a></li>
                                                                <li><a href="/education/platnye-obrazovatel-nye-uslugi-1636/">Платные образовательные услуги</a></li>
                                                    </ul>
                    </li>
                                    <li class="dropdown ">
                        <a href="#">Наука</a>
                        <ul class="dropdown-menu">
                                                                <li><a href="/science/doktorantura-i-aspirantura-kon-1388/">Конференции</a></li>
                                                                <li><a href="/science/obshchaia-informatciia-nauchnoi-rabot-388/">Научно-исследовательская часть</a></li>
                                                                <li><a href="/science/ob-iavleniia-o-zashchite-dissertatci-1277/">Диссертации и диссертационные советы</a></li>
                                                                <li><a href="/science/granty-1763/">Научные гранты</a></li>
                                                                <li><a href="/science/napravleniia-i-rezul-taty-nauchnoi-deiatel-nosti/">Направления и результаты научной деятельности</a></li>
                                                                <li><a href="/science/baza-dlia-osushchestvleniia-nauchno-i-705/">База для осуществления научной деятельности</a></li>
                                                                <li><a href="/science/stat-i-patenty-svidetelstva/">Публикации статей, патенты, свидетельства</a></li>
                                                                <li><a href="/science/studencheskaia-nauka/">Студенческая наука</a></li>
                                                                <li><a href="/science/sovet-molodykh-uchenykh/">Совет молодых ученых</a></li>
                                                                <li><a href="/science/razrabotki-143/">Разработки</a></li>
                                                                <li><a href="/science/nauchnye-shkoly-144/">Научные школы</a></li>
                                                                <li><a href="/science/nauka-i-universitety/">Национальный проект Наука и университеты</a></li>
                                                                <li><a href="/science/izdaniia-v-rostovskom-gosudarst-362/">Издания</a></li>
                                                    </ul>
                    </li>
                                    <li class="dropdown ">
                        <a href="#">Студенческая жизнь</a>
                        <ul class="dropdown-menu">
                                                                <li><a href="/students/uchastie-rgups-v-mezhdunarodnom-k-1544/">Православная Инициатива</a></li>
                                                                <li><a href="/students/konkursy-proekty-975/">Конкурсы, проекты</a></li>
                                                                <li><a href="/students/dvoretc-kul-tury-767/">Дворец культуры</a></li>
                                                                <li><a href="/students/tcentry-pritiazheniia-profil-nye-k-1791/">Кружки и мастер-классы</a></li>
                                                                <li><a href="/students/sotcial-nye-seti/">Социальные сети</a></li>
                                                                <li><a href="/students/studencheskii-profkom/">Студенческий профком</a></li>
                                                    </ul>
                    </li>
                                    <li class="dropdown ">
                        <a href="#">Сервисы</a>
                        <ul class="dropdown-menu">
                                                                <li><a href="/services/time/">Расписание</a></li>
                                                                <li><a href="/services/progress/">Успеваемость (c 1-й сессии)</a></li>
                                                                <li><a href="/services/visits/">Посещаемость</a></li>
                                                                <li><a href="/services/test/">Результаты тестирования</a></li>
                                                                <li><a href="/services/corruption/">Противодействие коррупции</a></li>
                                                                <li><a href="/services/feedback/">Электронное обращение (жалобы, предложения и иное)</a></li>
                                                                <li><a href="http://portal.rgups.ru/index.php?r=site/registerexternaluser">Регистрация участников образовательного процесса</a></li>
                                                                <li><a href="http://portal.rgups.ru/">Электронная  информационно- образовательная среда</a></li>
                                                                <li><a href="/services/vypisat-kvitantciiu/">Сформировать квитанцию на оплату</a></li>
                                                                <li><a href="/services/vypuskniki-okonchivshie-riips-riizht-rgups-s-otlichiem/">Выпускники, окончившие РИИПС-РИИЖТ-РГУПС с отличием</a></li>
                                                                <li><a href="/services/spravochnik-ezhemesiachnykh-tarifov-oplaty-prozhivaniia-v-obshchezhitiiakh/">Справочник ежемесячных тарифов оплаты проживания в общежитиях</a></li>
                                                                <li><a href="/services/iuridicheskaia-klinika/">Юридическая клиника</a></li>
                                                                <li><a href="/services/elektronno-bibliotechnye-sistemy/">Электронно-библиотечные системы</a></li>
                                                                <li><a href="/services/chasto-zadavaemye-voprosy/">Часто задаваемые вопросы</a></li>
                                                                <li><a href="/services/poluchenie-konsul-tatcii-po-okazyvaemym-uslugam/">Получение консультации по оказываемым услугам</a></li>
                                                                <li><a href="https://forms.yandex.ru/cloud/647cfa0a068ff056c36f6082/">Анкета удовлетворенности качеством услуг</a></li>
                                                    </ul>
                    </li>
                                    <li class="dropdown ">
                        <a href="#">Медиа</a>
                        <ul class="dropdown-menu">
                                                                <li><a href="/media/ob-ektiv-vremeni/">В объективе времени</a></li>
                                                                <li><a href="/media/smi-rgups-1652/">СМИ РГУПС</a></li>
                                                                <li><a href="/media/gazeta-magistral-981/">&quot;Магистраль&quot;</a></li>
                                                    </ul>
                    </li>
                                                </ul>
                        </nav>
                                        </div>
        </div>
        <header class="page-header container">

                <!-- New-Year theme -->
                                                <!-- end New-Year theme -->

                <div class="page-header__content row">

                        <!-- langs -->
                        <div class="languages col-sm-1 col-sm-push-11 col-xs-12">
                                                <a class="languages__language" href="/en/" title="EN">
                        <img src="/site/templates/design/images/langs__en.jpg" alt="Английская версия">en</a>

                        </div>
                        <!-- /end.langs -->

                        <!-- logo -->
                        <div class="header-logo col-lg-5 col-sm-7 col-sm-pull-1 col-xs-12">
                                <a class="header-logo__logo-img" href="/" title="На главную"><img src="/site/templates/design/images/logo2.png"></a>
                                <a class="header-logo__logo-caption" href="/" title="На главную">Ростовский государственный<br/>университет путей сообщения</a>
                        </div>
                        <!-- /end.logo -->

                        <!-- contact -->
                        <div class="header-contact col-lg-2 visible-lg-block col-sm-pull-1">
                                <a href="/university/kontaktnaia-informatciia-rgups-353/">Контакты</a>
                                <div class="header-contact-phone"><span>8 (800)</span> 707-19-29</div>
                                <div class="header-contact-phone"><span>8 (863)</span> 255-32-83</div>
                                <!--a href="#">Схема проезда</a-->
                        </div>
                        <!-- /end.contact -->

                        <!-- search form -->
                        <div class="header-search col-sm-4 col-sm-pull-1 col-xs-12">
                                <form class="search-form" action="/search/" method="GET">
                                        <input class="search-form__text" type="text" name="q" placeholder="поиск">
                                        <input class="search-form__button" type="submit" value="">
                                </form>
                                                                        <a href="?special=1" class="special-version underline" itemprop="Copy">Версия для слабовидящих</a>
                                                        </div>
                        <!-- /end.search form -->

                </div>
        </header>


        <!-- <div class="vuzonline-banner container">
                <a href="https://www.gosuslugi.ru/vuzonline" target="_blank">
                        <img src="/site/assets/files/140583/vuzonline.jpg" alt="">
                </a>
        </div> -->

        <div class="content container">

                <!-- main content -->
                <article class="content__main">

                        <!-- side-menu -->
                        <ul class="side-menu">
                                <li>
                                        <a href="/abitur/">
                                                <figure>
                                                        <figcaption>Поступающим</figcaption>
                                                        <img src="/site/templates/design/images/menu/enrollee.jpg" alt="">
                                                </figure>
                                        </a>
                                </li>
                                <li>
                                        <a href="/content-pages/studentam-1641/">
                                                <figure>
                                                        <figcaption>Студентам</figcaption>
                                                        <img src="/site/templates/design/images/menu/students.jpg" alt="">
                                                </figure>
                                        </a>
                                </li>
                                <li>
                                        <a href="/content-pages/aspirantura-2016-1901/">
                                                <figure>
                                                        <figcaption>Аспирантам</figcaption>
                                                        <img src="/site/templates/design/images/menu/graduate.jpg" alt="">
                                                </figure>
                                        </a>
                                </li>
                                <li>
                                        <a href="/content-pages/prepodavateliam-i-sotrudnikam-1643/">
                                                <figure>
                                                        <figcaption>Сотрудникам</figcaption>
                                                        <img src="/site/templates/design/images/menu/employee.jpg" alt="">
                                                </figure>
                                        </a>
                                </li>
                                <li>
                                        <a href="/content-pages/shkol-nikam/">
                                                <figure>
                                                        <figcaption>Школьникам</figcaption>
                                                        <img src="/site/templates/design/images/menu/schoolchild.jpg" alt="">
                                                </figure>
                                        </a>
                                </li>
                                <li>
                                        <a href="/content-pages/vypusknikam-1642/">
                                                <figure>
                                                        <figcaption>Выпускникам</figcaption>
                                                        <img src="/site/templates/design/images/menu/alumni.jpg" alt="">
                                                </figure>
                                        </a>
                                </li>
                                <li>
                                        <a href="/content-pages/roditeliam/">
                                                <figure>
                                                        <figcaption>Родителям</figcaption>
                                                        <img src="/site/templates/design/images/menu/parents.jpg" alt="">
                                                </figure>
                                        </a>
                                </li>
                                <li>
                                        <a href="/content-pages/rabotodateliam/">
                                                <figure>
                                                        <figcaption>Работодателям</figcaption>
                                                        <img src="/site/templates/design/images/menu/employer.jpg" alt="">
                                                </figure>
                                        </a>
                                </li>
                        </ul>
                        <!-- /end.side-menu -->


                        <!-- slider -->
                        <div class="slider">
                                <!-- slides -->
                                <ul>
                                                                               <li>
                                                                               <img src='/site/assets/files/78257/rgups-s.jpg'>
                                                                               </li>
                                                                               <li>
                                                                               <img src='/site/assets/files/106553/slides-raspredelenie-3.jpg'>
                                                                               </li>
                                                                               <li>
                                                                               <img src='/site/assets/files/110686/slides-raspredelenie-3.jpg'>
                                                                               </li>
                                                                               <li>
                                                                               <img src='/site/assets/files/78263/slides-freshman-1.jpg'>
                                                                               </li>
                                                                               <li>
                                                                               <img src='/site/assets/files/91410/slides-stroiotryad-2.jpg'>
                                                                               </li>
                                                                               <li>
                                                                               <img src='/site/assets/files/89828/slides-alumni.jpg'>
                                                                               </li>
                                                                               <li>
                                                                               <img src='/site/assets/files/126817/slides-rate-1.jpg'>
                                                                               </li>
                                                                               </ul>
                                <!-- controls -->
                                <a class="slide-prev" href="#"></a>
                                <a class="slide-next" href="#"></a>
                        </div>
                        <!-- /end.slider -->


                </article>
                <!-- /end.content__main -->

                <!-- sidebar -->
                <aside class="content__sidebar">

                        <!-- graphic-links -->
                        <div class="graphic-links">
                                <a class="graphic-link" href="/services/dlia-predlozhenii-i-zhalob/">
                                        <img src="/site/templates/design/images/side-feedback.png" alt="">
                                </a>
<!--                            <a class="graphic-link" href="/content-pages/den-otkrytykh-dverei-v-rgups-online/">
                                        <img src="/site/templates/design/images/side-dod.jpg" alt="">
                                </a> -->

<!--                            <a class="graphic-link" href="/news/onlain-priemnaia-rgups/">
                    <img src="/site/templates/design/images/side-dod3.jpg" alt="">
                </a>  -->

                                <a class="graphic-link" href="/news/">
                                        <span class="graphic-link__img"><img src="/site/templates/design/images/sb.jpg" alt=""></span>
                                        <strong class="graphic-link__caption">Новости</strong>
                                </a>
                                <a class="graphic-link" href="http://www.tour.rgups.ru/start">
                                        <span class="graphic-link__img"><img src="/site/templates/design/images/vtour_sb.jpg" alt=""></span>
                                        <strong class="graphic-link__caption">Виртуальный тур</strong>
                                </a>
                                <!--<a class="graphic-link" href="https://test.rgups.ru/opendoors" target="_blank">
                                        <img src="/site/templates/design/images/side-dod4.jpg" alt="">
                                </a> -->


                        </div>
                        <!-- /end.graphic-links -->

                        <!-- sidebar-tags -->
                        <ul class="tags">

                                <li><a href="/sved-obr/">Сведения<br>об образовательной организации</a></li>
                            <li><a href="http://portal.rgups.ru/">Электронная <br /> информационно-<br>образовательная<br>среда</a></li>
                                <li><a href="/services/raspisanie/">Расписание</a></li>
                                <li><a href="/services/uspevaemost/">Успеваемость</a></li>
                                <li><a href="/services/poseshchaemost/">Поcещаемость</a></li>
                        </ul>
                        <!-- /end.sidebar-tags -->
                </aside>
                <!-- /end.sidebar -->

        </div>

        <div class="homenews container">
                <div class="row">

                    <div class="news-item news-item_important">
                                        <div class="thumbnail">
                                                        <time class="news-item__time">08.11.2021</time>
                            <div class="caption">
                                                                <p>Информация для студентов очной формы обучения, оформляющих документы на социальную стипендию на период с 08 ноября 2021 года.</p>
                                <p><a href="/news/informatciia-dlia-studentov-ochnoi-formy-obucheniia-oformliaiushchikh-dokumenty-na-sotcial-nuiu-stipendiiu/" class="btn btn-primary" role="button">Подробнее</a></p>
                            </div>
                        </div>
                    </div>

                    <div class="news-item">
                                        <div class="thumbnail">
                                                        <a href="/news/rgups-uchastnik-xiv-festivalia-nauki-iuga-rossii/"><img src="/site/assets/files/199364/6.253x0.png" alt="Новость"></a>                             <time class="news-item__time">19.09.2023</time>
                            <div class="caption">
                                                                <p>РГУПС участник  XIV Фестиваля науки Юга России</p>
                                <p><a href="/news/rgups-uchastnik-xiv-festivalia-nauki-iuga-rossii/" class="btn btn-primary" role="button">Подробнее</a></p>
                            </div>
                        </div>
                    </div>

                    <div class="news-item">
                                        <div class="thumbnail">
                                                        <a href="/news/tcifrovaia-olimpiada-volga-it2023/"><img src="/site/assets/files/199365/group-258.253x0.png" alt="Новость"></a>                             <time class="news-item__time">19.09.2023</time>
                            <div class="caption">
                                                                <p>Цифровая олимпиада «Волга-IT’2023»</p>
                                <p><a href="/news/tcifrovaia-olimpiada-volga-it2023/" class="btn btn-primary" role="button">Подробнее</a></p>
                            </div>
                        </div>
                    </div>

                    <div class="news-item">
                                        <div class="thumbnail">
                                                        <a href="/news/boitcy-studencheskikh-otriadov-rgups-stali-uchastnikami-vserossiiskoi-mediashkoly-mooo-rso-v-g-sankt-peterburg/"><img src="/site/assets/files/199366/ijjb7bkrhq0.253x0.jpg" alt="Новость"></a>                             <time class="news-item__time">19.09.2023</time>
                            <div class="caption">
                                                                <p>Бойцы студенческих отрядов РГУПС стали участниками Всероссийской медиашколы МООО «РСО» в г. Санкт-Петербург</p>
                                <p><a href="/news/boitcy-studencheskikh-otriadov-rgups-stali-uchastnikami-vserossiiskoi-mediashkoly-mooo-rso-v-g-sankt-peterburg/" class="btn btn-primary" role="button">Подробнее</a></p>
                            </div>
                        </div>
                    </div>

                    <div class="news-item">
                                        <div class="thumbnail">
                                                        <a href="/news/19-noiabria-v-rgups-sostoitsia-napisanie-geograficheskogo-diktanta/"><img src="/site/assets/files/199367/photo.253x0.jpg" alt="Новость"></a>                             <time class="news-item__time">19.09.2023</time>
                            <div class="caption">
                                                                <p>19 ноября в РГУПС состоится написание  Географического  диктанта</p>
                                <p><a href="/news/19-noiabria-v-rgups-sostoitsia-napisanie-geograficheskogo-diktanta/" class="btn btn-primary" role="button">Подробнее</a></p>
                            </div>
                        </div>
                    </div>

                    <div class="news-item">
                                        <div class="thumbnail">
                                                        <a href="/news/prezentatcionnyi-kontcert-territoriia-tvorchestva-21-sentiabria-v-17.30-dvoretc-kul-tury-rgups/"><img src="/site/assets/files/199252/dlia_vk.253x0.jpg" alt="Новость"></a>                             <time class="news-item__time">18.09.2023</time>
                            <div class="caption">
                                                                <p>Презентационный концерт "Территория творчества" 21 сентября в 17.30, Дворец культуры РГУПС</p>
                                <p><a href="/news/prezentatcionnyi-kontcert-territoriia-tvorchestva-21-sentiabria-v-17.30-dvoretc-kul-tury-rgups/" class="btn btn-primary" role="button">Подробнее</a></p>
                            </div>
                        </div>
                    </div>

                    <div class="news-item">
                                        <div class="thumbnail">
                                                        <a href="/news/rgups-prinial-uchastie-v-shkole-peredovogo-opyta-po-organizatcii-innovatcionnoi-deiatel-nosti-kompanii-oao-rzhd/"><img src="/site/assets/files/199253/50jphsf7quo8swwskg4gs8sg40wo0g.253x0.png" alt="Новость"></a>                             <time class="news-item__time">18.09.2023</time>
                            <div class="caption">
                                                                <p>РГУПС принял участие  в Школе передового опыта по организации инновационной деятельности  компании ОАО «РЖД»</p>
                                <p><a href="/news/rgups-prinial-uchastie-v-shkole-peredovogo-opyta-po-organizatcii-innovatcionnoi-deiatel-nosti-kompanii-oao-rzhd/" class="btn btn-primary" role="button">Подробнее</a></p>
                            </div>
                        </div>
                    </div>

                    <div class="news-item">
                                        <div class="thumbnail">
                                                        <a href="/news/v-rgups-sostoialas-vstrecha-pervokursnikov-i-nastavnikov-s-predstaviteliami-studencheskikh-vneuchebnykh-ob-edinenii-rgups-1/"><img src="/site/assets/files/199363/dsc_9012.253x0.jpg" alt="Новость"></a>                             <time class="news-item__time">18.09.2023</time>
                            <div class="caption">
                                                                <p>В РГУПС состоялась встреча первокурсников и наставников с представителями студенческих внеучебных объединений «РГУПС внеучебный»</p>
                                <p><a href="/news/v-rgups-sostoialas-vstrecha-pervokursnikov-i-nastavnikov-s-predstaviteliami-studencheskikh-vneuchebnykh-ob-edinenii-rgups-1/" class="btn btn-primary" role="button">Подробнее</a></p>
                            </div>
                        </div>
                    </div>

                    <div class="news-item">
                                        <div class="thumbnail">
                                                        <a href="/news/startoval-priem-rabot-na-mezhdunarodnyi-molodezhnyi-konkurs-nauchnykh-i-nauchno-fantasticheskikh-rabot-gorizont-2100/"><img src="/site/assets/files/199149/konkurs_gorizont_2100.253x0.jpg" alt="Новость"></a>                             <time class="news-item__time">15.09.2023</time>
                            <div class="caption">
                                                                <p>Стартовал прием работ на Международный молодёжный конкурс научных и научно-фантастических работ «Горизонт 2100»</p>
                                <p><a href="/news/startoval-priem-rabot-na-mezhdunarodnyi-molodezhnyi-konkurs-nauchnykh-i-nauchno-fantasticheskikh-rabot-gorizont-2100/" class="btn btn-primary" role="button">Подробнее</a></p>
                            </div>
                        </div>
                    </div>

                    <div class="news-item">
                                        <div class="thumbnail">
                                                        <a href="/news/stan-ambassadorom-oao-rzhd/"><img src="/site/assets/files/198950/3vkxqszobbo.253x0.jpg" alt="Новость"></a>                             <time class="news-item__time">14.09.2023</time>
                            <div class="caption">
                                                                <p>Стань амбассадором ОАО «РЖД»</p>
                                <p><a href="/news/stan-ambassadorom-oao-rzhd/" class="btn btn-primary" role="button">Подробнее</a></p>
                            </div>
                        </div>
                    </div>

                    <div class="news-item">
                                        <div class="thumbnail">
                                                        <a href="/news/interaktivnaia-platforma-agregator-dobrykh-del/"><img src="/site/assets/files/198951/jmnhrrunim0.253x0.jpg" alt="Новость"></a>                             <time class="news-item__time">14.09.2023</time>
                            <div class="caption">
                                                                <p>Интерактивная платформа «Агрегатор добрых дел»</p>
                                <p><a href="/news/interaktivnaia-platforma-agregator-dobrykh-del/" class="btn btn-primary" role="button">Подробнее</a></p>
                            </div>
                        </div>
                    </div>

                    <div class="news-item">
                                        <div class="thumbnail">
                                                        <a href="/news/molodezh-za-soiuznoe-gosudarstvo-ansambl-uspekh-prinial-uchastie-v-mezhdunarodnom-festivale/"><img src="/site/assets/files/198735/w-6ckwekpb4.253x0.jpg" alt="Новость"></a>                             <time class="news-item__time">13.09.2023</time>
                            <div class="caption">
                                                                <p>Молодежь – за Союзное государство: ансамбль «Успех» принял участие в международном фестивале</p>
                                <p><a href="/news/molodezh-za-soiuznoe-gosudarstvo-ansambl-uspekh-prinial-uchastie-v-mezhdunarodnom-festivale/" class="btn btn-primary" role="button">Подробнее</a></p>
                            </div>
                        </div>
                    </div>

                                </div>
        </div>

        <!-- events -->
        <div class="home-events container">
                <aside class="events-list">

                                <a class="event" href="abitur/" target="_blank">
                                        <figure>
                                                <img src='/site/assets/files/81111/1.jpg' alt="Абитуриенту РГУПС">
                                                <figcaption>Абитуриенту РГУПС</figcaption>
                                        </figure>
                                </a>

                                <a class="event" href="https://minobrnauki.gov.ru/press-center/news/?ELEMENT_ID=50667" target="_blank">
                                        <figure>
                                                <img src='/site/assets/files/145612/315kh150_sinii_.jpg' alt="">
                                                <figcaption></figcaption>
                                        </figure>
                                </a>

                                <a class="event" href="/science/nauka-i-universitety/" target="_blank">
                                        <figure>
                                                <img src='/site/assets/files/161091/nauka_i_universitety_3.png' alt="">
                                                <figcaption></figcaption>
                                        </figure>
                                </a>

                                <a class="event" href="https://lib.rgups.ru/" target="_blank">
                                        <figure>
                                                <img src='/site/assets/files/127019/ntb_banner.png' alt="">
                                                <figcaption></figcaption>
                                        </figure>
                                </a>

                                <a class="event" href="http://iiti.rgups.ru" target="_blank">
                                        <figure>
                                                <img src='/site/assets/files/156263/iiti2023.jpg' alt="">
                                                <figcaption></figcaption>
                                        </figure>
                                </a>

                                <a class="event" href="https://dlearn.rgups.ru" target="_blank">
                                        <figure>
                                                <img src='/site/assets/files/198517/elektronnye_obrazovatel_nye_resursyv2.png' alt="">
                                                <figcaption></figcaption>
                                        </figure>
                                </a>

                                <a class="event" href="/education/litcei/" target="_blank">
                                        <figure>
                                                <img src='/site/assets/files/81120/licey.jpg' alt="">
                                                <figcaption></figcaption>
                                        </figure>
                                </a>

                                <a class="event" href="/rtgt" target="_blank">
                                        <figure>
                                                <img src='/site/assets/files/108508/technikum.jpg' alt="">
                                                <figcaption></figcaption>
                                        </figure>
                                </a>

                                <a class="event" href="/abitur/spo/spetcial-nosti-po-kotorym-osushchestvliaetsia-priem-v-ramkakh-fp-professionalitet/" target="_blank">
                                        <figure>
                                                <img src='/site/assets/files/152579/professionalitet_obshchii.jpg' alt="">
                                                <figcaption></figcaption>
                                        </figure>
                                </a>

                                <a class="event" href="https://upkpp.rgups.ru/" target="_blank">
                                        <figure>
                                                <img src='/site/assets/files/168330/2_banner.png' alt="">
                                                <figcaption></figcaption>
                                        </figure>
                                </a>

                                <a class="event" href="http://pobeda.onf.ru" target="_blank">
                                        <figure>
                                                <img src='/site/assets/files/154296/veb-banner_300_x_250-1.png' alt="">
                                                <figcaption></figcaption>
                                        </figure>
                                </a>

                                <a class="event" href="/services/soobshchit-o-korruptcii/" target="_blank">
                                        <figure>
                                                <img src='/site/assets/files/81116/corruption.gif' alt="">
                                                <figcaption></figcaption>
                                        </figure>
                                </a>

                                <a class="event" href="https://map.ncpti.ru/" target="_blank">
                                        <figure>
                                                <img src='/site/assets/files/81119/map_ncpti_banner.png' alt="">
                                                <figcaption></figcaption>
                                        </figure>
                                </a>

                                <a class="event" href="/content-pages/oao-rzhd-vakansii-2020/" target="_blank">
                                        <figure>
                                                <img src='/site/assets/files/123129/dvas2.gif' alt="">
                                                <figcaption></figcaption>
                                        </figure>
                                </a>

                                <a class="event" href="https://team.rzd.ru/career/vacancies/place/rostov-na-donu" target="_blank">
                                        <figure>
                                                <img src='/site/assets/files/160994/01112022.png' alt="">
                                                <figcaption></figcaption>
                                        </figure>
                                </a>

                                <a class="event" href="/content-pages/75-let-pobedy/" target="_blank">
                                        <figure>
                                                <img src='/site/assets/files/120779/s_dnem_pobedy_1.jpg' alt="">
                                                <figcaption></figcaption>
                                        </figure>
                                </a>

                                <a class="event" href="/content-pages/nauchnyi-polk/" target="_blank">
                                        <figure>
                                                <img src='/site/assets/files/143093/vserossiiskaia_aktciia_nauchnyi_polk_200.jpg' alt="">
                                                <figcaption></figcaption>
                                        </figure>
                                </a>

                                <a class="event" href="https://edu.gov.ru/" target="_blank">
                                        <figure>
                                                <img src='/site/assets/files/109269/ministerstvo_prosveshcheniia_2.png' alt="Министерство просвещения">
                                                <figcaption>Министерство просвещения</figcaption>
                                        </figure>
                                </a>

                                <a class="event" href="https://minobrnauki.gov.ru/" target="_blank">
                                        <figure>
                                                <img src='/site/assets/files/109366/mnvo.png' alt="Министерство образования и науки">
                                                <figcaption>Министерство образования и науки</figcaption>
                                        </figure>
                                </a>

                                <a class="event" href="/services/iuridicheskaia-klinika/" target="_blank">
                                        <figure>
                                                <img src='/site/assets/files/109368/law.jpg' alt="">
                                                <figcaption></figcaption>
                                        </figure>
                                </a>

                                <a class="event" href="/site/assets/files/110210/pamyatka_sberbank-1.pdf" target="_blank">
                                        <figure>
                                                <img src='/site/assets/files/110210/sber-1.jpg' alt="Памятка о способах оплаты">
                                                <figcaption>Памятка о способах оплаты</figcaption>
                                        </figure>
                                </a>

                                <a class="event" href="/university/dokumenty/antiterror/" target="_blank">
                                        <figure>
                                                <img src='/site/assets/files/118913/stop-terror.jpg' alt="">
                                                <figcaption></figcaption>
                                        </figure>
                                </a>

                                <a class="event" href="/content-pages/prepodavateliam-i-sotrudnikam-1643/starshee-pokolenie/" target="_blank">
                                        <figure>
                                                <img src='/site/assets/files/119931/bnr.png' alt="">
                                                <figcaption></figcaption>
                                        </figure>
                                </a>

                                <a class="event" href="/news/itogi-pervogo-etapa-vtorogo-tura-olimpiady-diplomnykh-proektov/" target="_blank">
                                        <figure>
                                                <img src='/site/assets/files/137161/olimpiada_dp-1.png' alt="">
                                                <figcaption></figcaption>
                                        </figure>
                                </a>

                                <a class="event" href="/news/tretii-sezon-proekta-tvoi-khod-nachinaetsia-priamo-seichas/" target="_blank">
                                        <figure>
                                                <img src='/site/assets/files/127043/tvoi_khod.jpg' alt="">
                                                <figcaption></figcaption>
                                        </figure>
                                </a>

                                <a class="event" href="http://Объясняем.рф" target="_blank">
                                        <figure>
                                                <img src='/site/assets/files/139523/180x150.png' alt="">
                                                <figcaption></figcaption>
                                        </figure>
                                </a>

                                <a class="event" href="https://history.mintrans.ru/" target="_blank">
                                        <figure>
                                                <img src='/site/assets/files/118983/bezimeni-2.jpg' alt="">
                                                <figcaption></figcaption>
                                        </figure>
                                </a>

                                <a class="event" href="/content-pages/ia-professional/" target="_blank">
                                        <figure>
                                                <img src='/site/assets/files/169280/whatsapp_image_2023-03-01_at_11.05.46.jpeg' alt="">
                                                <figcaption></figcaption>
                                        </figure>
                                </a>

                                <a class="event" href="/site/assets/files/196410/prilozhenie_kreditovanie_spo.pdf" target="_blank">
                                        <figure>
                                                <img src='/site/assets/files/169334/banner-1.png' alt="">
                                                <figcaption></figcaption>
                                        </figure>
                                </a>

                                <a class="event" href="/content-pages/sberbank-obrazovatel-nyi-kredit" target="_blank">
                                        <figure>
                                                <img src='/site/assets/files/167684/sber.png' alt="">
                                                <figcaption></figcaption>
                                        </figure>
                                </a>

                                <a class="event" href="/content-pages/o-profilakticheskikh-meropriiatiiakh-ostroinfektcionnykh-virusnykh-zabolevanii/" target="_blank">
                                        <figure>
                                                <img src='/site/assets/files/132303/covus.jpg' alt="">
                                                <figcaption></figcaption>
                                        </figure>
                                </a>

                </aside>
        </div>
        <!-- /end.events -->


        <footer class="page-footer">
                <div class="page-footer__content container row">
                        <div class="column-left col-sm-6 col-xs-12">
                                <a class="footer-logo" href="/" title="На главную">
                                        <img class="footer-logo__img" src="/site/templates/design/images/footer-logo.png" alt="РГУПС">
                                        <p class="footer-logo__caption">
                                                <span class="footer-logo__ru">Ростовский Государственный<br>Университет Путей Сообщения</span>
                                                <br>
                                                <span class="footer-logo__en">Rostov State Transport University</span>
                                        </p>
                                </a>
                                <div class="copyright">
                                                                        <p>
                                                <a href="/sved-obr/">Сведения об образовательной организации</a>
                                        </p>
                                        <p>
                                                <a href="/university/kontaktnaia-informatciia-rgups-353/rekvizity-dlia-zakliucheniia-dogovorov/">Реквизиты</a>
                                        </p>
                                        <p>
                                                Электронная почта университета:
                                                <a href="mailto:up_del@rgups.ru">up_del@rgups.ru</a>
                                        </p>
                                        <p>
                                                Приемная комиссия:
                                                <a href="mailto:prkom@rgups.ru">prkom@rgups.ru</a>
                                        </p>
                                        <p>
                                                Отдел по связям с общественностью (пресс-служба):
                                                <a href="mailto:press_centr@rgups.ru">press_centr@rgups.ru</a>
                                        </p>
                                                                               <p>
                                                По вопросам работы сайта:      <a href="mailto:www@rgups.ru">www@rgups.ru</a>
                                        </p>
                                </div>
                        </div>
                        <div class="column-right col-sm-6 col-xs-12">
                                <div class="footer-contacts">
                                        <address class="footer-contacts__item">
                                                <small class="footer-contacts__title">Адрес:</small><br>
                                                пл. Ростовского Стрелкового Полка Народного Ополчения, д. 2,<br>
                                                г. Ростов-на-Дону, 344038
                                        </address>
                                        <div class="footer-contacts__item">
                                                <small class="footer-contacts__title">Телефон/факс:</small><br>
                                                (863) <strong>255-32-83</strong>
                                        </div>
                                        <div class="footer-contacts__item">
                                                <small class="footer-contacts__title">Телефон приемной комиссии:</small><br>
                                                <strong>8 800 707-19-29</strong><br>
                                                (863) <strong>255-31-61</strong>
                                        </div>
                                </div>
                                <div class="soc-seti">
                                        <a title="Официальная группа РГУПС" target="_blank" href="https://vk.com/rgupsofficial">
                                                <img src="/site/templates/design/images/vkk-btn.png" alt="RGUPSVK">
                                        </a>
                                        <a title="Официальная группа РГУПС" target="_blank" href="https://ok.ru/rgupsofficial">
                                                <img src="/site/templates/design/images/odn-btn.png" alt="Odnoklassniki">
                                        </a>
                                        <a title="Официальный канал РГУПС" target="_blank" href="https://rutube.ru/channel/25031231/">
                                                <img src="/site/templates/design/images/r-btn.png" alt="Rutube">
                                        </a>
100 47792    0 47792    0     0  39537      0 --:--:--  0:00:01 --:--:-- 39793циальный канал РГУПС" target="_blank" href="https://t.me/RGUPSofficial">
                                                <img src="/site/templates/design/images/tg-btn.png" alt="Telegram">
                                        </a>
                                        <a title="RSS" target="_blank" href="/rss/">
                                                <img src="/site/templates/design/images/rss-btn.png" alt="RSS">
                                        </a>
                                </div>
                                <div class="copyright">
                                        <p>
                                                Разработка и поддержка –
                                                <a href="http://rgups.ru/content-pages/upravlenie-informatizatcii-ui-1547/">УИ РГУПС</a>
                                        </p>
                                </div>
                        </div>
                </div>
        </footer>

        <script src="/site/templates/design/js/jquery-1.12.3.min.js"></script>
        <script src="/site/templates/design/js/libs/jquery-ui.min.js"></script>
        <script src="/site/templates/design/js/bootstrap.min.js"></script>
        <script src="/site/templates/design/js/jquery.jcarousel.min.js"></script>
        <script src="/site/templates/design/js/masonry.min.js"></script>
    <script src="/site/templates/design/js/libs/flexmenu.js"></script>
    <script src="/site/templates/design/js/libs/jquery.stickytableheaders.min.js"></script>
    <script src="/site/templates/design/js/libs/jquery.tablesorter.min.js"></script>
        <script src="/site/templates/design/js/scripts.js?v=1"></script>
        <script src="/site/templates/design/js/plugins/schedule.js"></script>
        <script src="/site/templates/design/js/plugins/visits.js"></script>
        <script src="/site/templates/design/js/plugins/progress.js"></script>





        <script src="/site/templates/design/js/plugins/test_result.js"></script>
        <script src="/site/templates/design/js/plugins/alumni.js"></script>
    <script src="/site/templates/design/js/libs/fancybox.min.js"></script>



    <!-- Counters -->
    <!-- <script>
          (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
          (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
          m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
          })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

          ga('create', 'UA-6818511-1', 'auto');
          ga('send', 'pageview');
        </script>
--><script type="text/javascript" >
   (function(m,e,t,r,i,k,a){m[i]=m[i]||function(){(m[i].a=m[i].a||[]).push(arguments)};
   m[i].l=1*new Date();k=e.createElement(t),a=e.getElementsByTagName(t)[0],k.async=1,k.src=r,a.parentNode.insertBefore(k,a)})
   (window, document, "script", "https://mc.yandex.ru/metrika/tag.js", "ym");

   ym(21318811, "init", {
        clickmap:true,
        trackLinks:true,
        accurateTrackBounce:true
   });
</script>
<noscript><div><img src="https://mc.yandex.ru/watch/21318811" style="position:absolute; left:-9999px;" alt="" /></div></noscript>
</body>
</html>
```
## ответы короче 
```
Admin@MSI MINGW64 ~
$ curl rgups.ru
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   169  100   169    0     0    964      0 --:--:-- --:--:-- --:--:--  1011
<html>
<head><title>301 Moved Permanently</title></head>
<body>
<center><h1>301 Moved Permanently</h1></center>
<hr><center>nginx/1.19.1</center>
</body>
</html>

Admin@MSI MINGW64 ~
$ curl www.rgups.ru
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   169  100   169    0     0   1200      0 --:--:-- --:--:-- --:--:--  1270
<html>
<head><title>301 Moved Permanently</title></head>
<body>
<center><h1>301 Moved Permanently</h1></center>
<hr><center>nginx/1.19.1</center>
</body>
</html>

Admin@MSI MINGW64 ~
$ curl http://www.rgups.ru
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   169  100   169    0     0   1221      0 --:--:-- --:--:-- --:--:--  1300
<html>
<head><title>301 Moved Permanently</title></head>
<body>
<center><h1>301 Moved Permanently</h1></center>
<hr><center>nginx/1.19.1</center>
</body>
</html>
```
## только заголовки
```
Admin@MSI MINGW64 ~
$ curl -I rgups.ru | grep -iE "x-some-header|other-header" 
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0   169    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
```
## запрос с -I -s rgups.ru
```
Admin@MSI MINGW64 ~
$ curl -I -s rgups.ru
HTTP/1.1 301 Moved Permanently #код ответа и его значение
Server: nginx/1.19.1 #сервер
Date: Wed, 20 Sep 2023 04:48:20 GMT  #текущая дата по время запроса
Content-Type: text/html #вывод информации о формате данных
Content-Length: 169 #Заголовок с информацией о длине контента в символах.
Connection: keep-alive #определяет, остаётся ли сетевое соединение активным после завершения текущей транзакции (запроса)
Location: https://rgups.ru/ #заголовок ответа, который используется при 2 обстоятельствах, чтобы попросить браузер перенаправить URL или предоставить информацию о местоположении вновь созданного ресурса
```
## запрос с -I -s www.rgups.com. как мы видим ответы отличаются, например во 2 случае есть X-Powered-By, X-Redirect-By и тд
```
Admin@MSI MINGW64 ~
$ curl -I -s www.rgups.com
HTTP/1.1 301 Moved Permanently #код ответа и его значение
Date: Wed, 20 Sep 2023 04:51:12 GMT #текущая дата по время запроса
Server: Apache  #сервер
X-Powered-By: PHP/7.3.33 #обычно он указывает платформу приложений, на которой работает сервер
X-Redirect-By: WordPress # и указывает перенаправления
Upgrade: h2,h2c #может использоваться для обновления уже установленного клиент-серверного соединения с другим протоколом (по тому же транспортному протоколу).
Connection: Upgrade #как мы видим при использовании www.rgups.com и rgups.ru ответы Connection различаются
Location: https://rgups.com/
Content-Type: text/html; charset=UTF-8
```
## код ответа и его значение
```
Admin@MSI MINGW64 ~
$ curl -I -s www.rgups.com | head -n 1 
HTTP/1.1 301 Moved Permanently
```
## протокол по которому осуществляется запрос
```
Admin@MSI MINGW64 ~ 
$ curl -I -s www.rgups.com | awk 'NR==1{print $2}'
301
```
## сравнение
не на все запросы можно получить нужный ответ
например здесь получен 1 вывод location от сайта ргупс, но не получен от сайта экзампл
а выводы pragma отсутвуют у обоих сайтов ргупс и экзампл
```
Admin@MSI MINGW64 ~
$ curl -I -s www.rgups.com | grep -i "Location"
Location: https://rgups.com/
Admin@MSI MINGW64 ~
$ curl -I -s www.rgups.com | grep -i "Pragma"
Admin@MSI MINGW64 ~
$ curl -I -s www.example.com | grep -i "Pragma"
Admin@MSI MINGW64 ~
$ curl -I -s www.example.com | grep -i "Location"  
```
вы не поверите, но для других последующих сайтов запросы и опции curl 
обозначают то же самое что и для rgups и example
## github.com
```
Admin@MSI MINGW64 ~
$ curl github.com
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0

Admin@MSI MINGW64 ~
$ curl https://github.com
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
<!DOCTYPE html>
<html lang="en"   data-a11y-animated-images="system" data-a11y-link-underlines="false">
  <head>
    <meta charset="utf-8">
  <link rel="dns-prefetch" href="https://github.githubassets.com">
  <link rel="dns-prefetch" href="https://avatars.githubusercontent.com">
  <link rel="dns-prefetch" href="https://github-cloud.s3.amazonaws.com">
  <link rel="dns-prefetch" href="https://user-images.githubusercontent.com/">
  <link rel="preconnect" href="https://github.githubassets.com" crossorigin>
#нереально длинный вырезанныйответ с http
</html>

Admin@MSI MINGW64 ~
$ curl http://github.com
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0

Admin@MSI MINGW64 ~
$ curl www.github.com
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
```
## запрос curl -I -s
как мы видим тут выводится меньшее кол-во данных, только код ответа, длина и ссылка на сайт
```
Admin@MSI MINGW64 ~
$ curl -I -s www.github.com
HTTP/1.1 301 Moved Permanently
Content-Length: 0
Location: https://www.github.com/ 
```
## вывод заголовков, порта и протокола
```
Admin@MSI MINGW64 ~
$ curl -I https://www.github.com | grep -iE "x-some-header|other-header" #заголовки
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
Admin@MSI MINGW64 ~ #протокол по которому осуществляется запрос
$ curl -I https://github.com | awk 'NR==1{print $2}'
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
200
Admin@MSI MINGW64 ~  #вывод номера порта
$ curl -I -w "%{remote_port}\n" github.com
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0HTTP/1.1 301 Moved Permanently
Content-Length: 0
Location: https://github.com/

80
```
## с подобными запросами нужный ответ не приходит :(
`$ curl -I -s www.github.com | grep -i "Data" `
## ржд
все ответы короткие
```
Admin@MSI MINGW64 ~
$ curl https://www.rzd.ru
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   109  100   109    0     0    226      0 --:--:-- --:--:-- --:--:--   228<h1>Forbidden</h1><pre>Request ID: 2|2023-09-20-06-04-29-144C09DD00138970|59ccae99eb2f055a7b107e4e</pre> <br>

Admin@MSI MINGW64 ~
$ curl http://www.rzd.ru
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   150  100   150    0     0   1413      0 --:--:-- --:--:-- --:--:--  1470
<html>
<head><title>301 Moved Permanently</title></head>
<body bgcolor="white">
<center><h1>301 Moved Permanently</h1></center>
</body>
</html>

Admin@MSI MINGW64 ~
$ curl www.rzd.ru
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:--  0:00:05 --:--:--     0
  0     0    0     0    0     0      0      0 --:--:--  0:00:07 --:--:--     0
100   150  100   150    0     0      6      0  0:00:25  0:00:22  0:00:03    31
<html>
<head><title>301 Moved Permanently</title></head>
<body bgcolor="white">
<center><h1>301 Moved Permanently</h1></center>
</body>
</html>

Admin@MSI MINGW64 ~
$ curl rzd.ru
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   150  100   150    0     0   1194      0 --:--:-- --:--:-- --:--:--  1219
<html>
<head><title>301 Moved Permanently</title></head>
<body bgcolor="white">
<center><h1>301 Moved Permanently</h1></center>
</body>
</html>
```
##  запрос curl -I -s
```
Admin@MSI MINGW64 ~
$ curl -I -s  http://www.rzd.ru
HTTP/1.1 301 Moved Permanently
Date: Wed, 20 Sep 2023 06:11:02 GMT
Content-Type: text/html
Content-Length: 150
Connection: keep-alive
Location: https://www.rzd.ru:443/
```
## подобные запросы не работают
```
Admin@MSI MINGW64 ~
$ curl -I -w "%{remote_port}\n" http://www.rzd.ru
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:--  0:00:03 --:--:--     0

  0     0    0     0    0     0      0      0 --:--:--  0:00:04 --:--:--     0
  0     0    0     0    0     0      0      0 --:--:--  0:00:06 --:--:--     0
Admin@MSI MINGW64 ~
$ curl -i -k http://www.rzd.ru --proxy "http://wp:3128"
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:--  0:00:01 --:--:--     0curl: (5) Could not resolve proxy: wp
```
## яндекс
с 4-мя спосоюави ввода, выдается только  начало
```
Admin@MSI MINGW64 ~
$ curl dzen.ru
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
Admin@MSI MINGW64 ~
$ curl https://dzen.ru/?yredirect=true
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
Admin@MSI MINGW64 ~
$ curl http://dzen.ru
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
Admin@MSI MINGW64 ~
$ curl www.dzen.ru
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
```
пробуем узнать подробности
```
Admin@MSI MINGW64 ~
$ curl -I -s dzen.ru
HTTP/1.1 302 Moved temporarily
Content-Length: 0
Location: https://dzen.ru/

Admin@MSI MINGW64 ~
$ curl -I https://dzen.ru | awk 'NR==1{print $2}' \\узнаем протокол по которому осуществляется запрос
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
200

Admin@MSI MINGW64 ~
$ curl -I -s dzen.ru | grep -i "Data"
\\ничего не выводит

Admin@MSI MINGW64 ~
$ curl -I dzen.ru | grep -iE "x-some-header|other-header"
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0

Admin@MSI MINGW64 ~
$ curl -I -s dzen.ru | head -n 1
HTTP/1.1 302 Moved temporarilyAdmin@MSI MINGW64 ~
$ curl -I -k -w "%{remote_port}\n" https://dzen.ru
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0HTTP/1.1 200 Ok
Cache-Control: no-cache, no-store, max-age=0, must-revalidate
Content-Security-Policy-Report-Only: default-src 'none'; connect-src 'self' an.yandex.ru strm.yandex.ru *.strm.yandex.net mc.yandex.ru yandex.st yastatic.net matchid.adfox.yandex.ru adfox.yandex.ru ads.adfox.ru ads6.adfox.ru jstracer.yandex.ru yastat.net yandex.ru awaps.yandex.net awaps.yandex.ru verify.yandex.ru *.verify.yandex.ru favicon.yandex.net pixel.adsafeprotected.com tps.doubleverify.com ad.adriver.ru amc.yandex.ru *.tunneler-si.dzen.ru *.tun.si.dzen.ru http-check-headers.yandex.ru mc.yandex.az mc.yandex.by mc.yandex.co.il mc.yandex.com mc.yandex.com.am mc.yandex.com.ge mc.yandex.com.tr mc.yandex.ee mc.yandex.fr mc.yandex.kg mc.yandex.kz mc.yandex.lt mc.yandex.lv mc.yandex.md mc.yandex.tj mc.yandex.tm mc.yandex.ua mc.yandex.uz mc.admetrica.ru yandexmetrica.com yandexmetrica.com:29009 yandexmetrica.com:30102 forms-ext-api.yandex.ru strm.yandex.net *.strm.yandex.ru *.cdn.ngenix.net zen-rc3.yandex.ru frontend.vh.yandex.ru https://vh.test.yandex.ru/live/ wss://push.yandex.ru api.passport.yandex.ru api.passport-test.yandex.ru suggest-maps.yandex.ru/suggest-geo vk.ru static.dzeninfra.ru avatars.dzeninfra.ru cdn.dzen.ru video.dzen.ru log.dzen.ru playlog.dzen.ru cdn.dzeninfra.ru *.cdn.dzeninfra.ru *.extcdn.dzeninfra.ru *.hot-video.dzeninfra.ru cold-video.dzeninfra.ru *.cold-video.dzeninfra.ru s3.dzeninfra.ru *.s3.dzeninfra.ru *.ms.dzen.ru notify.dzen.ru clck.dzen.ru static-mon.yandex.net cloud-api.yandex.ru yandex.ru dzen.ru *.adlooxtracking.com *.adlooxtracking.ru *.adsafeprotected.com *.doubleverify.com *.moatads.com *.serving-sys.com *.serving-sys.ru *.mail.ru *.mradx.net *.imgsmail.ru *.criteo.com *.criteo.net *.mycdn.me *.vkuser.net; frame-src awaps.yandex.net yandexadexchange.net *.yandexadexchange.net yastatic.net *.yandex.ru banners.adfox.ru yastat.net yandex.ru storage.mds.yandex.net *.tunneler-si.dzen.ru *.tun.si.dzen.ru http-check-headers.yandex.ru blob: mc.yandex.ru mc.yandex.md zenadservices.net sso.passport.yandex.ru id.vk.com *.dzen.ru sso.dzen.ru static.dzeninfra.ru suggest.dzen.ru 'self' yandex.ru *.mail.ru *.mradx.net *.imgsmail.ru *.criteo.com *.criteo.net *.mycdn.me *.vkuser.net *.doubleverify.com *.doubleclick.net; img-src 'self' data: avatars-fast.yandex.net favicon.yandex.net an.yandex.ru banners.adfox.ru content.adfox.ru ads6.adfox.ru tns-counter.ru *.tns-counter.ru s3.mds.yandex.net ads.adfox.ru amc.yandex.ru mc.admetrica.ru wcm-ru.frontend.weborama.fr wcm.solution.weborama.fr ad.adriver.ru bs.serving-sys.com ad.doubleclick.net counter.yadro.ru gdeby.hit.gemius.pl mc.yandex.ru verify.yandex.ru *.verify.yandex.ru yastatic.net yastat.net avatars.mds.yandex.net yandex.ru px.moatads.com awaps.yandex.net awaps.yandex.ru gdero.hit.gemius.pl pixel.adlooxtracking.com tps.doubleverify.com impression.appsflyer.com rgi.io track.rutarget.ru ssl.hurra.com pixel.adsafeprotected.com storage.mds.yandex.net *.tunneler-si.dzen.ru *.tun.si.dzen.ru http-check-headers.yandex.ru mc.yandex.az mc.yandex.by mc.yandex.co.il mc.yandex.com mc.yandex.com.am mc.yandex.com.ge mc.yandex.com.tr mc.yandex.ee mc.yandex.fr mc.yandex.kg mc.yandex.kz mc.yandex.lt mc.yandex.lv mc.yandex.md mc.yandex.tj mc.yandex.tm mc.yandex.ua mc.yandex.uz mc.webvisor.org *.mediascope.mc.yandex.ru avatars.mdst.yandex.net zen.s3.yandex.net strm.yandex.ru strm.yandex.net sso.passport.yandex.ru dzen.ru avatars.dzeninfra.ru static.dzeninfra.ru cdn.dzen.ru video.dzen.ru log.dzen.ru playlog.dzen.ru s3.dzeninfra.ru *.ms.dzen.ru *.s3.dzeninfra.ru *.zen.yandex.com *.m-counter.ru www.m-counter.ru www.tns-counter.ru *.mail.ru *.mradx.net *.imgsmail.ru *.criteo.com *.criteo.net *.mycdn.me *.vkuser.net *.doubleverify.com *.adsafeprotected.com *.serving-sys.com *.serving-sys.ru *.weborama.fr *.weborama-tech.ru *.hit.gemius.pl consentmanager.mgr.consensu.org cdn.consentmanager.mgr.consensu.org *.adlooxtracking.com *.adlooxtracking.ru vk.com vk.ru *.userapi.com *.vk.com *.vk.ru; media-src *.yandex.net strm.yandex.ru *.strm.yandex.r  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0ent.adfox.ru data: yastat.net *.mycdn.me *.vkuser.net *.tunneler-si.dzen.ru *.tun.si.dzen.ru http-check-headers.yandex.ru blob: *.strm.yandex.net *.cdn.ngenix.net cdn.dzen.ru video.dzen.ru *.cdn.dzeninfra.ru *.extcdn.dzeninfra.ru *.hot-video.dzeninfra.ru cold-video.dzeninfra.ru *.cold-video.dzeninfra.ru *.s3.dzeninfra.ru *.mail.ru *.mradx.net *.imgsmail.ru *.criteo.com *.criteo.net; script-src 'unsafe-inline' 'unsafe-eval' an.yandex.ru yandex.st yastatic.net mc.yandex.ru banners.adfox.ru ads.adfox.ru ads6.adfox.ru yastat.net yandex.ru z.moatads.com storage.mds.yandex.net *.tunneler-si.dzen.ru *.tun.si.dzen.ru http-check-headers.yandex.ru mc.yandex.az mc.yandex.by mc.yandex.co.il mc.yandex.com mc.yandex.com.am mc.yandex.com.ge mc.yandex.com.tr mc.yandex.ee mc.yandex.fr mc.yandex.kg mc.yandex.kz mc.yandex.lt mc.yandex.lv mc.yandex.md mc.yandex.tj mc.yandex.tm mc.yandex.ua mc.yandex.uz chat.s3.yandex.net sso.dzen.ru sso.passport.yandex.ru static.dzeninfra.ru 'self' *.zen.yandex.com dzen.ru *.mail.ru *.mradx.net *.imgsmail.ru *.criteo.com *.criteo.net *.mycdn.me *.vkuser.net *.adlooxtracking.com *.adlooxtracking.ru *.adsafeprotected.com *.doubleverify.com *.moatads.com *.dvtps.com *.doubleclick.net *.serving-sys.ru *.userapi.com vk.com vk.ru *.vk.com *.vk.ru; style-src 'unsafe-inline' 'unsafe-eval' yandex.st yastatic.net banners.adfox.ru content.adfox.ru yastat.net *.tunneler-si.dzen.ru *.tun.si.dzen.ru http-check-headers.yandex.ru yandex.ru static.dzeninfra.ru 'self' *.zen.yandex.com dzen.ru *.mail.ru *.mradx.net *.imgsmail.ru *.criteo.com *.criteo.net *.mycdn.me *.vkuser.net; font-src 'self' data: an.yandex.ru yastatic.net yastat.net *.tunneler-si.dzen.ru *.tun.si.dzen.ru http-check-headers.yandex.ru static.dzeninfra.ru *.mail.ru *.mradx.net *.imgsmail.ru *.criteo.com *.criteo.net *.mycdn.me *.vkuser.net fonts.gstatic.com; child-src blob: mc.yandex.ru; manifest-src *.dzen.ru/manifest.webmanifest 'self'; report-uri https://csp.yandex.net/csp?from=zen_old&project=zen&yandex_login=&yandexuid=6670734801695190819&requestid=1348732743.123.1695190819587.51219&page=site_desktop;
Content-Type: text/html; charset=utf-8
Set-Cookie: _yasc=0oCOeupYX+BZnXTzvbo+z6s6a3cVzTq6Je9PpNJWcIUac7rALT91hHKE+PURr74D; domain=.dzen.ru; path=/; expires=Sat, 17 Sep 2033 06:20:19 GMT; secure
X-Content-Type-Options: nosniff
X-Frame-Options: deny
X-Requestid: 1348732743.123.1695190819587.51219
X-XSS-Protection: 1; mode=block
X-Yandex-Req-Id: 1695190819563337-1559746283847769837000128-production-app-host-vlx-zen-146

443
```
## python
```
Admin@MSI MINGW64 ~
$ curl https://www.python.org
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0<!doctype html>
<!--[if lt IE 7]>   <html class="no-js ie6 lt-ie7 lt-ie8 lt-ie9">   <![endif]-->
<!--[if IE 7]>      <html class="no-js ie7 lt-ie8 lt-ie9">          <![endif]-->
<!--[if IE 8]>      <html class="no-js ie8 lt-ie9">                 <![endif]-->
<!--[if gt IE 8]><!--><html class="no-js" lang="en" dir="ltr">  <!--<![endif]-->

<head>
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-TF35YF9CVH"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-TF35YF9CVH');
    </script>

    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
#опять много html ....
</html>

Admin@MSI MINGW64 ~
$ curl http://www.python.org
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0

Admin@MSI MINGW64 ~
$ curl www.python.org
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0

Admin@MSI MINGW64 ~
$ curl python.org
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
```
## curl -i -s https://www.python.org
```
Admin@MSI MINGW64 ~
$ curl -i -s https://www.python.org
HTTP/1.1 200 OK
Connection: keep-alive
Content-Length: 50329
Server: nginx
Content-Type: text/html; charset=utf-8
X-Frame-Options: SAMEORIGIN
Via: 1.1 vegur, 1.1 varnish, 1.1 varnish
Accept-Ranges: bytes
Date: Wed, 20 Sep 2023 06:25:59 GMT
Age: 587
X-Served-By: cache-iad-kiad7000025-IAD, cache-fra-eddf8230101-FRA
X-Cache: HIT, HIT
X-Cache-Hits: 30, 6
X-Timer: S1695191160.709484,VS0,VE0
Vary: Cookie
Strict-Transport-Security: max-age=63072000; includeSubDomains; preload
#далее идет html который мы уже видели
```
## запросы номеров протокола и порта
```
Admin@MSI MINGW64 ~
$ curl -I https://www.python.org | awk 'NR==1{print $2}'
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0 50329    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
200
Admin@MSI MINGW64 ~
$ curl -I -k -w "%{remote_port}\n" https://www.python.org
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0 50329    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0HTTP/1.1 200 OK
Connection: keep-alive
Content-Length: 50329
Server: nginx
Content-Type: text/html; charset=utf-8
X-Frame-Options: SAMEORIGIN
Via: 1.1 vegur, 1.1 varnish, 1.1 varnish
Accept-Ranges: bytes
Date: Wed, 20 Sep 2023 06:28:55 GMT
Age: 763
X-Served-By: cache-iad-kiad7000025-IAD, cache-fra-eddf8230088-FRA
X-Cache: HIT, HIT
X-Cache-Hits: 30, 8
X-Timer: S1695191335.301008,VS0,VE0
Vary: Cookie
Strict-Transport-Security: max-age=63072000; includeSubDomains; preload

443
```
## в случае с git-scm не так много html кода
```
Admin@MSI MINGW64 ~
$ curl https://git-scm.com
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset='utf-8'>
  <meta content='IE=edge,chrome=1' http-equiv='X-UA-Compatible'>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Git</title>

  <link href='/favicon.ico' rel='shortcut icon' type='image/x-icon'>

  <link rel="stylesheet" media="screen" href="/assets/application-a058ab010d6f86a86903175bbfdaac30ef6057e5901875616753328abbf98b2c.css" />
  <script src="/assets/modernize-b3ebe0c31c24f230dc62179d3e1030d2e57a53b1668d9382c0a27dbd44a94beb.js"></script>
  <!--[if (gte IE 6)&(lte IE 8)]>
  <script src="/javascripts/selectivizr-min.js"></script>
  <![endif]-->

</head>

<body id="home">

  <div class="inner">
    <header>

  <a href="/"><img src="/images/logo@2x.png" width="110" height="46" alt="Git" /></a>
  <span id="tagline"></span>
  <script type="text/javascript">
    var taglines = ["fast-version-control","everything-is-local","distributed-even-if-your-workflow-isnt","local-branching-on-the-cheap","distributed-is-the-new-centralized"];
    var tagline = taglines[Math.floor(Math.random() * taglines.length)];
    document.getElementById('tagline').innerHTML = '--' + tagline;
  </script>
  <form id="search" action="/search/results">
    <input id="search-text" name="search" placeholder="Search entire site..." autocomplete="off" type="text" />
  </form>
  <div id="search-results"></div>

</header>

  </div> <!-- .inner -->

    <div id="masthead">
  <div class="inner">
    <div>
      <p>
        Git is a <a href="/about/free-and-open-source">free and open source</a>
        distributed version control system designed to handle everything from small to
        very large projects with speed and efficiency.
      </p>
      <p>
        Git is <a href="/doc">easy to learn</a> and has a
        <a href="/about/small-and-fast">tiny footprint with lightning fast performance</a>.
        It outclasses SCM tools like Subversion, CVS, Perforce, and ClearCase
        with features like <a href="/about/branching-and-merging">cheap local branching</a>,
        convenient <a href="/about/staging-area">staging areas</a>, and
        <a href="/about/distributed">multiple workflows</a>.
      </p>
    </div>
    <div class="illustration-wrapper">
      <img class="illustration" src="/images/branching-illustration@2x.png" width="389" height="251" />
    </div>
  </div> <!-- .inner --></div> <!-- #masthead -->

    <div id="content-wrapper">
      <div class="inner">
        <div id="front-content">
  <section id="front-navigation">
    <nav id="front-nav">
      <ul>
        <li id="nav-about">
          <a href="/about">
            <img src="/images/icons/nav-about@2x.png" width="74" height="74" />
            <h3>About</h3>
            <p>The advantages of Git compared to other source control systems.</p>
</a>        </li>
        <li id="nav-documentation">
          <a href="/doc">
            <img src="/images/icons/nav-documentation@2x.png" width="74" height="74" />
            <h3>Documentation</h3>
            <p>Command reference pages, Pro Git book content, videos and other material.</p>
</a>        </li>
        <li id="nav-downloads">
          <a href="/downloads">
            <img src="/images/icons/nav-downloads@2x.png" width="74" height="74" />
            <h3>Downloads</h3>
            <p>GUI clients and binary releases for all major platforms.</p>
</a>        </li>
        <li id="nav-community">
          <a href="/community">
            <img src="/images/icons/nav-community@2x.png" width="74" height="74" />
            <h3>Community</h3>
            <p>Get involved! Bug reporting, mailing list, chat, development and more.</p>
</a>        </li>
      </ul>
    </nav>
    <div id="front-book">
      <img src="/images/progit2.png" width="56" height="74" />
      <p>
        <strong><a href="/book">Pro Git</a></strong>
        by Scott Chacon and Ben Straub is available to
        <a href="/book">read online for free</a>.
        Dead tree versions are available on <a href="https://www.amazon.com/Pro-Git-Sc100  7313    0  7313    0     0  18200      0 --:--:-- --:--:-- --:--:-- 18513e=UTF8&camp=1789&creative=9325&creativeASIN=1430218339&linkCode=as2&tag=git-sfconservancy-20">Amazon.com</a>.
      </p>
    </div>
  </section>
  <section id="front-downloads">
    <div class="monitor">

  <h4> Latest source Release </h4>

  <span class="version">
    2.42.0
  </span>

  <a href="https://raw.github.com/git/git/master/Documentation/RelNotes/2.42.0.txt">Release Notes</a>
  <span class="release-date">
    (2023-08-21)
  </span>
  <span data-mac="2.33.0" data-win="2.42.0" id="installer-version"></span>

  <a class="button" id="download-link" href="https://www.kernel.org/pub/software/scm/git/">Download Source Code</a>
</div>

    <table>
      <tr>
        <td nowrap="true"><a class="icon gui" id="gui-link" href="/downloads/guis">Graphical UIs</a></td>
        <td nowrap="true"><a class="icon older-releases" href="https://www.kernel.org/pub/software/scm/git/">Tarballs</a></td>
      </tr>
      <tr>
        <td nowrap="true"><a class="icon windows" id="alt-link" href="/download/win">Windows Build</a></td>
        <td nowrap="true"><a class="icon source" href="https://github.com/git/git">Source Code</a></td>
      </tr>
    </table>
</section></div>

<section id="companies-projects">
  <h3 class="text-center"> Companies &amp; Projects Using Git </h3>
  <ul>
    <li><a class="google" href="https://github.com/google">Google</a></li>
    <li><a class="microsoft" href="https://github.com/Microsoft">Microsoft</a></li>
    <li><a class="twitter" href="https://github.com/twitter">Twitter</a></li>
    <li><a class="linked-in" href="https://github.com/linkedin">LinkedIn</a></li>
    <li><a class="netflix" href="https://github.com/netflix">Netflix</a></li>
    <li><a class="perl" href="https://perl5.git.perl.org/perl.git">Perl</a></li>
    <li><a class="postgresql" href="https://git.postgresql.org/gitweb/">PostgreSQL</a></li>

    <li><a class="android" href="https://android-review.googlesource.com/#/q/status:open,n,z">Android</a></li>
    <li><a class="linux" href="https://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git">Linux</a></li>
    <li><a class="rails" href="https://github.com/rails/rails">Ruby on Rails</a></li>
    <li><a class="qt" href="https://code.qt.io/cgit/">Qt</a></li>
    <li><a class="gnome" href="https://gitlab.gnome.org/GNOME">Gnome</a></li>
    <li><a class="eclipse" href="https://git.eclipse.org/c/">Eclipse</a></li>
    <li><a class="kde" href="https://invent.kde.org/explore/groups">KDE</a></li>
    <li><a class="x" href="https://cgit.freedesktop.org/xorg/xserver/">X</a></li>
</ul>
</section>

        <footer>
  <div class="site-source">
    <a href="/site">About this site</a><br>
    Patches, suggestions, and comments are welcome.
  </div>
  <div class="sfc-member">
    Git is a member of <a href="/sfc">Software Freedom Conservancy</a>
  </div></footer>
<a href="#top" class="no-js scrollToTop" id="scrollToTop" data-label="Scroll to top">
  <img src="/images/icons/chevron-up@2x.png" width="20" height="20" alt="scroll-to-top"/>
</a>
<script src="/assets/application-b09f91f7c527919e4bc194769429065537d64a7f73b9fe93b107afef32b02939.js"></script>

      </div> <!-- .inner -->
    </div> <!-- #content-wrapper -->

</body>
</html>


Admin@MSI MINGW64 ~
$ curl http://git-scm.com
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0

Admin@MSI MINGW64 ~
$ curl git-scm.com
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
```
## curl -I -s
```
Admin@MSI MINGW64 ~
$ curl -I -s https://git-scm.com
HTTP/1.1 200 OK
Date: Wed, 20 Sep 2023 06:34:14 GMT
Content-Type: text/html; charset=utf-8
Connection: keep-alive
X-Frame-Options: SAMEORIGIN #Сайты могут использовать это, чтобы избежать атак с перехватом кликов, гарантируя, что их контент не будет внедрен на другие сайты
X-Xss-Protection: 1; mode=block #особенность Internet Explorer, Chrome и Safari, которая останавливает загрузку страниц при обнаружении (XSS) атаки.
X-Content-Type-Options: nosniff #маркер, используемый сервером для указания того, что типы MIME, объявленные в заголовках Content-Type, должны соблюдаться и не изменяться.
X-Download-Options: noopen #Это предназначено для Internet Explorer начиная с версии 8, чтобы указать браузеру не открывать загрузку непосредственно в браузере, а вместо этого предоставлять только опцию "Сохранить"
X-Permitted-Cross-Domain-Policies: none #указывает, разрешен ли файл междоменной политики (crossdomain.xml)
Referrer-Policy: strict-origin-when-cross-origin #определяет, сколько информации о реферере (отправляемой с заголовком Referer) должно быть включено в запросы. 
Cache-Control: public, max-age=14400
Etag: W/"db69273d9410cbf4536e9d4b3a59685d" # закрытый идентификатор, 
#присвоенный веб-сервером на определённую версию ресурса, найденного на URL
X-Request-Id: 476d2e08-474c-4f3d-8503-d83ed21ae45f #уникальный идентификатор ответа.
X-Runtime: 0.015343 #используется для указания времени (в секундах), необходимого приложению для обработки каждого запроса.
Via: 1.1 vegur #Он используется для отслеживания пересылки сообщений, предотвращения зацикливания запросов и определения протокольных возможностей отправителей по цепочке запрос/ответ. 
CF-Cache-Status: HIT
Age: 14159
Server: cloudflare
CF-RAY: 80980a9d9b5316fe-DME #(иначе известный как Ray ID) представляет собой хэшированное значение, в котором закодирована информация о дата-центре и запросе посетителя
```
## вывод номера порта
```
Admin@MSI MINGW64 ~
$ curl -I -k -w "%{remote_port}\n" https://git-scm.com
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0HTTP/1.1 200 OK
#laalala повторяющийся вывод
443 
```
## вижуал студиа
```
Admin@MSI MINGW64 ~
$ curl https://code.visualstudio.com
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  1 50213    1   533    0     0    934      0  0:00:53 --:--:--  0:00:53   941<!DOCTYPE html>
<html lang="en">
#много html
</html>

Admin@MSI MINGW64 ~
$ curl http://code.visualstudio.com
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0

Admin@MSI MINGW64 ~
$ curl www.code.visualstudio.com
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0curl: (6) Could not resolve host: www.code.visualstudio.com

Admin@MSI MINGW64 ~
$ curl code.visualstudio.com
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
```
## curl -I -s https://code.visualstudio.com
```
Admin@MSI MINGW64 ~
$ curl -I -s https://code.visualstudio.com
HTTP/1.1 200 OK
Content-Length: 50213
Content-Type: text/html; charset=utf-8
Accept-Ranges: bytes
ETag: W/"c425-XBxswsHoV0dlJCAKuBbwZ9s5rjQ"
Strict-Transport-Security: max-age=31536000; includeSubDomains \\заголовок ответа (часто используется аббревиатура HSTS (en-US)), позволяющий web-сайтам уведомить браузер о том, что доступ к ним должен быть осуществлён только посредством HTTPS вместо HTTP.
Content-Security-Policy: frame-ancestors 'self'
X-Frame-Options: SAMEORIGIN
X-XSS-Protection: 1; mode=block
X-Content-Type-Options: nosniff
X-Content-Type-Options: nosniff
X-Powered-By: ASP.NET
x-azure-ref: 07JUKZQAAAACrDAhLGc56T6nDnVrYk0whU1RPRURHRTE0MDYAYmU4N2RjNmQtNDBmOS00NWIwLTg4MTAtOTkxMDg3ZWY4YjI5 \\никальная ссылочная строка, идентифицирующая запрос, обслуживаемый Front Door. Она используется для поиска в журналах доступа и критически важных для устранения неполадок
X-Cache: CONFIG_NOCACHE
Date: Wed, 20 Sep 2023 06:49:16 GMT
```
## номер порта и только заголовки
```
Admin@MSI MINGW64 ~
$ curl -I -k -w "%{remote_port}\n" https://code.visualstudio.com
\\повторяющая информация предыдущего запроса и номер порта
443
Admin@MSI MINGW64 ~ \\заголовки
$ curl -I  http://code.visualstudio.com | grep -iE "x-some-header|other-header"
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
```
