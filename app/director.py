from app import create_app, celery
from app.models import db  # Assuming SQLAlchemy is being used for ORM

class AppDirector:
    """Director class to orchestrate app-level activities."""

    def __init__(self, config_name):
        """Initialize the app director."""
        self.app = create_app(config_name)
        self.celery = celery

    def initialize_database(self):
        """Initialize the database."""
        with self.app.app_context():
            db.create_all()
            print("Database initialized successfully.")

    def run_celery_task(self, task_name, *args, **kwargs):
        """
        Run a Celery task by name.

        Args:
            task_name (str): The task's full name (e.g., 'app.celery_worker.example_task').
            *args: Positional arguments for the task.
            **kwargs: Keyword arguments for the task.
        """
        task = self.celery.signature(task_name)
        result = task.apply_async(args=args, kwargs=kwargs)
        return result

    def start_app(self):
        """Run the Flask application."""
        self.app.run(
            host=self.app.config.get('HOST', '127.0.0.1'),
            port=self.app.config.get('PORT', 5000),
            debug=self.app.config.get('DEBUG', True)
        )
