from flask import Flask
# 可以用来指定 session 保存的位置
from flask.ext.session import Session
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.wtf import CSRFProtect
from redis import StrictRedis

from config import config

# 初始化数据库
db = SQLAlchemy()


def creat_app(config_name):
    app = Flask(__name__)
    # 加载配置
    app.config.from_object(config[config_name])
    # 通过app初始化
    db.init_app(app)
    # 初始化redis存储对象
    redise_store = StrictRedis(host=config[config_name].REDIS_HOST, port=config[config_name].REDIS_PORT)
    # 开启当前项目CSRF保护
    CSRFProtect(app)
    # 设置session保存指定位置
    Session(app)

    return app
