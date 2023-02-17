from app.main import app
from app.core.data import SQLALCHEMY_MYSQL_URI
from app.core.data import JWT_SECRET_KEY


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:3138533232@mydb1:3306/tienda'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config["JWT_SECRET_KEY"] = JWT_SECRET_KEY
