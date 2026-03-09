from fastapi import APIRouter, Depends
from typing import List
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import get_db
import models

router = APIRouter()

class CartItem(BaseModel):
    id: int
    quantity: int

class CheckoutRequest(BaseModel):
    items: List[CartItem]
    total_price: int
    comment: str | None = None

@router.get("/menu")
def get_menu(db: Session = Depends(get_db)):
    """
    Returns the categorized menu data from SQLite Database.
    """
    special_dishes = db.query(models.Dish).filter(models.Dish.is_special_menu == True).all()
    special_menu_data = {
        "name": {
            "en": "Special Menu",
            "ru": "Специальное меню",
            "kk": "Арнайы мәзір"
        },
        "items": [{
            "id": dish.id,
            "name": dish.name,
            "price": dish.price,
            "description": dish.description,
            "ingredients": dish.ingredients,
            "image": dish.image,
            "weight": dish.weight
        } for dish in special_dishes]
    }
    
    categories = db.query(models.Category).all()
    categories_data = []
    
    for category in categories:
        cat_data = {
            "id": category.id,
            "name": category.name,
            "subcategories": []
        }
        for sub in category.subcategories:
            sub_data = {
                "id": sub.id,
                "name": sub.name,
                "items": [{
                    "id": dish.id,
                    "name": dish.name,
                    "price": dish.price,
                    "description": dish.description,
                    "ingredients": dish.ingredients,
                    "image": dish.image,
                    "weight": dish.weight
                } for dish in sub.dishes if not dish.is_special_menu]
            }
            cat_data["subcategories"].append(sub_data)
        categories_data.append(cat_data)
        
    return {
        "special_menu": special_menu_data,
        "categories": categories_data
    }

@router.post("/checkout")
def checkout(request: CheckoutRequest):
    """
    Mock endpoint for submitting the cart.
    """
    print(f"Checkout received with {len(request.items)} items for {request.total_price}tg.")
    return {"status": "success", "message": "Order placed successfully!"}
