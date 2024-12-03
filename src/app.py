from flask import Flask, jsonify, request
app = Flask(__name__)


todos = [ { "label": "Aprender Flask", "done": False } ]



@app.route('/todos', methods=['GET'])
def hello_world():
  todos_json = jsonify(todos)
  return todos_json, 200

@app.route('/todos', methods=['POST'])
def add_new_todo():
  body = request.json
  todos.append(body) # AGREGA UN NUEVO ELEMENTO A LA LISTA
  todos_actualizado = jsonify(todos) 
  return todos_actualizado, 200

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
  todos.remove(todos[position])
  todos_actualizado = jsonify(todos) 
  return todos_actualizado, 200
  




# Estas dos líneas siempre deben estar al final de tu archivo app.py

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)