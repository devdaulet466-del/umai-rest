from sqladmin import ModelView
from models import Category, Subcategory, Dish
import urllib.request
import threading

def trigger_webhook():
    def send_request():
        try:
            url = "https://umairest.kz/update_menu.php?token=umai_cache_update_2026"
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            urllib.request.urlopen(req, timeout=20.0)
            print("Webhook sent successfully.")
        except Exception as e:
            print(f"Webhook failed: {e}")
    # Run in background to avoid blocking the Admin UI response
    threading.Thread(target=send_request).start()

class WebhookMixin:
    async def after_model_change(self, data, model, is_created, request):
        trigger_webhook()
        
    async def after_model_delete(self, model, request):
        trigger_webhook()

class CategoryAdmin(WebhookMixin, ModelView, model=Category):
    column_list = [Category.id, Category.name]
    column_searchable_list = [Category.id]
    form_include_pk = True
    name = "Category"
    name_plural = "Categories"

class SubcategoryAdmin(WebhookMixin, ModelView, model=Subcategory):
    column_list = [Subcategory.id, Subcategory.category_id, Subcategory.name]
    column_searchable_list = [Subcategory.id, Subcategory.category_id]
    form_include_pk = True
    name = "Subcategory"
    name_plural = "Subcategories"

class DishAdmin(WebhookMixin, ModelView, model=Dish):
    column_list = [Dish.id, Dish.name, Dish.subcategory_id, Dish.is_special_menu, Dish.price]
    column_searchable_list = [Dish.id, Dish.name]
    column_sortable_list = [Dish.id, Dish.price]
    form_include_pk = True
    form_widget_args = {
        "description": {"rows": 4},
        "ingredients": {"rows": 4},
        "name": {"rows": 2} # for JSON fields, sometimes helpful
    }
    name = "Dish"
    name_plural = "Dishes"
