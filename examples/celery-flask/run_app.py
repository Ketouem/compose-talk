import os

from application import create_app

app = create_app(os.getenv('COMPOSE_TALK_CONF', default='default'))

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
