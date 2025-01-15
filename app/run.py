from app.director import AppDirector

if __name__ == "__main__":
    director = AppDirector(config_name='development')
    director.initialize_database()  # Optionally initialize the database
    director.start_app()
