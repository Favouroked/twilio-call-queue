from flask import Blueprint
from twilio.twiml.voice_response import Dial, VoiceResponse

calls = Blueprint('calls', __name__)


@calls.route('/enqueue', methods=['GET', 'POST'])
def add_caller():
    response = VoiceResponse()
    response.say('Welcome to customer support, an agent will attend to you shortly.')
    response.enqueue('customer-support')

    print(response)

    return str(response)


@calls.route('/dequeue', methods=['GET', 'POST'])
def attend_to_caller():
    response = VoiceResponse()
    response.say('You are about to connect to a customer.')
    dial = Dial()
    dial.queue('customer-support')
    response.append(dial)

    print(response)

    return str(response)
