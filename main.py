from flask import Flask

from flask_sqlalchemy import SQLAlchemy

from comment import bp as comment_bp
from hashtag import bp as hashtag_bp
from user import bp as user_bp
from posts import bp as posts_bp
from photo import bp as photo_bp

app = Flask(__name__)

# Подключение базы данных
db = SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///media.db'
db.init_app(app)


# Регистрация компонента
app.register_blueprint(comment_bp)
app.register_blueprint(hashtag_bp)
app.register_blueprint(user_bp)
app.register_blueprint(posts_bp)
app.register_blueprint(photo_bp)


@app.route('/hello')
def hellower():
    return 'Hello world'


app.run()
