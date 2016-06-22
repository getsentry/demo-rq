import os

from rq import Connection, Worker, Queue
from raven import Client
from raven.transport.http import HTTPTransport
from rq.contrib.sentry import register_sentry

client = Client(os.environ['SENTRY_DSN'], transport=HTTPTransport)

with Connection():
	worker = Worker(map(Queue, ['default']))
	register_sentry(client, worker)
	worker.work()
