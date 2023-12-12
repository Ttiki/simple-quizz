class Config(object):
    """
    Common configurations
    """

class DevelopmentConfig(Config):
    """
    Development configurations
    """
    DEBUG = True
    MONGO_DBNAME = 'dev_db'
    MONGO_URI = 'mongodb://localhost:27017/dev_db'

class ProductionConfig(Config):
    """
    Production configurations
    """
    DEBUG = False
    MONGO_DBNAME = 'prod_db'
    MONGO_URI = 'mongodb://mongo:27017/prod_db'

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
