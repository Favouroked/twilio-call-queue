from flask import Flask

from controllers.calls import calls
from controllers.queue import queue

app = Flask(__name__)

app.register_blueprint(calls, url_prefix='/calls')
app.register_blueprint(queue, url_prefix='/queue')

if __name__ == '__main__':
    app.run()
