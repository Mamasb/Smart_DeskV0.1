from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from celery import Celery
from config import Config

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()
celery = Celery(__name__)

def create_app(config_class=Config):
    """Factory function to create and configure the Flask app."""
    app = Flask(__name__)
    app.config.from_object(config_class)  # Ensure correct config is loaded

    # Initialize extensions with the app
    db.init_app(app)
    migrate.init_app(app, db)

    # Celery initialization after app config is set
    celery.config_from_object(config_class)

    # Register blueprints
    from app.routes import (
        accountant_routes,
        director_routes,
        expense_routes,
        fees_routes,
        invoice_routes,
        main_routes,
        payroll_routes,
        school_fee_routes,
        secretary_routes,
        students_routes,  # Ensure this is the correct import
    )

    # Registering the blueprints
    app.register_blueprint(accountant_routes.bp)
    app.register_blueprint(director_routes.bp)
    app.register_blueprint(expense_routes.bp)
    app.register_blueprint(fees_routes.bp)
    app.register_blueprint(invoice_routes.bp)
    app.register_blueprint(main_routes.bp)
    app.register_blueprint(payroll_routes.bp)
    app.register_blueprint(school_fee_routes.bp)
    app.register_blueprint(secretary_routes.bp)
    app.register_blueprint(students_routes.bp)  # Register students blueprint

    return app
