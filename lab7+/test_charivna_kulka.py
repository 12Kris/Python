import charivna_kulka


def test_response_type():
    """
    Тест перевіряє, чи результат функції є рядком типу str
    """
    user_question = "Чи виграю я в лотерею?"
    response = charivna_kulka.charivna_kulka(user_question)
    assert isinstance(response, str)


def test_response_in_expected_answers():
    """
    Тест перевіряє, чи результат функції знаходиться серед відповідей
    """
    user_question = "Чи завтра буде сонячно?"
    response = charivna_kulka.charivna_kulka(user_question)
    expected_answers = ["так", "ні", "можливо", "категорично ні"]
    assert response in expected_answers


def test_empty_question_response():
    """
    Тест перевіряє реакцію функції на пусте запитання
    """
    empty_question = ""
    response_empty = charivna_kulka.charivna_kulka(empty_question)
    assert response_empty == "Запитання відсутнє"


def test_case_insensitivity():
    """
    Тест перевіряє, чи функція правильно обробляє регістр символів у запитанні
    """
    user_question = "Чи знайду я роботу у майбутньому?"
    response = charivna_kulka.charivna_kulka(user_question.lower())
    assert response in ["так", "ні", "можливо", "категорично ні"]
