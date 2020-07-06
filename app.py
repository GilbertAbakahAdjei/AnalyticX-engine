from flask import Flask
from flask_cors import CORS

from app_modules.base import router as base_blueprint
from mongo_converters import ObjectIdConverter

app = Flask(__name__)
CORS(app, supports_credentials=True)
app.config['DEBUG'] = True
app.url_map.converters['ObjectId'] = ObjectIdConverter


app.register_blueprint(base_blueprint,  user_prefix='/')

if __name__ == '__main__':
    app.run()

