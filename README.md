# OZON UI AUTOTESTS

Проект предназначен для проверки UI сайта Ozon. 

##Структура проекта
<ul>
    <li>page_elements
        <ul>
            <li>Классы где хранятся локаторы элементов страниц</li>
        </ul>
    </li>
    <li>page_object
        <ul>
            <li>Классы где хранятся логика работы с элементами страниц</li>
        </ul>
    </li>
    <li>tests - Хранятся все функциональные тесты</li>
    <li>.gitignore - Игнорирование файлов и папок гитом</li>
    <li>conftest.py - Содержит фикстуры и описание праметров запуска тестов</li>
    <li>requirements.txt - Описание зависимостей</li>
    <li>Dockerfile - Конфигурационный файл с инструкциями по созданию Docker-образов./li>
    <li>test.sh - Shell скрипт для создания Docker-образа и запуска тестов в нем</li>
 </ul>

## Локальный запуск тестов
Откройте к командной строке проект и выполните команду

` pytest ./tests/ `

Так же тесты можно запустить с параметрами

```
pytest ./tests/ --alluredir=<Дериктория куда складываются файля для формирования отчета allure> --url <Url запуска тестов> --executor <Где запускать тесты> --browser <Браузер для запуска> --drivers <Путь до папки с selenium драйверами> --n <Количество потоков>`
```

## Запуск тестов в Docker 
Откройте к командной строке проект и выполните команды

```
DOCKER_SCAN_SUGGEST=false docker build -t tests .`
docker run --env url=<Url запуска тестов> --env browser=<Браузер для запуска> --name tests_run --network <Подключение контейнера для прогона тестов. Например selenoid> tests \
 && docker cp tests_run:/app/allure-report . \
 && allure serve allure-report

```

