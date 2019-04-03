from app import db
from datetime import date

class Remessa(db.Model):
    __tablename__ = 'remessa'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    data = db.Column(db.Date, default=date.today)
    qtde = db.Column(db.Integer)
    status = db.Column(db.Boolean)
    vendidos = db.Column(db.Integer)
    pagos = db.Column(db.Integer)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    local_id = db.Column(db.Integer, db.ForeignKey('local.id'))

    def __init__(self, data, qtde, status, vendidos, pagos, usuario_id, local_id):
        self.data = data
        self.qtde = qtde
        self.status = status
        self.vendidos = vendidos
        self.pagos = pagos
        self.usuario_id = usuario_id
        self.local_id = local_id

    def __repr__(self):
        return "Remessa: {}".format(self.id)

class Usuario(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    senha = db.Column(db.String(120), nullable=False)

    remessas = db.relationship('Remessa', backref='usuario', lazy='dynamic')

    def __init__(self, username, senha):
        self.username = username
        self.senha = senha

    def __repr__(self):
        return "Usuario: {}".format(self.username)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

class Local(db.Model):
    __tablename__ = 'local'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    descricao = db.Column(db.String(20), nullable=False)

    remessas = db.relationship('Remessa', backref='local', lazy='dynamic')

    def __init__(self, descricao):
        self.descricao = descricao
    
    def __repr__(self):
        return "Local: {}".format(self.descricao)

