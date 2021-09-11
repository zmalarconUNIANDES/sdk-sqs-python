import logging
import boto3
from botocore.exceptions import ClientError
import json

# logger config
logger = logging.getLogger()
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s: %(levelname)s: %(message)s')

sqs = boto3.client('sqs', aws_access_key_id='AKIA6MXHEC2H7EF2KAF3', aws_secret_access_key='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', region_name='us-east-1')

def send_queue_message(queue_url, msg_attributes, msg_body):
    """
    Sends a message to the specified queue.
    """
    try:
        response = sqs.send_message(QueueUrl=queue_url,
                                    MessageAttributes=msg_attributes,
                                    MessageBody=msg_body)
    except ClientError:
        logger.exception(f'Could not send meessage to the - {queue_url}.')
        raise
    else:
        return response


def receive_queue_message(queue_url):
    """
    Retrieves one or more messages (up to 10), from the specified queue.
    """
    try:
        response = sqs.receive_message(QueueUrl=queue_url)
    except ClientError:
        logger.exception(
            f'Could not receive the message from the - {queue_url}.')
        raise
    else:
        return response


if __name__ == '__main__':
    # CONSTANTS
    QUEUE_URL = 'https://sqs.us-east-1.amazonaws.com/989400929935/sqs-msg-registrar-examenes'
    MSG_ATTRIBUTES = {
        'Title': {
            'DataType': 'String',
            'StringValue': 'Working with SQS in Python using Boto3'
        },
        'Author': {
            'DataType': 'String',
            'StringValue': 'Grupo 4'
        }
    }
    MSG_BODY = 'Learn how to create, receive, delete and modify SQS queues and see the other functions available within the AWS.'

    msg = send_queue_message(QUEUE_URL, MSG_ATTRIBUTES, MSG_BODY)

    json_msg = json.dumps(msg, indent=4)

    logger.info(f'''
        Message sent to the queue {QUEUE_URL}.
        Message attributes: \n{json_msg}''')
