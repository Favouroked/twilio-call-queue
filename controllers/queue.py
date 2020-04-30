import os
from flask import Blueprint, jsonify
from twilio.rest import Client

queue = Blueprint('queue', __name__)

account_sid = os.getenv('ACCOUNT_SID')
auth_token = os.getenv('AUTH_TOKEN')
queue_sid = os.getenv('QUEUE_SID')


@queue.route('/details')
def queue_count():
    client = Client(account_sid, auth_token)
    q = client.queues(queue_sid).fetch()
    print(q)
    response = {
        'friendly_name': q.friendly_name,
        'current_size': q.current_size,
        'sid': q.sid
    }
    return jsonify(response)
