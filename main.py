from flask import Flask
app=Flask(__name__)
@app.route('/')
    return("Hello WOrld")

@app.route('/arya')
def hello_anish():
    return("Hi Aryaman")

    app.run(port=5000,debug="True")