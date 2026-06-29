from flask import (
    Blueprint,
    render_template,
    session,
    redirect
)

from models.post import Post
from models.user import User
from models.comment import Comment

admin = Blueprint(
    "admin",
    __name__,
    url_prefix="/admin"
)

def admin_required():
    return session.get("admin")

@admin.route("/")
def dashboard():

    if not admin_required():
        return redirect("/")

    total_posts = Post.query.count()

    total_users = User.query.count()

    total_comments = Comment.query.count()

    ultimos_posts = (
        Post.query
        .order_by(Post.criado_em.desc())
        .limit(5)
        .all()
    )

    return render_template(
        "admin/dashboard.html",
        total_posts=total_posts,
        total_users=total_users,
        total_comments=total_comments,
        ultimos_posts=ultimos_posts
    )