from redis import Redis
from rq import Queue

from jobs import broken_function

q = Queue(connection=Redis())
result = q.enqueue(broken_function, "Error within RQ job.")
