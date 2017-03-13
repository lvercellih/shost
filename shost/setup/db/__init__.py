from shost.setup.db import commons


def setup_db():
    commons.setup_users()
    commons.setup_currencies()