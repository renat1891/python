from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.orm import declarative_base, sessionmaker
import os
import json

Base = declarative_base()

current_dir = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(current_dir, "countries.json")

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    tg_id = Column(Integer, unique=True, nullable=False)
    score = Column(Integer, default=0)

class History(Base):
    __tablename__ = 'history'

    id = Column(Integer, primary_key=True, autoincrement=True)
    event = Column(String, unique=True, nullable=False)
    description = Column(Text, nullable=False)

class DB:
    def __init__(self, file_name="animaldb.db"):
        # sqlite файл
        self.engine = create_engine(f"sqlite:///{file_name}", echo=False)

        # створюємо таблиці (аналог CREATE TABLE IF NOT EXISTS)
        Base.metadata.create_all(self.engine)

        # фабрика сесій
        self.Session = sessionmaker(bind=self.engine, autoflush=False, autocommit=False)
        self.populate_history_from_json()

    def populate_history_from_json(self):
        history_json_path = os.path.join(current_dir, "history.json")
        if os.path.exists(history_json_path):
            with open(history_json_path, 'r', encoding='utf-8') as f:
                history_data = json.load(f)
            with self.Session() as session:
                for event, description in history_data.items():
                    if not session.query(History).filter_by(event=event).first():
                        session.add(History(event=event, description=description))
                session.commit()

    def add_user(self, name, tg_id):
        with self.Session() as session:
            if not session.query(User).filter_by(tg_id=tg_id).first():
                session.add(User(name=name, tg_id=tg_id))
                session.commit()

    def add_score(self, tg_id, points):
        with self.Session() as session:
            user = session.query(User).filter_by(tg_id=tg_id).first()
            if user:
                user.score += points
                session.commit()

    def get_score(self, tg_id):
        with self.Session() as session:
            user = session.query(User).filter_by(tg_id=tg_id).first()
            return user.score if user else 0

    def get_history_data(self):
        with self.Session() as session:
            history = session.query(History).all()
            return {h.event: h.description for h in history}

    def delete_user(self, user_id):
        with self.Session() as session:
            user = session.query(User).filter(User.id == user_id).first()
            if user:
                session.delete(user)
                session.commit()

    def close(self):
        pass