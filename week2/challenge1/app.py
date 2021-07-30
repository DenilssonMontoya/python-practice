from flask import Flask
from flask import request

app = Flask(__name__)

departments = {
    "ok": True,
    "content": ["Lima", "Callao", "Arequipa"],
    "message" : "List of departments"
}

@app.route('/ping')
def test():
    return 'Pong'

# Get all users
@app.route('/departments.json', methods=['GET'])
def getDepartments():
    return departments   

if __name__ == '__main__':
    app.run()    