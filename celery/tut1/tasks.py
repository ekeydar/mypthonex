from celery import Celery

app = Celery('tasks',
		broker='amqp://localhost//',
		backend='amqp://localhost')

@app.task
def add(x, y):
	if x == y:
		raise Exception('should not be equal')
	return x + y

	


