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


class Role(db.Document):
    name = db.StringField(max_length=255, required=True, unique=True)
    description = db.StringField(max_length=255)
    permissions = db.ListField(db.ReferenceField(Permission), default=[])

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

    roles = db.ListField(db.ReferenceField(Role), default=[])

    # 给这个用户增加角色
    def add_role(self, role_names: list):
        for role_name in role_names:
            role = Role.objects(name=role_name).first()
            if not role:
                role = Role(name=role_name)
                role.save()
            self.roles.append(role)
        self.roles = list(set(self.roles))

    @staticmethod
    def register(username, password):
        new_user = User(username=username, _password=generate_password_hash(password))
        new_user.add_role(['everyone'])
        new_user.save()
        return new_user

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
