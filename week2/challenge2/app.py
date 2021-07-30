from flask import Flask
from flask import request

app = Flask(__name__)


students = {}

@app.route('/ping')
def test():
    return 'Pong'

# Add student
@app.route('/student', methods=['POST'])
def add_student():
    data = request.json
    students[data["id"]] = {
        "firstName": data["firstName"],
        "lastName": data["lastName"],
        "age": data["age"]
        }
    return 'OK', 201

# get all student
@app.route('/student.json')
def get_students():
    return students

if __name__ == '__main__':
    app.run()    