#
# Configurações da aplicação
#

import os
from os.path import abspath

DEBUG = True

# diretório base
basedir = os.path.abspath(os.path.dirname(__name__))

# diretório base da aplicação
BASE_DIR = basedir

# connection string: mysql://usuario:senha@host/nomedobanco
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost/dbdevweb'

# SQLAlchemy monitorará modificações de objetos
SQLALCHEMY_TRACK_MODIFICATIONS = True