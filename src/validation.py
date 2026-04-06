def validate_user(data: dict[str, any]) -> tuple[bool, str]:
    """Проверка корректности данных пользователя

    Args:
        data (dict[str, any]): данные пользователя

    Returns:
        tuple[bool, str]: Результат валидации
    """
    if not data.get("name"):
        return False, "Name is required"
    if not isinstance(data.get("name"), str):
        return False, "Name must be string"
    if not data.get("age"):
        return False, "Age is required"
    if not isinstance(data.get("age"), int):
        return False, "Age must be number"
    if data.get("age") < 0 or data.get("age") > 150:
        return False, "Age must be between 0 and 150"
    return True, "OK"