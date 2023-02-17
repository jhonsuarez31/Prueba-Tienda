from passlib.context import CryptContext

pwd_contex = CryptContext(schemes=["bcrypt"], deprecated="auto")


def generate_password_hash(password):
    return pwd_contex.hash(password)


def verify_password(password_plain, hash_password):
    return pwd_contex.verify(password_plain, hash_password)
