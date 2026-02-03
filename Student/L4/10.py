from sqlalchemy import create_engine, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker, Mapped, mapped_column

Base = declarative_base()

class Animal(Base):
    __tablename__ = "animals"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str]
    age: Mapped[int]
    weight: Mapped[int]
    height: Mapped[int]

class DB:
    def __init__(self, file_name="animaldb.db"):
        # sqlite файл
        self.engine = create_engine(f"sqlite:///{file_name}", echo=False)

        # створюємо таблиці (аналог CREATE TABLE IF NOT EXISTS)
        Base.metadata.create_all(self.engine)

        # фабрика сесій
        self.Session = sessionmaker(bind=self.engine, autoflush=False, autocommit=False)
    
    def add_animal(self, name: str="", age: int=0, weight: int=0, height: int=0):
        new_animal = Animal(name=name, age=age, weight=weight, height=height)
        with self.Session() as session:
            session.add(new_animal)
            session.commit()
    
    def show_animals(self):
        with self.Session() as session:
            return session.query(Animal).all()
            
new_db = DB()
new_db.add_animal("Rex")
new_db.add_animal("milka")
new_db.add_animal("tuzik")
animals = new_db.show_animals()
for animal in animals:
    print(f"Animal {animal.id}: {animal.name}, Age: {animal.age}, Weight: {animal.weight}, Height: {animal.height}")
