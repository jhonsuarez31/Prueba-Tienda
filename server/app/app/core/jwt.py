from re import sub
from flask_jwt_extended import JWTManager

from ..main import app
from app.providers import users_providers
from app.providers import TokenBlocklist_provider
# Setup the Flask-JWT-Extended extension

from flask import jsonify
jwt = JWTManager(app)


@jwt.user_lookup_loader
def get_current_user(identity, jwtpayload):
    return users_providers.get_by_id(id=jwtpayload['sub'])


@jwt.token_in_blocklist_loader
def check_if_token_revoked(jwt_header, jwt_payload):
    jti = jwt_payload["jti"]
    return TokenBlocklist_provider.get_by_jti(jti=jti)


@jwt.revoked_token_loader
def revoked_token_response(jwt_header, jwt_payload):
    return jsonify({
        'error': "Error en la autenticacion.",
        'error_detail':"Lo sentimos, la sesion se ha cerrado."
    }),401

@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    return jsonify({
        'error': "Error en la autenticacion.",
        'error_detail':"El token de autenticación ha expirado."
    }),401

@jwt.unauthorized_loader
def unauthorized_loader_callback(msg):
    return jsonify({
        'error': "Error en la autenticacion.",
        'error_detail':"Token de autenticación no encontrado."
    }),401


@jwt.invalid_token_loader
def invalid_token_loader_callback(msg):
    return jsonify({
        'error': "Error en la autenticacion.",
        'error_detail':"Token inválido."
    }),401    
