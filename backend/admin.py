from sqladmin import ModelView
from models import Category, Subcategory, Dish

class CategoryAdmin(ModelView, model=Category):
    column_list = [Category.id, Category.name]
    column_searchable_list = [Category.id]
    form_include_pk = True
    name = "Category"
    name_plural = "Categories"

class SubcategoryAdmin(ModelView, model=Subcategory):
    column_list = [Subcategory.id, Subcategory.category_id, Subcategory.name]
    column_searchable_list = [Subcategory.id, Subcategory.category_id]
    form_include_pk = True
    name = "Subcategory"
    name_plural = "Subcategories"

class DishAdmin(ModelView, model=Dish):
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
