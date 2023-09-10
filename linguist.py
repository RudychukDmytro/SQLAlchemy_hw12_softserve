from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('sqlite:///linguist.db', echo=True)


Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    decks = relationship('Deck', back_populates='user')
    cards = relationship('Card', back_populates='user')

class Deck(Base):
    __tablename__ = 'decks'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship('User', back_populates='decks')
    cards = relationship('Card', back_populates='deck')



class Card(Base):
    __tablename__ = 'cards'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    word = Column(String)
    translation = Column(String)
    tip = Column(String)
    deck_id = Column(Integer, ForeignKey('decks.id'))

    user = relationship('User', back_populates='cards')
    deck = relationship('Deck', back_populates='cards')



Base.metadata.create_all(engine)

def user_create(name, email, password):
    session = Session()
    user = User(name=name, email=email, password=password)
    session.add(user)
    session.commit()
    session.close()
    return user

def user_get_by_id(user_id):
    session = Session()
    user = session.query(User).filter_by(id=user_id).first()
    session.close()
    return user

def user_update_name(user_id, name):
    session = Session()
    user = session.query(User).filter_by(id=user_id).first()
    if user:
        user.name = name
        session.commit()
    session.close()
    return user

def user_change_password(user_id, old_password, new_password):
    session = Session()
    user = session.query(User).filter_by(id=user_id).first()
    if user and user.password == old_password:
        user.password = new_password
        session.commit()
        session.close()
        return True
    session.close()
    return False

def user_delete_by_id(user_id):
    session = Session()
    user = session.query(User).filter_by(id=user_id).first()
    if user:
        session.delete(user)
        session.commit()
        session.close()
        return True
    session.close()
    return False


def deck_create(name, user_id):
    session = Session()
    deck = Deck(name=name, user_id=user_id)
    session.add(deck)
    session.commit()
    session.close()
    return deck

def deck_get_by_id(deck_id):
    session = Session()
    deck = session.query(Deck).filter_by(id=deck_id).first()
    session.close()
    return deck

def deck_update(deck_id, name):
    session = Session()
    deck = session.query(Deck).filter_by(id=deck_id).first()
    if deck:
        deck.name = name
        session.commit()
    session.close()
    return deck

def deck_delete_by_id(deck_id):
    session = Session()
    deck = session.query(Deck).filter_by(id=deck_id).first()
    if deck:
        session.delete(deck)
        session.commit()
        session.close()
        return True
    session.close()
    return False


def card_create(user_id, word, translation, tip, deck_id):
    session = Session()
    card = Card(user_id=user_id, word=word, translation=translation, tip=tip, deck_id=deck_id)
    session.add(card)
    session.commit()
    session.close()
    return card

def card_get_by_id(card_id):
    session = Session()
    card = session.query(Card).filter_by(id=card_id).first()
    session.close()
    return card

def card_filter(sub_word):
    session = Session()
    cards = session.query(Card).filter(
        (Card.word.like(f"%{sub_word}%")) |
        (Card.translation.like(f"%{sub_word}%")) |
        (Card.tip.like(f"%{sub_word}%"))
    ).all()
    session.close()
    return tuple(cards)

def card_update(card_id, word=None, translation=None, tip=None):
    session = Session()
    card = session.query(Card).filter_by(id=card_id).first()
    if card:
        if word is not None:
            card.word = word
        if translation is not None:
            card.translation = translation
        if tip is not None:
            card.tip = tip
        session.commit()
    session.close()
    return card

def card_delete_by_id(card_id):
    session = Session()
    card = session.query(Card).filter_by(id=card_id).first()
    if card:
        session.delete(card)
        session.commit()
        session.close()
        return True
    session.close()
    return False



