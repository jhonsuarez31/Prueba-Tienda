from app.providers import pr

from webargs import fields
from flask_apispec import use_kwargs
from flask_apispec import marshal_with
from flask_apispec import doc
from app.api.v1.api_docs import docs
from app.main import app
from flask import redirect, request
from flask import jsonify

@app.route('/producto/<int:producto_id>')
def addNewProduct():
    return 'Hola'

@app.route('/carrito/agregar/<int:producto_id>')
def deleteOneProduct():
    return