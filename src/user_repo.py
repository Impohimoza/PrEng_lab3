from flask import jsonify

class UsersRepositoryInMemory:
    """
    Класс, реализующий паттерн Repository над сущностью User. 
    Предоставляет функциональность коллекции.
    
    Attributes:
        users (list): Коллекция объектов User
    """
    def __init__(self):
        self.users = [
            {"id": 1, "name": "Alice", "age": 25},
            {"id": 2, "name": "Bob", "age": 30}
        ]

    def __len__(self):
        return len(self.users)

    def get_all(self):
        """
        Функция возвращает json всех пользователей
        
        :return: json объект
        """            
        return self.users

    def add(self, new_user):
        """
        Функция добавляет новый объект пользователя в коллекцию
        
        :param new_user: объект нового пользовотеля
        """           
        self.users.append(new_user)

    def get(self, user_id):
        """
        Функция возвращает объект пользователя по айди
        
        :param user_id: айди пользователя
        :return: объект пользователя
        """                
        user = next((u for u in self.users if u["id"] == user_id), None)
        return user

    def update(self, user_id, data):
        """
        Функция обновляет атрибуты пользователя
        
        :param user_id: айди пользователя
        :return: user обновлённый объект пользователя     
        """           
        user = next((u for u in self.users if u["id"] == user_id), None)
        if not user:
            raise ValueError("User not found")
        
        user["name"] = data.get("name", user["name"])
        user["age"] = data.get("age", user["age"])
        return user

    def delete(self, user_id):
        """
        Функция удаляет пользователя по айди
        
        :param user_id: айди пользователя  
        """            
        user = next((u for u in self.users if u["id"] == user_id), None)
        if not user:
            raise ValueError("User not found")            
        
        self.users = [u for u in self.users if u["id"] != user_id]