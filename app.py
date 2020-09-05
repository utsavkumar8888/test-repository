# In this lesson we are creating authtication for that we need to install 
# flask jwt.< pip install 
# (REST_section4) C:\Users\utsavk\Desktop\REST_section4>pip install Flask-JWT
# flask-JWT is flask Jeson Web Token. 


from flask import Flask
from flask_restful import Api
from flask_jwt import JWT 
from security import authenticate,identity
from resources.user import UserRegister
from resources.item import Item , Itemlist
from resources.store import Store, StoreList 


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.secret_key = 'jose'
api = Api(app)

@app.before_first_request
def create_tables():
	db.create_all()




 
jwt = JWT(app,authenticate,identity)             # this will create a "/auth" endpoints 



api.add_resource(Item , '/item/<string:name>') 
api.add_resource(Itemlist , '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(Store,'/store/<string:name>')
api.add_resource(StoreList , '/stores')


if __name__ == "__main__":
	from db import db
	db.init_app(app)
	app.run(port=5000,debug=True)



