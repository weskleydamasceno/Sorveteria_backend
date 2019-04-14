from flask import Flask
from app import app, db, login_manager
from app.models.tables import Usuario

# Load the user
@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(user_id)