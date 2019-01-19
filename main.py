from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>

    </head>
    <body>
    
        <form action="/web-caesar" method='POST'>
        <lable for="rot">Rotate by:</lable>
        <input id="rot" type="text" value "" name="rot" />
        
        <lable for="textarea"></lable>
        <textarea id="textarea" value "0" name="text">
        </textarea>

        <button type="submit">Submit Query</button>
        </form>
    </body>
</html>
"""
@app.route("/")
def index():
    return form

@app.route("/web-caesar", methods=['POST'])
def encrypt():
    text1 = request.form ['text']
    rotate = request.form ['rot']
    
    encrypt1 = rotate_string(rotate, text1)
    return '<h1>' + encrypt1 + '</h1>'

app.run()
