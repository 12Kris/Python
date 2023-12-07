import random


def charivna_kulka(question):
    """
    Функція, яка приймає питання та повертає випадкову відповідь

    Функція вибирає випадкову відповідь зі списку ["так", "ні", "можливо", "категорично ні"].
    Якщо запитання порожнє, функція поверне повідомлення "Запитання відсутнє. Будь ласка, задайте питання"
    """
    answers = ["так", "ні", "можливо", "категорично ні"]
    if not question:
        return "Запитання відсутнє"
    response = random.choice(answers)
    return response
