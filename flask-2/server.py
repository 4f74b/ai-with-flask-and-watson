from flask import Flask, jsonify
app=Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify(message='hello world',name='Aftab',profession={'MERN Stack Developer': '1 Year', 'Farigh': '3 Years'})