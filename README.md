## This project provides API-service for Eshop - another project

### Технологии

- python
- пакеты python из файла requirements.txt

### Структура

```shell
.
├── eshop_api/
│   ├── eshop_api/
│   │   ├── asgi.py
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   └── yasg.py
│   ├── shop/
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── service.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   └── manage.py
├── media/
├── static/
│   ├── admin/
│   ├── ckeditor/
│   ├── css/
│   ├── img/
│   └── js/
└── Volume/
    └── DB
```

### API

- admin/

---

- api/v1/item/ GET
- api/v1/item/<int:pk>/ GET
- api/v1/review/ POST
- api/v1/vendors/ GET
- api/v1/vendors/<int:pk>/ GET
- api/v1/category/ GET
- api/v1/category/<str:url>/ GET

---

- auth/token/login/ POST
- auth/token/logout/ POST
- auth/users/ GET
- auth/users/ POST
- auth/user/activation/ POST
- auth/users/me/ GET
