from flask import Flask, request, jsonify

from src.user_repo import UsersRepositoryInMemory
from src.validation import validate_user

app = Flask(__name__)

# Простая база данных в памяти
user_repo = UsersRepositoryInMemory()

# GET - получить всех пользователей
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(user_repo.get_all())

# GET - получить одного пользователя
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = user_repo.get(user_id)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

# POST - создать пользователя
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    is_valid, message = validate_user(data)
    if not is_valid:
        return jsonify({"error": message}), 400
    
    new_user = {
        "id": len(len(user_repo)) + 1,
        "name": data.get("name"),
        "age": data.get("age")
    }
    user_repo.add(new_user)
    return jsonify(new_user), 201

# PUT - обновить пользователя
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = user_repo.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    data = request.get_json()
    is_valid, message = validate_user(data)
    if not is_valid:
        return jsonify({"error": message}), 400
    updated_user = user_repo.update(user_id=user_id, data=data)
    return jsonify(updated_user)

# DELETE - удалить пользователя
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = user_repo.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    user_repo.delete(user_id)
    return jsonify({"message": "User deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)