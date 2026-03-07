from fastapi import APIRouter
from typing import List
from pydantic import BaseModel
from mock_data import menu_categories, special_menu

router = APIRouter()

class CartItem(BaseModel):
    id: int
    quantity: int

class CheckoutRequest(BaseModel):
    items: List[CartItem]
    total_price: int
    comment: str | None = None

@router.get("/menu")
def get_menu():
    """
    Returns the categorized menu data.
    """
    return {
        "special_menu": special_menu,
        "categories": menu_categories
    }

@router.post("/checkout")
def checkout(request: CheckoutRequest):
    """
    Mock endpoint for submitting the cart.
    """
    print(f"Checkout received with {len(request.items)} items for {request.total_price}tg.")
    return {"status": "success", "message": "Order placed successfully!"}
