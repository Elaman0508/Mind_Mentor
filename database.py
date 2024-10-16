from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Правильная строка подключения
DATABASE_URL = "postgresql://postgres:Ernisov1x@localhost:5432/mindmentor"

# Использование правильной строки подключения в create_engine
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
