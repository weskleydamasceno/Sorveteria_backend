#
# Configurações da aplicação
#
Debug = True

# connection string: mysql://usuario:senha@host/nomedobanco
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost/dbdevweb'

# SQLAlchemy monitorará modificações de objetos
SQLALCHEMY_TRACK_MODIFICATIONS = True