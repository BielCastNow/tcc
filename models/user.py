from datetime import datetime
from models.database import db


class User(db.Model):

    __tablename__ = "usuarios"

    id = db.Column(db.Integer, primary_key=True)

    nome = db.Column(
        db.String(120),
        nullable=False
    )

    email = db.Column(
        db.String(150),
        unique=True,
        nullable=False
    )

    senha = db.Column(
        db.String(255),
        nullable=False
    )

    foto_perfil = db.Column(
        db.String(255)
    )

    biografia = db.Column(
        db.Text
    )

    admin = db.Column(
        db.Boolean,
        default=False
    )

    ativo = db.Column(
        db.Boolean,
        default=True
    )

    criado_em = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    atualizado_em = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    posts = db.relationship(
        "Post",
        backref="autor",
        lazy=True
    )

    comentarios = db.relationship(
        "Comment",
        backref="usuario",
        lazy=True
    )

    def __repr__(self):
        return f"<User {self.nome}>"