from redis import StrictRedis


class Config(object):
    """项目的配置"""
    DEBUG = True

    SECRET_KEY = 'y1f1dJFwD3TGRhQKmljeT1/dSWwS57h+GvbLtBmLukIoLiqLfU3P92nyVZI0V1p6'

    # 为数据库添加配置
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/information"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Redis的配置
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379

    # session的配置信息
    SESSION_TYPE = "redis"  # 指定 session 保存到 redis 中
    # 让 cookie 中的 session_id 被加密签名处理
    SESSION_USE_SIGNER = True
    # 设置需要过期
    SESSION_PERMANENT = False
    # 使用 redis 的实例
    SESSION_REDIS = StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    # session 的有效期，单位是秒
    PERMANENT_SESSION_LIFETIME = 86400 * 2
