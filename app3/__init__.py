from flask import Blueprint

app3_bp = Blueprint('app3', __name__)

from app3.routes import *
