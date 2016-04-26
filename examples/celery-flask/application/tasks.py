import os
import time

from . import create_app

app = create_app(
    config_name=os.getenv('COMPOSE_TALK_CONF', default='default'),
    register_blueprint=False
)

celery = app.celery

@celery.task()
def add_together(a, b):
    return a + b
