from models.database import db


class Category(db.Model):

    __tablename__ = "categorias"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    nome = db.Column(
        db.String(100),
        nullable=False,
        unique=True
    )

    slug = db.Column(
        db.String(120),
        nullable=False,
        unique=True
    )

    descricao = db.Column(
        db.Text
    )

    posts = db.relationship(
        "Post",
        backref="categoria",
        lazy=True
    )

    def __repr__(self):
        return f"<Category {self.nome}>"