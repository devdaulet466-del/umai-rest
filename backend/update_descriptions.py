import os
import json
from database import SessionLocal
from models import Dish

def update_descriptions():
    # Path to the JSON file
    json_path = os.path.join(os.path.dirname(__file__), "..", "description_for_umai_rest.json")
    
    if not os.path.exists(json_path):
        print(f"Error: {json_path} does not exist.")
        return

    print("Loading descriptions from JSON...")
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    db = SessionLocal()
    updated_count = 0
    not_found_count = 0

    print("Updating database...")
    try:
        for idx, item in enumerate(data):
            food_id = item.get("food_id")
            description = item.get("description")
            
            # Find the dish in the database
            dish = db.query(Dish).filter(Dish.id == food_id).first()
            if dish:
                dish.description = description
                updated_count += 1
            else:
                print(f"Warning: Dish with ID {food_id} not found in database.")
                not_found_count += 1

        db.commit()
        print("Database commit successful.")
    except Exception as e:
        db.rollback()
        print(f"Error occurred, database changes rolled back: {e}")
    finally:
        db.close()

    print(f"\nUpdate completed:")
    print(f" - Successfully updated: {updated_count} dishes")
    print(f" - Not found in database: {not_found_count} dishes")

if __name__ == "__main__":
    update_descriptions()
