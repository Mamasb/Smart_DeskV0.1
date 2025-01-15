from app import create_app, celery
from celery import Celery

app = create_app()

# Ensure the app context is available for tasks
app.app_context().push()

# Define the Celery tasks here or import them from other modules
@celery.task
def example_task():
    """An example Celery task."""
    return "Task executed successfully!"
