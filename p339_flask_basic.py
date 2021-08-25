from flask import Flask
app = Flask(__name__)

@app.route("/") # 데코레이터
def hello():
    return "<h1>Hello, World!</h1>"

"""
$env:FLASK_APP="p339_flask_basic.py" # (환경) 변수를 설정(터미널 실행후 한 번만!)
flask run                            # flask 명령
"""