from faker import Faker

fake = Faker('ru_RU')


# Создание профиля пользователя
def generate_profile():
    profile = {
        "name": fake.first_name_male(),
        "surname": fake.last_name_male(),
        "address": "Москва, ул. Карла Маркса 145",
        "metro": "Сокольники",
        "phone": "89819819881"
    }
    return profile


# Генерация даты заказа
def generate_rent_date():
    return str(fake.future_date())
