from database import SessionLocal, engine
import models
import mock_data

def seed_database():
    print("Dropping existing tables...")
    models.Base.metadata.drop_all(bind=engine)
    print("Creating tables...")
    models.Base.metadata.create_all(bind=engine)
    
    db = SessionLocal()
    
    print("Seeding special menu...")
    for item_data in mock_data.special_menu["items"]:
        dish = models.Dish(
            id=item_data["id"],
            subcategory_id=None,
            is_special_menu=True,
            name=item_data["name"],
            description=item_data.get("description"),
            ingredients=item_data.get("ingredients"),
            price=item_data["price"],
            weight=item_data.get("weight"),
            image=item_data.get("image")
        )
        db.add(dish)
        
    print("Seeding regular categories...")
    for cat_data in mock_data.menu_categories:
        category = models.Category(
            id=cat_data["id"],
            name=cat_data["name"]
        )
        db.add(category)
        
        for sub_data in cat_data.get("subcategories", []):
            subcategory = models.Subcategory(
                id=sub_data["id"],
                category_id=category.id,
                name=sub_data["name"]
            )
            db.add(subcategory)
            
            for item_data in sub_data.get("items", []):
                dish = models.Dish(
                    id=item_data["id"],
                    subcategory_id=subcategory.id,
                    is_special_menu=False,
                    name=item_data["name"],
                    description=item_data.get("description"),
                    ingredients=item_data.get("ingredients"),
                    price=item_data["price"],
                    weight=item_data.get("weight"),
                    image=item_data.get("image")
                )
                db.add(dish)
                
    db.commit()
    db.close()
    print("Database seeding completed.")

if __name__ == "__main__":
    seed_database()
