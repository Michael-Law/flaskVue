from flask import Flask, jsonify
from flask import Flask, render_template, url_for, copy_current_request_context
from random import random
from time import sleep
from threading import Thread, Event
import threading
from flask_cors import CORS
import pandas as pd
from sqlalchemy import create_engine
import cx_Oracle
import jsonpickle
from modelizer import serialise_blend
from modelizer import serialise_dye
from modelizer import Object


app = Flask(__name__)
app.config.from_object(__name__)

oracle_connection_string = 'oracle+cx_oracle://{username}:{password}@{hostname}:{port}/{database}'

SQLALCHEMY_TRACK_MODIFICATIONS = True

engine = create_engine(
    oracle_connection_string.format(
        username='woolodbc',
        password='ferney77',
        hostname='192.168.1.219',
        port='1535',
        database='SPWDB',
    )
)


# configuration
DEBUG = True

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# sanity check route
@app.route('/ping', methods=['GET'])
def connect():  
    def process():
        n = 0
        while n > 1:
            time.sleep(5)
        return serialise_blend(engine)

    return jsonpickle.encode(process(), unpicklable= False,keys=True)
    
@app.route('/ding',methods = ['GET'])
def test():
    def process():
        n = 0
        while n > 1:
            time.sleep(5)
    return jsonify(serialise_dye(engine))

if __name__ == '__main__':
    app.debug = True
    app.run()
    app.run(debug = True)
