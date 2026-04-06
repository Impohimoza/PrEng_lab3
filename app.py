from flask import Flask, request, jsonify

app = Flask(__name__)

# Простая база данных в памяти
users = [
    {"id": 1, "name": "Alice", "age": 25},
    {"id": 2, "name": "Bob", "age": 30}
]

# GET - получить всех пользователей
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# GET - получить одного пользователя
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

# POST - создать пользователя
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    new_user = {
        "id": len(users) + 1,
        "name": data.get("name"),
        "age": data.get("age")
    }
    users.append(new_user)
    return jsonify(new_user), 201

# PUT - обновить пользователя
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    data = request.get_json()
    user["name"] = data.get("name", user["name"])
    user["age"] = data.get("age", user["age"])
    return jsonify(user)

# DELETE - удалить пользователя
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    user = next((u for u in users if u["id"] == user_id), None)
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    users = [u for u in users if u["id"] != user_id]
    return jsonify({"message": "User deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)