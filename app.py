from flask import Flask
import os


app = Flask(__name__)
POD_NAME = os.environ.get("HOSTNAME")


@app.route("/")
def hello():
    return f'''<body style="text-align:center;">
               <p style="color:lightgray; margin-top:40px;">- pypod-helloworld -</p>\n
               <h1>Hello World!</h1>\n
               <h2>Pod: <span style="color:gray;">{POD_NAME}</span></h2>
               </body>'''               


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')
