# Куда пойти — Москва глазами Артёма

Фронтенд для будущего сайта о самых интересных местах в Москве. Авторский проект Артёма.

![Куда пойти](https://github.com/devmanorg/where-to-go-frontend/blob/master/.gitbook/assets/site.png?raw=true)

[Демка сайта](https://alexwolf.pythonanywhere.com/).

## Установка

`Python3` должен быть установлен. Используйте `pip` (или `pip3`, если есть конфликт с `Python2`) для установки зависимостей:

```sh
pip install -r requirements.txt
```

Настройте таблицы БД командой:

```sh
python manage.py migrate
```

## Настройка

Скопируйте файл `.env.example` из папки short_links и переименуйте его в `.env`.

Заполните переменные окружения в файле `.env`:

- `ALLOWED_HOSTS` - Разрешенные хосты. Указываются через запятую, например: `127.0.0.1`,`localhost`;
- `SECRET_KEY` - Секретный ключ Django;
- `DEBUG` - Если нужно включить режим отладки web-сервера, установите значение в `True`.

Для доступа в административную часть сайта создайте суперпользователя (администратора) сайта командой:

```sh
python manage.py createsuperuser
```

## Запуск

Запустите командой:

```sh
python manage.py runserver localhost:80
```

## Загрузка данных из JSON-файлов

Данные об интересных местах могут быть загружены из JSON-файлов. Образцы таких файлов расположены в [учебном репозитории](https://github.com/devmanorg/where-to-go-places/tree/master/places)

Вы можете загрузить любое место (либо несколько) указав RAW-ссылку(и) на нужный(ые) JSON-файл(ы):

```sh
python manage.py load_place <RAW_JSON url> [<RAW_JSON url> ...]
```

Так же можно загрузить максимально возможное количество из имеющихся в репозитории (одинаковые координаты недопустимы!)

```sh
python manage.py load_place --repo
```

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).

Тестовые данные взяты с сайта [KudaGo](https://kudago.com).
