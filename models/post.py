from datetime import datetime

from models.database import db
from models.tag import post_tags


class Post(db.Model):

    __tablename__ = "posts"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    titulo = db.Column(
        db.String(255),
        nullable=False
    )

    slug = db.Column(
        db.String(255),
        unique=True,
        nullable=False
    )

    resumo = db.Column(
        db.Text
    )

    conteudo = db.Column(
        db.Text,
        nullable=False
    )

    imagem_capa = db.Column(
        db.String(255)
    )

    destaque = db.Column(
        db.Boolean,
        default=False
    )

    publicado = db.Column(
        db.Boolean,
        default=True
    )

    visualizacoes = db.Column(
        db.Integer,
        default=0
    )

    categoria_id = db.Column(
        db.Integer,
        db.ForeignKey("categorias.id")
    )

    autor_id = db.Column(
        db.Integer,
        db.ForeignKey("usuarios.id")
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

    comentarios = db.relationship(
        "Comment",
        backref="post",
        lazy=True,
        cascade="all, delete"
    )

    tags = db.relationship(
        "Tag",
        secondary=post_tags,
        lazy="subquery",
        backref=db.backref(
            "posts",
            lazy=True
        )
    )

    def __repr__(self):
        return f"<Post {self.titulo}>"