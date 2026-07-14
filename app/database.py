from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# SQLAlchemy uses a URL string to know which db engine to use and where the database file is located.
SQLALCHEMY_DATABASE_URL = "sqlite:///./inventory.db"

# The engine is the core connection to the database. It manages connections and allows SQLAlchemy to communicate with the database.
# The connect_args parameter is used to pass additional arguments to the database connection. 
# In this case, check_same_thread is set to False to allow multiple threads to access the database simultaneously.
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# The sessionmaker creates a class that can generate new database sessions.
# autocommit=False means that changes to the database will not be automatically committed after each operation.
# autoflush=False means that changes to the database will not be automatically flushed to the database before each query.
# The bind=engine parameter tells the sessionmaker to use the engine we created earlier to connect to the database.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# The declarative_base function creates a base class for our ORM models.
# This Base class maintains a catalog of classes and tables relative to that base, which is used to generate the database schema.
Base = declarative_base()
