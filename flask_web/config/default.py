# coding: utf-8
import os


class Config(object):
    RESULT_ERROR = 0
    RESULT_SUCCESS = 1
    JSON_AS_ASCII = False

    SITE_ROOT = "http://task.cocotask.com/"

    # 微信设置信息
    WECHAT_APPID = "wxf36645bdd574084f"
    WECHAT_SECRET = "8686910394a9cc112d9cf89ccfc6c8dc"
    WECHAT_MCH_ID = "1525943361"
    WECHAT_MCH_KEY = "c9a5241f1d9b1a21659f75cb0e3d82ba"
    WECHAT_AUTH_URL = "http://task.cocotask.com/wechat/authorized"
    WECHAT_ROOT = "http://task.cocotask.com/wechat"  # 微信根目录，结尾不带"/"

    MONGODB_SETTINGS = {'ALIAS': 'default',
                        'DB': 'jwt_test',
                        'host': 'localhost',
                        'username': 'admin',
                        'password': ''}

    """Base config class."""
    # Flask app config
    DEBUG = True
    TESTING = True

    SECRET_KEY = "\xb5\xb3}#\xb7A\xcac\x9d0\xb6\x0f\x80z\x97\x00\x1e\xc0\xb8+\xe9)\xf0}"

    # Root path of project
    PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

    # Site domain
    SITE_TITLE = "Cocotask管理平台"
    SITE_DOMAIN = "http://localhost:5000"

    BABEL_DEFAULT_LOCALE = 'zh_Hans_CN'

    SECURITY_PASSWORD_HASH = 'bcrypt'
    SECURITY_PASSWORD_SALT = 'izt'
    SECURITY_USER_IDENTITY_ATTRIBUTES = 'username'
    SECURITY_POST_LOGIN_VIEW = '/admin'
    SECURITY_POST_CHANGE_VIEW = '/admin'
    SECURITY_LOGIN_WITHOUT_CONFIRMATION = True
    SECURITY_CHANGEABLE = True
    SECURITY_SEND_PASSWORD_CHANGE_EMAIL = False

    SECURITY_MSG_DISABLED_ACCOUNT = ('账号已被禁用', 'error')
    SECURITY_MSG_INVALID_PASSWORD = ('密码错误', 'error')
    SECURITY_MSG_INVALID_REDIRECT = ('转向错误', 'error')
    SECURITY_MSG_LOGIN = ('请登录', 'error')
    SECURITY_MSG_LOGIN_EXPIRED = ('登录超时', 'error')
    SECURITY_MSG_PASSWORDLESS_LOGIN_SUCCESSFUL = ('无密码登录成功', 'error')
    SECURITY_MSG_PASSWORD_CHANGE = ('密码修改', 'error')
    SECURITY_MSG_PASSWORD_INVALID_LENGTH = ('密码不能少于6位', 'error')
    SECURITY_MSG_PASSWORD_IS_THE_SAME = ('密码和原密码相同', 'error')
    SECURITY_MSG_PASSWORD_MISMATCH = ('输入密码不匹配', 'error')
    SECURITY_MSG_PASSWORD_NOT_PROVIDED = ('密码不能为空', 'error')
    SECURITY_MSG_PASSWORD_NOT_SET = ('密码没有设置', 'error')
    SECURITY_MSG_PASSWORD_RESET = ('密码重置', 'error')
    SECURITY_MSG_PASSWORD_RESET_EXPIRED = ('密码重置过期', 'error')
    SECURITY_MSG_PASSWORD_RESET_REQUEST = ('密码重置请求', 'error')
    SECURITY_MSG_REFRESH = ('刷新', 'error')
    SECURITY_MSG_RETYPE_PASSWORD_MISMATCH = ('两次输入密码不匹配', 'error')
    SECURITY_MSG_UNAUTHORIZED = ('未授权', 'error')
    SECURITY_MSG_USER_DOES_NOT_EXIST = ('用户不存在', 'error')

    ROLES = {'SuperAdmin': '超级管理员',
             'CompanyAdmin': '公司管理员'
             }
