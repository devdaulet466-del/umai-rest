from database import SessionLocal, engine
import models

def add_mains():
    db = SessionLocal()
    
    # 1. Add Category
    cat_id = "mains"
    cat = db.query(models.Category).filter(models.Category.id == cat_id).first()
    if not cat:
        cat = models.Category(
            id=cat_id,
            name={'en': 'Main Courses', 'ru': 'Основные блюда', 'kk': 'Негізгі тағамдар'}
        )
        db.add(cat)
        db.commit()
    
    # 2. Add Subcategories
    subcategories = [
        {"id": "meat", "name": {'en': 'Meat', 'ru': 'Мясо', 'kk': 'Ет'}},
        {"id": "poultry", "name": {'en': 'Poultry', 'ru': 'Птица', 'kk': 'Құс еті'}},
        {"id": "fish", "name": {'en': 'Fish', 'ru': 'Рыба', 'kk': 'Балық'}},
    ]
    
    for sub in subcategories:
        existing_sub = db.query(models.Subcategory).filter(models.Subcategory.id == sub["id"]).first()
        if not existing_sub:
            new_sub = models.Subcategory(
                id=sub["id"],
                category_id=cat_id,
                name=sub["name"]
            )
            db.add(new_sub)
    
    db.commit()

    # 3. Add Dishes
    dishes_data = [
        # Meat
        {
            "id": 30, "subcategory_id": "meat", "price": 11300,
            "name": {'en': 'Ribeye steak with mushroom sauce', 'ru': 'Стейк Рибай с грибным соусом', 'kk': 'Саңырауқұлақ соусымен Рибай стейкі'}
        },
        {
            "id": 31, "subcategory_id": "meat", "price": 9500,
            "name": {'en': 'Beef rib with mashed potato and pickled vegetables', 'ru': 'Говяжье ребро с картофельным пюре и маринованными овощами', 'kk': 'Картоп езбесі және маринадталған көкөністермен сиыр қабырғасы'}
        },
        {
            "id": 32, "subcategory_id": "meat", "price": 9900,
            "name": {'en': 'Horse steak with truffle mash and peppercorn sauce', 'ru': 'Стейк из конины с трюфельным пюре и перечным соусом', 'kk': 'Трюфель езбесі және бұрыш соусымен жылқы етінен стейк'}
        },
        {
            "id": 33, "subcategory_id": "meat", "price": 6800,
            "name": {'en': 'Beef burger with chipotle sauce', 'ru': 'Говяжий бургер с соусом чипотле', 'kk': 'Чипотле соусымен сиыр етінен бургер'}
        },
        {
            "id": 34, "subcategory_id": "meat", "price": 7100,
            "name": {'en': 'Beshbarmak', 'ru': 'Бешбармак', 'kk': 'Бешбармақ'}
        },
        {
            "id": 35, "subcategory_id": "meat", "price": 4600,
            "name": {'en': 'Umai pelmeni dumplings', 'ru': 'Пельмени Умай', 'kk': 'Умай тұшпарасы'}
        },
        
        # Poultry
        {
            "id": 36, "subcategory_id": "poultry", "price": 5900,
            "name": {'en': 'Chicken breast with romaine lettuce and blue cheese sauce', 'ru': 'Куриная грудка с салатом ромэн и соусом блю чиз', 'kk': 'Ромэн салаты және көк ірімшік соусымен тауық төсі'}
        },
        {
            "id": 37, "subcategory_id": "poultry", "price": 5500,
            "name": {'en': 'Chicken thigh schnitzel with pickled cucumbers and mashed potato cream', 'ru': 'Шницель из куриного бедра с маринованными огурцами и кремом из картофельного пюре', 'kk': 'Маринадталған қияр және картоп езбесі кремімен тауық санынан шницель'}
        },
        {
            "id": 38, "subcategory_id": "poultry", "price": 5100,
            "name": {'en': 'Turkey patties with pesto mash', 'ru': 'Котлеты из индейки с пюре песто', 'kk': 'Песто езбесімен күркетауық котлеттері'}
        },
        
        # Fish
        {
            "id": 39, "subcategory_id": "fish", "price": 8900,
            "name": {'en': 'Salmon steak with caviar sauce', 'ru': 'Стейк из лосося с икорным соусом', 'kk': 'Уылдырық соусымен лосось стейкі'}
        },
        {
            "id": 40, "subcategory_id": "fish", "price": 8900,
            "name": {'en': 'Sicilian-style dorade', 'ru': 'Дорадо по-сицилийски', 'kk': 'Сицилияша дорадо'}
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
                description={'en': '', 'ru': '', 'kk': ''},
                ingredients={'en': '', 'ru': '', 'kk': ''},
                is_special_menu=False
            )
            db.add(dish)

    db.commit()
    db.close()
    print("Mains successfully appended to Database! Previous data was not touched.")

if __name__ == "__main__":
    add_mains()
