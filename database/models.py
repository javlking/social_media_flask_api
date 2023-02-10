from main import db
from werkzeug.security import generate_password_hash, check_password_hash


# Таблица пользователей
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String, nullable=False)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=True)
    email = db.Column(db.String, nullable=False)
    phone_number = db.Column(db.String, nullable=False)
    about = db.Column(db.String, nullable=True)

    # Изменить имя
    def change_username(self, user_id, new_username):
        user = User.query.get_or_404(user_id)

        # Меняем имя
        if user.username == new_username:
            return 'Новое имя должно отличаться от старого'

        user.username = new_username

        db.session.commit()

    ## ДЗ ##
    # Изменить номер телефона
    def change_phone_number(self, user_id, new_phone_number):
        user = User.query.get_or_404(user_id)

        # Меняем номер
        if user.phone_number == new_phone_number:
            return 'Новый номер должен отличаться от старого'

        user.phone_number = new_phone_number

        db.session.commit()

    # Изменить почту
    def change_email(self, user_id, new_email):
        user = User.query.get_or_404(user_id)

        # Меняем почту
        if user.email == new_email:
            return 'Новый адрес должен отличаться от старого'

        user.email = new_email

        db.session.commit()

    # Изменить "о себе"
    def change_about(self, user_id, new_about_text):
        user = User.query.get_or_404(user_id)

        # Меняем описание
        if user.about == new_about_text:
            return 'Новый адрес должен отличаться от старого'

        user.about = new_about_text

        db.session.commit()


# Таблица постов
class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    header = db.Column(db.String, nullable=False)
    main_text = db.Column(db.String, nullable=False)
    publish_date = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    post_likes = db.Column(db.Integer, default=0)

    user = db.relationship('User')

    # Изменить описание
    def change_main_text(self, post_id, new_main_text):
        current_post = Post.query.get_or_404(post_id)

        if current_post.main_text == new_main_text:
            return 'В новом тексте нет никаких изменений'

        current_post.main_text = new_main_text

        db.session.commit()


    ## ДЗ ##
    # Изменить header
    # Удалить пост
    # Счетчик лайков


# Таблица фото
class PhotoPost(db.Model):
    __tablename__ = 'photos_for_post'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id', ondelete='SET NULL'))
    photo_path = db.Column(db.String, nullable=False)

    post = db.relationship('Post')


# Таблица для коментарий
class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text = db.Column(db.String, nullable=False)
    likes = db.Column(db.Integer, nullable=True, default=0)
    date = db.Column(db.DateTime)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id', ondelete='SET NUll'))

    # Удалить коммент
    def delete_comment(self, comment_id):
        current_comment = Comment.query.get_or_404(comment_id)

        db.session.delete(current_comment)
        db.session.commit()

    # Счетчик лайков
    def likes_detect(self, comment_id):
        current_comment = Comment.query.get_or_404(comment_id)

        # Добавляем лайк
        current_comment.likes += 1

        db.session.commit()

    ## ДЗ ##
    # Изменить текст коментария


# Таблица хэштэгов
class Hashtag(db.Model):
    __tablename__ = 'hashtags'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    hash_name = db.Column(db.String, nullable=False, unique=True)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id', ondelete='SET NUll'))

    post = db.relationship('Post')


# Таблица паролей
class Password(db.Model):
    __tablename__ = 'passwords'
    password = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='SET NUll'))

    user = db.relationship('User')

    # Генерация пароля
    def set_password(self, password):
        self.password = generate_password_hash(password)

    # Проверка пароля на подлинность
    def check_password(self, password):
        return check_password_hash(self.password, password)


    ## ДЗ ##
    # Изменение пароля