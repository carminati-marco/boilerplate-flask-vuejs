from flask import Flask, jsonify
from flask_cors import CORS

# from toldyou.models import ToldYou
# ## connection via mongodb.
# from mongoengine import connect
# connect(host="mongodb://127.0.0.1:27017/toldyou")

## Init app

app = Flask(__name__)
CORS(app)

@app.route('/')
def get_status():
  return {"status": "ok"}

@app.route('/toldyou')
def get_toldyou():
  return {"results":"[{\"_id\": {\"$oid\": \"6274f219d391ef6e993799d8\"}, \"name\": \"test\", \"users\": []}]"}
  # return {"results": ToldYou.objects.to_json()} 


# Start the app
if __name__ == '__main__':
    app.run(debug=True)