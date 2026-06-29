from datetime import datetime

from models.database import db


class Comment(db.Model):

    __tablename__ = "comentarios"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    comentario = db.Column(
        db.Text,
        nullable=False
    )

    aprovado = db.Column(
        db.Boolean,
        default=True
    )

    usuario_id = db.Column(
        db.Integer,
        db.ForeignKey("usuarios.id")
    )

    post_id = db.Column(
        db.Integer,
        db.ForeignKey("posts.id")
    )

    criado_em = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    def __repr__(self):
        return f"<Comment {self.id}>"