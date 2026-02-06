from sqlalchemy import create_engine, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker, Mapped, mapped_column

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str]
    age: Mapped[int]

class DB:
    def __init__(self, file_name="mydborm.db"):
        # sqlite файл
        self.engine = create_engine(f"sqlite:///{file_name}", echo=False)

        # створюємо таблиці (аналог CREATE TABLE IF NOT EXISTS)
        Base.metadata.create_all(self.engine)

        # фабрика сесій
        self.Session = sessionmaker(bind=self.engine, autoflush=False, autocommit=False)

    def add_user(self, name: str="", age: int=0):
        new_user = User(name=name, age=age)
        with self.Session() as session:
            session.add(new_user)
            session.commit()

    def get_users(self):
        with self.Session() as session:
            return session.query(User).all()
        
    def change_age_for_name(self, name: str, new_age: int):
        with self.Session() as session:
            user = session.query(User).filter(User.name == name).first()
            if user:
                user.age = new_age
                session.commit()
            else:
                print(f"User with name {name} not found.")

    def show_users_bigger_age(self, age: int):
        with self.Session() as session:
            users = session.query(User).filter(User.age > age).all()
            return users

new_db = DB()
new_db.add_user("Alice", 30)
new_db.add_user("Bob", 25)
users = new_db.get_users()
for user in users:
    print(f"User {user.id}: {user.name}, Age: {user.age}")
