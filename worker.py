import os

from rq import Connection, Worker, Queue
import sentry_sdk
from sentry_sdk.integrations.rq import RqIntegration

sentry_sdk.init(os.environ['SENTRY_DSN'], integrations=[RqIntegration()])

with Connection():
	worker = Worker(map(Queue, ['default']))
	worker.work()
