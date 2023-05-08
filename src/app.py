from flask import Flask, jsonify
import json
from flask import request
app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]


@app.route('/blabla', methods=['GET'])
def hello_world():
    return 'Hello, World!'

@app.route('/todos', methods=['GET'])
def get_todos():
   return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data
    todo = json.loads(request_body)
    todos.append(todo)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.pop(position - 1)
    return jsonify(todos)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)