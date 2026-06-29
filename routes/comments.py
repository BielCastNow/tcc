from flask import (
    Blueprint,
    request,
    redirect,
    session
)

from models.database import db
from models.comment import Comment

comments = Blueprint(
    "comments",
    __name__
)


@comments.route(
    "/comentar/<int:post_id>",
    methods=["POST"]
)
def comentar(post_id):

    if not session.get(
        "user_id"
    ):
        return redirect("/login")

    texto = request.form[
        "comentario"
    ]

    comentario = Comment(
        comentario=texto,
        usuario_id=session[
            "user_id"
        ],
        post_id=post_id
    )

    db.session.add(
        comentario
    )

    db.session.commit()

    return redirect(
        f"/post/{post_id}"
    )