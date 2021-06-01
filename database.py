from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# SQLALCHEMY_DATABASE_URL = "mysql://root:@localhost:3306/codeburst"
# SQLALCHEMY_DATABASE_URL = "postgresql://root:1@localhost:5432/kardinahku" #+"?gssencmode=disable"
SQLALCHEMY_DATABASE_URL = "mssql://ffzkjadfreivst:98ba1c306e13f8983947db183f9ae2a6f5b17b2230b6673dad34ee8b67a05c5b@ec2-54-209-43-223.compute-1.amazonaws.com:5432/dfnomeliqel0qf" #+"?gssencmode=disable"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
