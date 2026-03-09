from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, JSON
from sqlalchemy.orm import relationship
from database import Base
import uuid

def generate_uuid():
    return str(uuid.uuid4())

class Category(Base):
    __tablename__ = "categories"

    id = Column(String, primary_key=True, index=True, default=generate_uuid)
    name = Column(JSON, nullable=False)
    
    subcategories = relationship("Subcategory", back_populates="category", cascade="all, delete-orphan")

    def __str__(self):
        try:
            return self.name.get('ru', self.name.get('en', 'Category'))
        except AttributeError:
            return "Category"

class Subcategory(Base):
    __tablename__ = "subcategories"

    id = Column(String, primary_key=True, index=True, default=generate_uuid)
    category_id = Column(String, ForeignKey("categories.id"), nullable=False)
    name = Column(JSON, nullable=False)
    
    category = relationship("Category", back_populates="subcategories")
    dishes = relationship("Dish", back_populates="subcategory", cascade="all, delete-orphan")

    def __str__(self):
        try:
            return self.name.get('ru', self.name.get('en', 'Subcategory'))
        except AttributeError:
            return "Subcategory"

class Dish(Base):
    __tablename__ = "dishes"

    id = Column(Integer, primary_key=True, index=True)
    subcategory_id = Column(String, ForeignKey("subcategories.id"), nullable=True)
    is_special_menu = Column(Boolean, default=False)
    
    name = Column(JSON, nullable=False)
    description = Column(JSON, nullable=True)
    ingredients = Column(JSON, nullable=True)
    
    price = Column(Float, nullable=False)
    weight = Column(String, nullable=True)
    image = Column(String, nullable=True)
    
    subcategory = relationship("Subcategory", back_populates="dishes")

    def __str__(self):
        try:
            return self.name.get('ru', self.name.get('en', 'Dish at %f' % self.price))
        except AttributeError:
            return "Dish"
