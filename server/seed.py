import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from server import create_app, db
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza

def seed_data():
    app = create_app()
    with app.app_context(): 
        
        db.drop_all()
        db.create_all()

        r1 = Restaurant(name="Domino's", address="Ngong lane")
        r2 = Restaurant(name="Pizza Inn", address="Junction Mall,Ngong rd")
        db.session.add_all([r1, r2])
        db.session.commit() 

        p1 = Pizza(name="Hawaian", ingredients="Dough, Tomato Sauce, Cheese,Pineapple")
        p2 = Pizza(name="Pepperoni", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni")
        db.session.add_all([p1, p2])

        db.session.commit()  

        rp1 = RestaurantPizza(price=10, restaurant_id=r1.id, pizza_id=p1.id)
        rp2 = RestaurantPizza(price=12, restaurant_id=r2.id, pizza_id=p2.id)
        db.session.add_all([rp1, rp2])

        db.session.commit()
        print("Database seeded successfully!")

if __name__ == '__main__':
    seed_data()
