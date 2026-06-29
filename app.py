from flask import Flask
from config import Config
from models.database import db
from routes.auth import auth
from routes.admin import admin
from routes.posts import posts
from routes.comments import comments
from routes.public import public

app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)

app.register_blueprint(auth)
app.register_blueprint(admin)
app.register_blueprint(posts)
app.register_blueprint(comments)
app.register_blueprint(public)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)