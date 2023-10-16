from flask import *
import json
import Database
app = Flask(__name__)

@app.route('/ratpartymix/dailysong',methods=["GET"])
def home_page():
    data_set = {'SpotifyID': Database.get_daily_song_database()}
    json_dump = json.dumps(data_set)
    return json_dump

if __name__ == '__main__':
    app.run(port=443)