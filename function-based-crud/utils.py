"""
файл с допольнительными функциями

"""

def generate_id(ids):
    """
    Принимает список существующих id
    Возвращает новое id в диапазоне от 100 до 1000
    """
    import random
    id_ = random.randint(100, 1000)
    while id_ in ids:
        id_ = random.randint(100, 1000)
    return id_

def validate_password(p1,p2):
    if p1 != p2:
        raise Exception('не совпадает')