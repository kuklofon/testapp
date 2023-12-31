from flask import Flask, jsonify
import os
import uuid

app = Flask(__name__)

@app.route('/hostname', methods=['GET'])
def get_hostname():
    hostname = os.uname().nodename
    return jsonify({'hostname': hostname})

@app.route('/author', methods=['GET'])
def get_author():
    author = os.environ.get('AUTHOR', 'Yuri Makarov')
    return jsonify({'author': author})

@app.route('/id', methods=['GET'])
def get_id():
    uuid_str = os.environ.get('UUID', str(uuid.uuid4()))
    return jsonify({'id': uuid_str})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

