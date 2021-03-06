from flask import Flask
from flask_cors import CORS, cross_origin
from .config import app_config
from .models import db
from .views.ServiceView import service_api as service_blueprint
import psycopg2
def create_app(env_name):
    # Create app
    # app initialization
    app = Flask(__name__)
    # CORS(app, origins=["https://web.postman.co"])
    # CORS(app)
    app.config.from_object(app_config[env_name])
    db.init_app(app)
    app.register_blueprint(service_blueprint, url_prefix="/api/v1/services")
    @app.route("/", methods=["GET"])
    # @cross_origin(origins=["https://web.postman.co"])
    # @cross_origin()
    def index():
        # example endpoint
        # establishing the connection
        conn = psycopg2.connect(database="mechanic", user="postgres", password="Rao1Samyan", host="127.0.0.1", port="5432")
        # Setting auto commit false
        conn.autocommit = False
        # Creating a cursor object using the cursor() method
        cursor = conn.cursor()
        # Retrieving data
        cursor.execute("SELECT * from SERVICES")
        # Fetching 1st row from the table
        result = cursor.fetchone()
        print(result)
        # Fetching 1st row from the table
        cursor.execute("SELECT * from SERVICES")
        result = cursor.fetchall()
        print(result)
        # Commit your changes in the database
        conn.commit()
        # Closing the connection
        conn.close()
        return result[0][1]+" "+result[0][2]+" "+result[0][3]+" "+result[0][4]+" "+result[1][1]+" "+result[1][2]+" "+result[1][3]+" "+result[1][4]
    return app