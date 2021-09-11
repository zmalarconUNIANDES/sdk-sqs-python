from celery.schedules import crontab
import boto3
from app import celery

sqs = boto3.client('sqs', aws_access_key_id='AKIA6MXHEC2H7EF2KAF3', aws_secret_access_key='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', region_name='us-east-1')

@celery.task(bind=True, name='remind_appointment')
def remind_appointment(args):
    response = sqs.send_message(QueueUrl='https://sqs.us-east-1.amazonaws.com/989400929935/sqs-msg-registrar-examenes',
                MessageBody='Learn how to create, receive, delete and modify SQS queues and see the other functions available within the AWS.')
    print(response)

@celery.task(bind=True, name='register_results')
def send_email(args):
    print("Enviar mensaje....")


celery.conf.beat_schedule = {
    'appointment reminder in every 60 seconds': {
        'task': 'remind_appointment',
        'schedule': 60.0
    },
    'send email every 1 hours': {
        'task': 'register_results',
        'schedule': crontab(minute='1')
    }
}