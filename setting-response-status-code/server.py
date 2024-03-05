from flask import Flask, make_response

app=Flask(__name__)


# We can set status code through touples
@app.route('/one-way')
def one_way():
    return ({"message": "First Way is through touples"}, 200)


# We can also set response through make_response() method
@app.route("/another-way")
def another_way():
    return make_response("Resourse not Found", 400)