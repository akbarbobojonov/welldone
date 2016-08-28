# Well Done Application

welldone - biron bir proyektni boshlaganda kerak bo‘ladigan sahifalar.

### Foydalanilgan open source proyektlar

* [Django] - Pythonda yozilgan Web framework
* [PostgreSQL] - Ma’lumotlar bazasi
* [Semantic UI] - HTML/Javascript framework

### O‘rnatish

```sh
$ pip install -r requirements.txt
```

```sh
$ python manage.py migrate
```

Saytni ishga tushirishdan oldin *welldone/settings/local.py* ni yaratish kerak. 

*local.py* ga misol:

```sh
# Email settings

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'your@mail.com'
EMAIL_HOST_PASSWORD = 'yourmailpassword'
EMAIL_PORT = 587

NOREAPLY_EMAIL = 'noreaply-your@mail.com'
```

   [Semantic UI]: <http://semantic-ui.com/>
   [Django]: <https://www.djangoproject.com/>
   [PostgreSQL]: <https://www.postgresql.org/>
