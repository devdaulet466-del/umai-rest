from database import SessionLocal, engine
import models

def add_more_categories():
    db = SessionLocal()
    
    categories_data = [
        {
            "id": "pasta",
            "name": {'en': 'Pasta', 'ru': 'Паста', 'kk': 'Паста'},
            "subcategories": [
                {
                    "id": "pasta-sub",
                    "name": {'en': 'Pasta', 'ru': 'Паста', 'kk': 'Паста'},
                    "dishes": [
                        {"id": 50, "price": 4800, "name": {'en': 'Casarecce with braised beef and mushrooms', 'ru': 'Казаречче с томленой говядиной и грибами', 'kk': 'Бұқтырылған сиыр еті мен саңырауқұлақ қосылған казаречче'}},
                        {"id": 51, "price": 6100, "name": {'en': 'Spicy tomato seafood pasta', 'ru': 'Острая томатная паста с морепродуктами', 'kk': 'Теңіз өнімдері қосылған ащы томат пастасы'}},
                        {"id": 52, "price": 5800, "name": {'en': 'Spaghetti aglio e olio with prawns', 'ru': 'Спагетти алио и олио с креветками', 'kk': 'Асшаян қосылған алио и олио спагеттиі'}},
                        {"id": 53, "price": 4500, "name": {'en': 'Fettuccine Alfredo with chicken breast', 'ru': 'Феттуччини Альфредо с куриной грудкой', 'kk': 'Тауық төсі қосылған Альфредо феттуччиниі'}}
                    ]
                }
            ]
        },
        {
            "id": "soups",
            "name": {'en': 'Soups', 'ru': 'Супы', 'kk': 'Сорпалар'},
            "subcategories": [
                {
                    "id": "soups-sub",
                    "name": {'en': 'Soups', 'ru': 'Супы', 'kk': 'Сорпалар'},
                    "dishes": [
                        {"id": 60, "price": 4100, "name": {'en': 'Bean soup with braised beef cheeks', 'ru': 'Фасолевый суп с говяжьими щечками', 'kk': 'Сиыр ұрты қосылған үрмебұршақ сорпасы'}},
                        {"id": 61, "price": 3500, "name": {'en': 'Chicken meatball and noodle soup', 'ru': 'Куриный суп с фрикадельками и лапшой', 'kk': 'Фрикаделька мен кеспе қосылған тауық сорпасы'}},
                        {"id": 62, "price": 6800, "name": {'en': 'Tom yum with seafood', 'ru': 'Том ям с морепродуктами', 'kk': 'Теңіз өнімдері қосылған том ям'}},
                        {"id": 63, "price": 4100, "name": {'en': 'Creamy lentil soup', 'ru': 'Крем-суп из чечевицы', 'kk': 'Жасымық крем-сорпасы'}}
                    ]
                }
            ]
        },
        {
            "id": "pizza",
            "name": {'en': 'Pizza', 'ru': 'Пицца', 'kk': 'Пицца'},
            "subcategories": [
                {
                    "id": "roman-style-pizza",
                    "name": {'en': 'Roman-style pizza', 'ru': 'Римская пицца', 'kk': 'Рим пиццасы'},
                    "dishes": [
                        {"id": 70, "price": 3800, "name": {'en': 'Margherita', 'ru': 'Маргарита', 'kk': 'Маргарита'}},
                        {"id": 71, "price": 4800, "name": {'en': 'Pepperoni-style with sujuk', 'ru': 'В стиле пепперони с суджуком', 'kk': 'Суджук қосылған пепперони стиліндегі пицца'}},
                        {"id": 72, "price": 6500, "name": {'en': 'Salmon and cucumber', 'ru': 'Лосось и огурец', 'kk': 'Лосось және қияр'}},
                        {"id": 73, "price": 4800, "name": {'en': 'Mortadella and pistachios', 'ru': 'Мортаделла и фисташки', 'kk': 'Мортаделла және пісте'}},
                        {"id": 74, "price": 5300, "name": {'en': 'Cheese and truffle', 'ru': 'Сыр и трюфель', 'kk': 'Ірімшік және трюфель'}}
                    ]
                }
            ]
        },
        {
            "id": "kids",
            "name": {'en': 'Kids Menu', 'ru': 'Детское меню', 'kk': 'Балалар мәзірі'},
            "subcategories": [
                {
                    "id": "kids-menu",
                    "name": {'en': 'Kids Menu', 'ru': 'Детское меню', 'kk': 'Балалар мәзірі'},
                    "dishes": [
                        {"id": 80, "price": 2300, "name": {'en': 'Meatball noodle soup', 'ru': 'Суп с лапшой и фрикадельками', 'kk': 'Фрикаделька мен кеспе қосылған сорпа'}},
                        {"id": 81, "price": 2900, "name": {'en': 'Spaghetti with cheese', 'ru': 'Спагетти с сыром', 'kk': 'Ірімшік қосылған спагетти'}},
                        {"id": 82, "price": 3200, "name": {'en': 'Dumplings with sour cream topping', 'ru': 'Пельмени со сметаной', 'kk': 'Қаймақ қосылған тұшпара'}},
                        {"id": 83, "price": 2900, "name": {'en': 'Turkey patties with mash', 'ru': 'Котлеты из индейки с пюре', 'kk': 'Күркетауық котлеттері және езбе'}},
                        {"id": 84, "price": 1900, "name": {'en': 'Potato dippers with ketchup', 'ru': 'Картофельные дипперы с кетчупом', 'kk': 'Кетчуп қосылған картоп дипперлері'}}
                    ]
                }
            ]
        },
        {
            "id": "desserts",
            "name": {'en': 'Desserts', 'ru': 'Десерты', 'kk': 'Десерттер'},
            "subcategories": [
                {
                    "id": "umai-homemade-desserts",
                    "name": {'en': 'Homemade Desserts', 'ru': 'Домашние десерты', 'kk': 'Үй десерттері'},
                    "dishes": [
                        {"id": 90, "price": 2900, "name": {'en': 'Honey cake', 'ru': 'Медовик', 'kk': 'Балды торт'}},
                        {"id": 91, "price": 2900, "name": {'en': 'Napoleon cake', 'ru': 'Наполеон', 'kk': 'Наполеон'}},
                        {"id": 92, "price": 3300, "name": {'en': 'Basque cheesecake', 'ru': 'Баскский чизкейк', 'kk': 'Баск чизкейкі'}},
                        {"id": 93, "price": 4000, "name": {'en': 'Umai dessert', 'ru': 'Десерт Умай', 'kk': 'Умай десерті'}},
                        {"id": 94, "price": 1600, "name": {'en': 'Classic croissant', 'ru': 'Классический круассан', 'kk': 'Классикалық круассан'}}
                    ]
                }
            ]
        }
    ]

    for cat_data in categories_data:
        # Add category if not exists
        cat = db.query(models.Category).filter(models.Category.id == cat_data["id"]).first()
        if not cat:
            cat = models.Category(id=cat_data["id"], name=cat_data["name"])
            db.add(cat)
            db.commit()
            
        for sub_data in cat_data["subcategories"]:
            # Add subcategory if not exists
            sub = db.query(models.Subcategory).filter(models.Subcategory.id == sub_data["id"]).first()
            if not sub:
                sub = models.Subcategory(
                    id=sub_data["id"],
                    category_id=cat_data["id"],
                    name=sub_data["name"]
                )
                db.add(sub)
                db.commit()
                
            for dish_data in sub_data["dishes"]:
                # Add dish if not exists
                dish = db.query(models.Dish).filter(models.Dish.id == dish_data["id"]).first()
                if not dish:
                    dish = models.Dish(
                        id=dish_data["id"],
                        subcategory_id=sub_data["id"],
                        price=dish_data["price"],
                        name=dish_data["name"],
                        description={'en': '', 'ru': '', 'kk': ''},
                        ingredients={'en': '', 'ru': '', 'kk': ''},
                        is_special_menu=False
                    )
                    db.add(dish)
    
    db.commit()
    db.close()
    print("All additional categories and dishes successfully appended to the Database!")

if __name__ == "__main__":
    add_more_categories()
