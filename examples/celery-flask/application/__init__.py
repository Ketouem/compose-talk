from celery import Celery
from flask import Flask

from .config import config

celery = None


def create_app(config_name='default', register_blueprint=True):
    app = Flask("compose-talk-web")
    app.config.from_object(config[config_name])

    if register_blueprint:
        from .views import main as blueprint
        app.register_blueprint(blueprint)

    global celery
    celery = make_celery(app)

    app.celery = celery
    print("Application prepared with configuration '{}'".format(config_name))
    return app


def make_celery(app):
    celery = Celery(
        app.import_name,
        broker=app.config['CELERY_BROKER_URL'],
    )
    celery.conf.update(app.config)

    TaskBase = celery.Task

    class ContextTask(TaskBase):

        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery.Task = ContextTask
    return celery
