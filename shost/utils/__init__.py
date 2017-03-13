from django.utils import timezone


def get_now():
    """
    Separado para poder establecer el tiempo como sea necesario durante los tests
    """
    return timezone.now()


def setallattr(obj, **kwargs):
    for k in kwargs:
        setattr(obj, k, kwargs.get(k))


def dict_except(obj, *args):
    result = {}
    for k in obj:
        if k not in args:
            result[k] = obj[k]
    return result
