import os
from twilio.rest import Client

account_sid = os.getenv('ACCOUNT_SID')
auth_token = os.getenv('AUTH_TOKEN')


def main(queue_name):
    client = Client(account_sid, auth_token)
    queue = client.queues.create(friendly_name=queue_name)
    print(queue)


if __name__ == '__main__':
    name = 'customer-support'
    print(f'Creating Queue :> {name}')
    main(name)
