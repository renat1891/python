from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.exc import IntegrityError
import os
import json

Base = declarative_base()

current_dir = os.path.dirname(os.path.abspath(__file__))

class Joke(Base):
    __tablename__ = 'jokes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    joke = Column(Text, unique=True, nullable=False)

class DB:
    def __init__(self, file_name="jokes.db"):
        
        self.engine = create_engine(f"sqlite:///{file_name}", echo=False)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine, autoflush=False, autocommit=False)
        self.populate_jokes_from_json()

    def populate_jokes_from_json(self):
        jokes_json_path = os.path.join(current_dir, "jokes.json")
        if os.path.exists(jokes_json_path):
            with open(jokes_json_path, 'r', encoding='utf-8') as f:
                jokes_data = json.load(f)
            with self.Session() as session:
                for joke_entry in jokes_data:
                    joke_text = joke_entry.get("joke")
                    if joke_text:
                        try:
                            if not session.query(Joke).filter_by(joke=joke_text).first():
                                session.add(Joke(joke=joke_text))
                                session.commit()
                        except IntegrityError:
                            session.rollback()  # Rollback the transaction if a duplicate is found
                            print(f"Duplicate joke skipped: {joke_text}")

    def add_joke(self, joke):
        with self.Session() as session:
            if not session.query(Joke).filter_by(joke=joke).first():
                session.add(Joke(joke=joke))
                session.commit()

    def get_all_jokes(self):
        with self.Session() as session:
            jokes = session.query(Joke).all()
            return [j.joke for j in jokes]

    def close(self):
        pass