from models.database import db


class PostImage(db.Model):

    __tablename__ = "imagens_post"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    imagem = db.Column(
        db.String(255),
        nullable=False
    )

    legenda = db.Column(
        db.String(255)
    )

    post_id = db.Column(
        db.Integer,
        db.ForeignKey("posts.id")
    )

    def __repr__(self):
        return f"<PostImage {self.id}>"