

from flask import jsonify
from crypt import methods
from flask import abort
from app.schema.user import UserSchema
from app.schema.token import TokenSchema
# import provaiders
from app.provedores import provaider_user

from webargs import fields
from flask_apispec import use_kwargs
from flask_apispec import marshal_with
from flask_apispec import doc
from app.api.v1.api_docs import docs
from app.main import app
from flask import redirect, request
from flask import jsonify


@docs.register
@doc(
    description='Crear un usario',
    tags=['users'])
@app.route('/v1/registryUser', methods=['POST'])
@use_kwargs({
    'name': fields.String(requered=True),
    'email': fields.Email(required=True),
    'password': fields.String(required=True),
    'role_id': fields.Integer(required=True),
})
@marshal_with(UserSchema())
def users_post(
    email, password, role_id, name
):

    user = (provaider_user.get_by_email(email=email))

    if user:
        abort(400, f"Ya existe un  usuario con este email.")
    user = provaider_user.create(
        name=name, email=email, password=password, role_id=role_id)
    return user





@docs.register
@doc(
    description='Hacer login',
    tags=['users'])
@app.route('/v1/users/login/', methods=['POST'])
@use_kwargs({
    'email': fields.Email(required=True),
    'password': fields.String(required=True)
})
@marshal_with(TokenSchema())
def login_post(email, password):
    user =     user = (provaider_user.get_by_email(email=email))
    if user is None:
        abort(403, f'No es posible iniciar sesion revisa tus credenciales')
    respuesta = provaider_user.get_access_token(user=user, password=password)

    return respuesta