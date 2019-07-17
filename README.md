# Start

```
$ git clone <repo>
$ cd <project name>

$ docker-machine create -d virtualbox dev;
$ eval "$(docker-machine env dev)"
$ docker-compose up --build -d
```



# Use

### Web browser

1. Get ip address: `$ docker-machine ip dev`
2. Type in a web browser (e.g.: http://192.168.99.101).


### API

```
$ curl -i http://<ip address>/api/exchange-rates/usd/2019-07-01/2019-07-15
```


### Info

```
$ docker-compose ps
$ docker-compose logs
```



# Stop

```
$ docker-compose stop
```
