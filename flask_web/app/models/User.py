from werkzeug.security import generate_password_hash, check_password_hash

from flask_web.app.models import db

import datetime


class Permission(db.Document):
    url = db.StringField(max_length=255, required=True, unique=True)
    name = db.StringField(max_length=80)
    description = db.StringField(max_length=255)

    def __str__(self):
        return self.description

    def __unicode__(self):
        return self.description


# 用户管理model
class User(db.Document):
    username = db.StringField(max_length=255, verbose_name='用户名称', required=True, unique=True)
    _password = db.StringField(max_length=255, verbose_name='用户密码')
    active = db.BooleanField(default=True, verbose_name='当前账户是否激活')

    create_time = db.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')

    roles = db.ListField(db.ReferenceField(Permission), default=[])

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, passwd):
        self._password = generate_password_hash(passwd)

    def check_password(self, raw):
        return check_password_hash(self._password, raw)

    def __unicode__(self):
        return str(self.username)


if __name__ == '__main__':
    from flask_web.app.models import db

    user = User("haha")
    print(user.username)
    user._password = "hehe"
    user.password = "xixi"
    print(user.password)
