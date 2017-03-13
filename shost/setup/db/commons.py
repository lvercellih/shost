from shost import models
from shost.consts import users, currencies
from shost.utils import db


def setup_users():
    if models.User.objects.filter(id=users.SYSTEM).count() == 0:
        models.User.objects.create_user("system", "system@cred.com")
    if models.User.objects.filter(id=users.ROOT).count() == 0:
        models.User.objects.create_superuser("root", "root@cred.com", "1243")


def setup_currencies():
    db.install_dicts(models.Currency, [
        {"id": currencies.PEN, "iso_code": "604", "iso_name": "PEN", "decimal_digits": 2},
        {"id": currencies.USD, "iso_code": "840", "iso_name": "USD", "decimal_digits": 2},
    ])
