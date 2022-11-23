from sqlmodel import create_engine, SQLModel


sqlite_file_name = "database.sqlite"
# define the path to the SQL lite
sqlite_url = f"sqlite:///{sqlite_file_name}"

# configuration because we are running an asynchronous server
connect_args = {"check_same_thread": False}
# create a motor to connect and operate with the database
engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)


# makes the SQLModel search by the model children and use then to create
# the database
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
