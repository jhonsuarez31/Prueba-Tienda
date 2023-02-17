from flask import jsonify
from app.core.db.session import db_session
from app.models.user import User
from app.models.token_blocklist import TokenBlocklist
from flask import abort as flask_abort
from app.core.security import generate_password_hash, verify_password
from flask_jwt_extended import create_access_token
from app.core.data import ACCESS_TOKEN_EXPIRE_MINUTES

#Get user by id
def get_by_id (id, abort=False):
    user = db_session.query(User).filter_by(id=id).first()
    if user is None and abort:
        flask_abort(404, f'El usuario  no existe en el sistema.')
    return user

#Get user by id
def get_by_email (email, abort=False):
    user = db_session.query(User).filter_by(email=email).first()
    if user is None and abort:
        flask_abort(404, f'El usuario  no existe en el sistema.')
    return user
#Get all user

def get_all_users():
    users = db_session.query(User).all()
    return users

def create(name, email, password, role_id ):
    user = User(
        name=name,
        email=email,
        password= generate_password_hash(password),
        role_id=role_id,
    )

    db_session.add(user)
    db_session.commit()
    return jsonify ({
        'msg': 'usuario creado con extito'
    })

#login
def get_access_token(user, password, token_type='Bearer'):
    if not verify_password(password, user.password):
        flask_abort(403, f'No es posible iniciar sesion revisa tus credenciales.')
    return {
        "access_token": create_access_token(
            identity=user.id,
            expires_delta=ACCESS_TOKEN_EXPIRE_MINUTES
        ),
        "token_type": token_type
    }


def logout(
    jti_access_token
):
    db_session.add(
        TokenBlocklist(
            jti=jti_access_token

        )
    )
    db_session.commit()
    return jsonify(msg="La sesion se ha cerrado.")

