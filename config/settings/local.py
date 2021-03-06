
from .base import *  # noqa
from .base import env


# GENERAL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = env(
    "SECRET_KEY",
    default="django-insecure-ry00cb&zi1^(5+e9icajm0izcvl--qpp0m0+$q0oke4e#*z&qz",
)


# https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1"]

# https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True
# Your stuff...
# ------------------------------------------------------------------------------
