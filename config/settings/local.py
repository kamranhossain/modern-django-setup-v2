from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=4ph*@9_!_swr@r*6-_g319fs2c-2j!3io4m^cdu0arxjhb@y4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DJANGO_DEBUG', True)