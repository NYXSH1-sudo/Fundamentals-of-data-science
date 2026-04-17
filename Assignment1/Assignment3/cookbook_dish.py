"""
Q6: cookbook_dish.py - Dish class and Cookbook class to manage dish collection.
Dish: dishid, dishname, ingredients, instructions.
Author: Seshank Kumar Sharma,SEC-B.
Date: 2026-04-17
"""
class Dish:
    '''Represents a single dish with its recipe details.'''

    def __init__(self, dish_id, dish_name, ingredients, instructions):
        self.dish_id      = dish_id
        self.dish_name    = dish_name
        self.ingredients  = ingredients    # list of strings
        self.instructions = instructions   # string

    def display(self):
        '''Print full dish details.'''
        print("\n" + "-" * 50)
        print(f"  Dish ID      : {self.dish_id}")
        print(f"  Dish Name    : {self.dish_name}")
        print(f"  Ingredients  : {', '.join(self.ingredients)}")
        print(f"  Instructions : {self.instructions}")
        print("-" * 50)


class Cookbook:
    '''Manages a collection of Dish objects.'''

    def __init__(self):
        self.dishes = []   # list of Dish objects

    def add_dish(self, dish):
        '''Add a Dish object to the cookbook.'''
        # Check for duplicate ID
        for d in self.dishes:
            if d.dish_id == dish.dish_id:
                print(f"  ✘ Dish with ID '{dish.dish_id}' already exists.")
                return
        self.dishes.append(dish)
        print(f"  ✔ '{dish.dish_name}' added to the cookbook.")

    def view_all(self):
        '''Display all dishes in the cookbook.'''
        if not self.dishes:
            print("\n  The cookbook is empty.")
            return
        print(f"\n  === Cookbook ({len(self.dishes)} dish(es)) ===")
        for dish in self.dishes:
            dish.display()

    def search_by_name(self, name):
        '''Search for dishes whose name contains the given string (case-insensitive).'''
        results = [d for d in self.dishes if name.lower() in d.dish_name.lower()]
        if results:
            print(f"\n  Found {len(results)} result(s) for '{name}':")
            for dish in results:
                dish.display()
        else:
            print(f"\n  No dish found matching '{name}'.")

    def remove_dish(self, dish_id):
        '''Remove a dish by its ID.'''
        for i, d in enumerate(self.dishes):
            if d.dish_id == dish_id:
                removed = self.dishes.pop(i)
                print(f"  ✔ '{removed.dish_name}' removed from the cookbook.")
                return
        print(f"  ✘ No dish found with ID '{dish_id}'.")


# ─── Helper input functions ───────────────────────────────────────────────────

def get_input(prompt):
    while True:
        val = input(prompt).strip()
        if val:
            return val
        print("  Field cannot be empty.")


def input_dish(cookbook):
    '''Collect dish details from user and add to cookbook.'''
    print("\n  --- Add New Dish ---")
    dish_id      = get_input("  Dish ID       : ")
    dish_name    = get_input("  Dish Name     : ")
    ing_raw      = get_input("  Ingredients (comma-separated): ")
    ingredients  = [i.strip() for i in ing_raw.split(",") if i.strip()]
    instructions = get_input("  Instructions  : ")

    dish = Dish(dish_id, dish_name, ingredients, instructions)
    cookbook.add_dish(dish)


# ─── Main menu ────────────────────────────────────────────────────────────────

def main():
    cookbook = Cookbook()

    # Prepopulate with two sample dishes
    cookbook.add_dish(Dish("D001", "Dal Bhat",
                           ["lentils", "rice", "turmeric", "ghee", "salt"],
                           "Boil lentils with turmeric and salt. Cook rice separately. Serve hot with ghee."))
    cookbook.add_dish(Dish("D002", "Momo",
                           ["flour", "minced chicken", "onion", "garlic", "ginger", "soy sauce"],
                           "Mix filling ingredients. Wrap in dough circles. Steam for 15 minutes."))

    while True:
        print("\n" + "=" * 40)
        print("       COOKBOOK MENU")
        print("=" * 40)
        print("  1. Add a dish")
        print("  2. View all dishes")
        print("  3. Search dish by name")
        print("  4. Remove a dish")
        print("  5. Exit")
        print("=" * 40)

        choice = input("  Enter choice (1-5): ").strip()

        if choice == "1":
            input_dish(cookbook)
        elif choice == "2":
            cookbook.view_all()
        elif choice == "3":
            name = input("  Enter dish name to search: ").strip()
            cookbook.search_by_name(name)
        elif choice == "4":
            dish_id = input("  Enter Dish ID to remove: ").strip()
            cookbook.remove_dish(dish_id)
        elif choice == "5":
            print("\n  Exiting Cookbook. Goodbye!")
            break
        else:
            print("  Invalid choice. Please enter a number from 1 to 5.")


# Main
main()