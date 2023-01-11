from flask import Flask, jsonify, request
import json

app = Flask(__name__)

with open("data.json") as f:
    data = json.loads(f.read())


@app.route('/api/v1.0/todos', methods=['GET'])
def get_todo():
    return jsonify({"todos": data})
# eg.: http://localhost:5000/api/v1.0/todos


@app.route('/api/v1.0/todos/<todo>', methods=['GET'])
def get_todo_id(todo):
    task = [data for data in data if data['task'] == todo]
    return jsonify({"todo": task[0]})
# eg.: http://localhost:5000/api/v1.0/todos/dinner


@app.route('/api/v1.0/todos', methods=['POST'])
def add_todo():
    for element in request.json:
        todo = {'task': element["task"], 'complete': False}
        data.append(todo)
    with open("data.json", "w") as f:
        json.dump(data, f)
    return jsonify({"todos": data})
# eg.: http://localhost:5000/api/v1.0/todos
# [
#     {
#         "task":"dinner"
#     },
#     {
#         "task": "python project"
#     }
# ]


@app.route('/api/v1.0/todos/<todo>', methods=['PUT'])
def put_todo(todo):
    task = [data for data in data if data['task'] == todo]
    task[0]['complete'] = request.json['complete']
    with open("data.json", "w") as f:
        json.dump(data, f)
    return jsonify({"todo": task[0]})
# eg.: http://localhost:5000/api/v1.0/todos/dinner
# {"complete" : true}


@app.route('/api/v1.0/todos/<todo>', methods=['DELETE'])
def delete_todo(todo):
    task = [data for data in data if data['task'] == todo]
    data.remove(task[0])
    with open("data.json", "w") as f:
        json.dump(data, f)
    return jsonify({"todos": data})
# eg.: http://localhost:5000/api/v1.0/todos/dinner


app.run()
