import os


class Config:

    CELERY_BROKER_URL = None
    CELERY_RESULT_BACKEND = None


class ComposeConfig(Config):

    CELERY_BROKER_URL = "amqp://{}:{}@celery-broker:5672".format(
        os.getenv('CELERY_USER'), os.getenv('CELERY_PASSWORD')
    )
    CELERY_RESULT_BACKEND = "redis://celery-result-backend:6379"

config = {
    'default': Config,
    'compose': ComposeConfig
}
