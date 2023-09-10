from linguist import *


user_create(name="Alice", email="alice@email.com", password="password1")
user_create(name="Bob", email="bob@email.com", password="password2")

deck_create(name="Vocabulary", user_id=1)
deck_create(name="Phrases", user_id=1)

card_create(user_id=1, word="apple", translation="яблуко", tip="A fruit", deck_id=1)
card_create(user_id=2, word="cat", translation="кіт", tip="A pet", deck_id=2)
card_create(user_id=1, word="hello", translation="привіт", tip="Greeting", deck_id=1)