from database import SessionLocal, engine
import models

def add_salads():
    db = SessionLocal()
    
    # 1. Add Category
    cat_salads = db.query(models.Category).filter(models.Category.id == "salads").first()
    if not cat_salads:
        cat_salads = models.Category(
            id="salads",
            name={'en': 'Salads', 'ru': 'Салаты', 'kk': 'Салаттар'}
        )
        db.add(cat_salads)
        db.commit()
    
    # 2. Add Subcategories
    sub_fresh = db.query(models.Subcategory).filter(models.Subcategory.id == "fresh-salads").first()
    if not sub_fresh:
        sub_fresh = models.Subcategory(
            id="fresh-salads",
            category_id="salads",
            name={'en': 'Fresh Salads', 'ru': 'Свежие салаты', 'kk': 'Жаңа салаттар'}
        )
        db.add(sub_fresh)
    
    sub_warm = db.query(models.Subcategory).filter(models.Subcategory.id == "warm-salads").first()
    if not sub_warm:
        sub_warm = models.Subcategory(
            id="warm-salads",
            category_id="salads",
            name={'en': 'Warm Salads', 'ru': 'Теплые салаты', 'kk': 'Жылы салаттар'}
        )
        db.add(sub_warm)
    
    db.commit()

    # 3. Add Dishes
    dishes_data = [
        {
            "id": 20,
            "subcategory_id": "fresh-salads",
            "price": 5200,
            "name": {'en': 'Panzanella salad', 'ru': 'Салат Панцанелла', 'kk': 'Панцанелла салаты'},
            "description": {'en': '', 'ru': '', 'kk': ''},
            "ingredients": {'en': '', 'ru': '', 'kk': ''},
        },
        {
            "id": 21,
            "subcategory_id": "fresh-salads",
            "price": 5300,
            "name": {'en': 'Stracciatella with tomatoes and strawberries', 'ru': 'Страчателла с томатами и клубникой', 'kk': 'Қызанақ және құлпынай қосылған страчателла'},
            "description": {'en': '', 'ru': '', 'kk': ''},
            "ingredients": {'en': '', 'ru': '', 'kk': ''},
        },
        {
            "id": 22,
            "subcategory_id": "warm-salads",
            "price": 6100,
            "name": {'en': 'Salad with grilled prawns and avocado', 'ru': 'Салат с креветками гриль и авокадо', 'kk': 'Грильде пісірілген асшаяндар мен авокадо қосылған салат'},
            "description": {'en': '', 'ru': '', 'kk': ''},
            "ingredients": {'en': '', 'ru': '', 'kk': ''},
        },
        {
            "id": 23,
            "subcategory_id": "warm-salads",
            "price": 5500,
            "name": {'en': 'Horse meat salad with pickles and stracciatella', 'ru': 'Салат из конины с солеными огурцами и страчателлой', 'kk': 'Тұздалған қияр мен страчателла қосылған жылқы етінен салат'},
            "description": {'en': '', 'ru': '', 'kk': ''},
            "ingredients": {'en': '', 'ru': '', 'kk': ''},
        },
        {
            "id": 24,
            "subcategory_id": "warm-salads",
            "price": 5100,
            "name": {'en': 'Crispy aubergine with marinated tomatoes and halloumi cheese', 'ru': 'Хрустящие баклажаны с маринованными томатами и сыром халуми', 'kk': 'Маринадталған қызанақ және халуми ірімшігі қосылған қытырлақ баклажан'},
            "description": {'en': '', 'ru': '', 'kk': ''},
            "ingredients": {'en': '', 'ru': '', 'kk': ''},
        }
    ]

    for d_data in dishes_data:
        existing = db.query(models.Dish).filter(models.Dish.id == d_data["id"]).first()
        if not existing:
            dish = models.Dish(
                id=d_data["id"],
                subcategory_id=d_data["subcategory_id"],
                price=d_data["price"],
                name=d_data["name"],
                description=d_data["description"],
                ingredients=d_data["ingredients"],
                is_special_menu=False
            )
            db.add(dish)

    db.commit()
    db.close()
    print("Salads successfully appended to Database! Breakfasts were not touched.")

if __name__ == "__main__":
    add_salads()
