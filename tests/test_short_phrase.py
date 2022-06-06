class TestShortPhrase:
    def test_short_phrase(self):
        phrase = input("Введите фразу короче 15 символов: ")
        n = len(phrase)
        assert n < 15, 'Фраза больше 15 символов'