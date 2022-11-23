from typing import Optional
from sqlmodel import SQLModel, Field

# create a table named Task
class Task(SQLModel, table=True):
    # makes id optional, but define it as an int variable
    # also defines it as a primary_key for the model
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
