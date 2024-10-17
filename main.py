from flask import *

from public import public
from admin import admin
from shop import shop
from user import user
from api import api


app=Flask(__name__)


app.secret_key="abcdf"


app.register_blueprint(public)
app.register_blueprint(admin)
app.register_blueprint(shop)
app.register_blueprint(user)
app.register_blueprint(api)


app.run(debug=True,port=5013,host="0.0.0.0")