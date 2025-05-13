from flask import Blueprint

app2_bp = Blueprint('app2', __name__)

from app2.routes import *
