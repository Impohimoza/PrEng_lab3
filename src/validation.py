def validate_user(data):
    """
    Проверка корректности данных пользователя
    
    :param data: данные пользователя
    :return: Результат валидации
    """
    if not data.get("name"):
        return False, "Name is required"
    if not isinstance(data.get("name"), str):
        return False, "Name must be string"
    if not data.get("age"):
        return False, "Age is required"
    if not isinstance(data.get("age"), int):
        return False, "Age must be number"
    return True, "OK"