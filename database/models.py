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
    phone_number = db.Column(db.String, nullable=False, unique=True)
    about = db.Column(db.String, nullable=True)

    # Создать пользователя
    def registration(self, username, first_name, last_name, email, phone_number, about):
        new_user = User(username=username, first_name=first_name, last_name=last_name,
                        email=email, phone_number=phone_number, about=about)

        db.session.add(new_user)
        db.session.commit()

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
    def change_header(self, post_id, new_header):
        current_post = Post.query.get_or_404(post_id)

        if current_post.header == new_header:
            return 'В новом заголовке нет никаких изменений'

        current_post.header = new_header

        db.session.commit()

    # Удалить пост
    def delete_post(self, post_id):
        current_post = Post.query.get_or_404(post_id)

        db.session.delete(current_post)
        db.session.commit()

    # Счетчик лайков
    def post_likes_increment(self, post_id):
        current_post = Post.query.get_or_404(post_id)

        # Добавляем лайк
        current_post.post_likes += 1

        db.session.commit()


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
    def change_comment_text(self, comment_id, new_text):
        current_comment = Comment.query.get_or_404(comment_id)

        # Изменяем текст коментария
        current_comment.text = new_text

        db.session.commit()


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
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='SET NUll'), primary_key=True)

    user = db.relationship('User')

    # Генерация пароля
    def set_password(self, password):
        self.password = generate_password_hash(password)

    # Проверка пароля на подлинность
    def check_password(self, password):
        return check_password_hash(self.password, password)

    ## ДЗ ##
    # Изменение пароля
    def change_password(self, user_id, new_password):
        user_password = Password.query.get_or_404(user_id)

        # Меняем описание
        if user_password.password == new_password:
            return 'Новый пароль должен отличаться от старого'

        user_password.about = new_password

        db.session.commit()


