# Start

```
$ git clone <repo>
$ cd <project name>

$ docker-machine create -d virtualbox dev;
$ eval "$(docker-machine env dev)"
$ docker-compose up --build -d
```


# Get info

```
$ docker-compose ps
$ docker-compose logs
```


# Use

## Web app

Get ip by running command below & type in a web browser (e.g.: http://192.168.99.101)

```
$ docker-machine ip dev
```


## API

```
$ curl -i http://192.168.99.101/api/exchange-rates/usd/2019-07-01/2019-07-15
```


# Stop

```
$ docker-compose stop
```
