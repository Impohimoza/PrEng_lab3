from flask import jsonify

class UsersRepositoryInMemory:
    
    def __init__(self):
        self.users = [
            {"id": 1, "name": "Alice", "age": 25},
            {"id": 2, "name": "Bob", "age": 30}
        ]

    def __len__(self):
        return len(self.users)

    def get_all(self):
        return jsonify(self.users)

    def add(self, new_user):
        self.users.append(new_user)

    def get(self, user_id):
        user = next((u for u in self.users if u["id"] == user_id), None)
        return user

    def update(self, user_id, data):
        user = next((u for u in self.users if u["id"] == user_id), None)
        if not user:
            raise ValueError("User not found")
        
        user["name"] = data.get("name", user["name"])
        user["age"] = data.get("age", user["age"])
        return user

    def delete(self, user_id):
        user = next((u for u in self.users if u["id"] == user_id), None)
        if not user:
            raise ValueError("User not found")            
        
        self.users = [u for u in self.users if u["id"] != user_id]