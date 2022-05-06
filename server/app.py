from flask import Flask, jsonify
from toldyou.models import ToldYou
## connection via mongodb.
from mongoengine import connect
connect(host="mongodb://127.0.0.1:27017/toldyou")

## Init app

app = Flask(__name__)


@app.route('/toldyou')
def get_toldyou():
  return ToldYou.objects.to_json()


# Start the app
if __name__ == '__main__':
    app.run(debug=True)