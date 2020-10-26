import sqlite3
from flask import Flask, jsonify, request

app = Flask(__name__)
app.debug = True

api_key = "RANDOM ACCESS KEY HERE"

def CheckAPIKey(key):
    if key == api_key:
        return True
    else:
        return False

@app.route('/')
def HomeDir():
    return jsonify({'msg': "invalid_endpoint"})

@app.route('/api/v1/hwid')
def HwidDir():
    db = sqlite3.connect('auth.db')
    c = db.cursor()
    opt = request.args.get('type')
    hwid = request.args.get('hwid')
    key = request.args.get('apikey')

    if opt == 'add':
        two_step = CheckAPIKey(key)
        if two_step == True:
            c.execute(f'INSERT INTO hwids VALUES ("{hwid}")')
            db.commit()
            return jsonify({'msg': "success"})
        if two_step == False:
            return jsonify({'msg': "invalid_apikey"})

    if opt == 'check':
        c.execute(f"SELECT * FROM hwids WHERE hwid='{hwid}'")
        if hwid in str(c.fetchall()):
            return jsonify({'msg': "success"})
        else:
            return jsonify({'msg': "invalid_hwid"})

    else:
        return jsonify({'msg': "invalid_type"})

if __name__ == "__main__":
    app.run()