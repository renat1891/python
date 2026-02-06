from sqlalchemy import create_engine, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker, Mapped, mapped_column

Base = declarative_base()

class Food(Base):
    __tablename__ = "foods"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    weight: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    price: Mapped[int] = mapped_column(Integer, nullable=False, default=0)

    def __repr__(self):
        return f"Food(id={self.id}, name='{self.name}', weight={self.weight}, price={self.price}')"

class DB:
    def __init__(self, file_name="animaldb.db"):
        # sqlite файл
        self.engine = create_engine(f"sqlite:///{file_name}", echo=False)

        # створюємо таблиці (аналог CREATE TABLE IF NOT EXISTS)
        Base.metadata.create_all(self.engine)

        # фабрика сесій
        self.Session = sessionmaker(bind=self.engine, autoflush=False, autocommit=False)
    
    def add_food(self, name, weight, price):
        with self.Session() as session:
            new_food = Food(name=name, weight=weight, price=price)
            session.add(new_food)
            session.commit()  
    
    def get_all_foods(self):
        with self.Session() as session:
            foods = session.query(Food).all()
            return foods
    
    def get_food_by_id(self, food_id):
        with self.Session() as session:
            food = session.query(Food).filter(Food.id == food_id).first()
            return food
    
    def delete_food(self, food_id):
        with self.Session() as session:
            food = session.query(Food).filter(Food.id == food_id).first()
            if food:
                session.delete(food)
                session.commit()
