import os
from flask import Flask, jsonify
from flask_cors import CORS

from toldyou.models import ToldYou
## connection via mongodb.
from mongoengine import connect
database_url = os.environ.get("DATABASE_URL")
connect(host=database_url)

## Init app
app = Flask(__name__)
CORS(app)

@app.route('/')
def get_status():
  return {"status": "ok"}

@app.route('/toldyou')
def get_toldyou():
  return {"results": ToldYou.objects.to_json()} 


# Start the app
if __name__ == '__main__':
    app.run(debug=True)