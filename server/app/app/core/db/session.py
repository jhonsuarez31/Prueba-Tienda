# Flask

from flask_sqlalchemy import SQLAlchemy

# sqlalchemy


from app.main import app
from app.core.db.base import Base


db = SQLAlchemy(app, model_class=Base)
db_session = db.session
