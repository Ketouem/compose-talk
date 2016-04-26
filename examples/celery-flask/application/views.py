from http import HTTPStatus as httplib

from flask import Blueprint, current_app, jsonify, request

from .tasks import add_together

main = Blueprint('main', __name__)


@main.route('/ping')
def ping():
    return "Pong !"

@main.route('/workers')
def workers():
    workers = current_app.celery.control.inspect().stats()
    # return jsonify({'workers': list(workers.keys())})
    # The above line causes a TypeError when there is no running workers
    return jsonify({'workers': list(workers.keys()) if workers else []})

@main.route('/worker/<worker_key>')
def worker(worker_key):
    workers = current_app.celery.control.inspect().stats() or {}
    worker = workers.get(worker_key)

    if worker is None:
        r = jsonify({'error': 'Worker \'{}\' not found'.format(worker_key)})
        r.status_code = httplib.NOT_FOUND
    else:
        r = jsonify(worker)
    return r

@main.route('/add', methods=['POST'])
def add():
    if request.headers.get('Content-Type') == 'application/json':
        a = request.json.get('a')
        b = request.json.get('b')
        result = add_together.delay(a, b)
        return str(result.wait())
