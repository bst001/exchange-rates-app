# Start

```
$ git clone <repo>
$ cd <project name>

$ docker-machine create -d virtualbox dev
$ eval "$(docker-machine env dev)"
$ docker-compose up --build -d
$ docker-compose run web python manage.py initdb
```



# Use

First, get machine IP address: `$ docker-machine ip dev`


### Web browser

Type IP in a web browser (e.g.: http://192.168.99.101).


### API

```
$ curl -i http://<ip address>/api/exchange-rates/usd/2019-07-01/2019-07-15
```


# Other

### Info

```
$ docker-compose ps
$ docker-compose logs
```

### Stop

```
$ docker-compose stop
```

### Remove

```
$ docker-compose rm dev
$ docker-machine rm dev
```
