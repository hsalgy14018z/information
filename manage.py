from flask import session
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from info import creat_app, db


# 通过指定的配置名字创建对应的app,
app = creat_app('development')
manager = Manager(app)
# 将 app 与 db 关联
Migrate(app, db)
# 将迁移命令添加到manager中
manager.add_command('db', MigrateCommand)


@app.route('/')
def index():
    session["name"] = "xiaomi"
    return 'index'


if __name__ == '__main__':
    manager.run()
