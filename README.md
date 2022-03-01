# KMG Parser

* Склонируйте репозиторий
```shell
$ git clone https://github.com/SamatSadvakasov/kmg_test.git
```

* Перейдите в склонированную директорию
```shell
$ cd ./kmg_test
```

* Запустите контейнер Postgresql
```shell
$ docker-compose up -d
```

* Создайте изолированную среду Python и установите зависимости
```shell
$ python3 -m virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```


* Инициализируйте БД
```shell
$ python main.py -i
```

* Запустите API
```shell
$ uvicorn api.app:app --host 0.0.0.0 --port 8080
```

* Откройте в браузере адрес http://localhost:8080/
Документация API в swagger


### Аргументы парсера
```shell
$ python main.py -i # Инициализация БД (migration up)
$ python main.py --drop_database # Уничтожение базы (migration down)
$ python main.py -d path_to_directory # Парсинг директории по пути (parsing/task/)
```