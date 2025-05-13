from flask import Blueprint

app1_bp = Blueprint('app1', __name__)

from app1.routes import *
