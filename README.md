# hands_on_sample

## environment

```bash
$ pip install -r sampleapp/requirements.txt
```

## Initialize

### With SQLite

```bash
$ python manage.py migrate
$ python manage.py run-server
```
### With MySQL

MySQLを使ってテストを実行する場合

```bash
$ docker-compose up --build
```

単純にMySQLバックエンドで起動させる場合

```bash
docker build -t guestbook `pwd`

docker run -d --name mysql -p 3306:3306 \
-e MYSQL_ROOT_PASSWORD="mysqlpassword" \
-e MYSQL_USER="guestbook" \
-e MYSQL_PASSWORD="guestbook_pass" \
-e MYSQL_DATABASE="guestbook" \
mysql:5

GUESTBOOK_DATABASE_HOST="127.0.0.1"
python manage.py migrate --settings sampleapp.settings_prod
python manage.py runserver --settings sampleapp.settings_prod
```
