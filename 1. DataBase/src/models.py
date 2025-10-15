from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, ForeignKey, Enum as SQLEnum
from typing import List
from enum import Enum
from sqlalchemy import DateTime
from datetime import datetime

Base = declarative_base()  # <- саме Base використовується для create_all

