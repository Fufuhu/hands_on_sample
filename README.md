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

```bash
$ docker-compose up -d
$ python manage.py migrate --setting sampleapp.settings_prod
$ python manage.py runserver --setting sampleapp.settings_prod
```
