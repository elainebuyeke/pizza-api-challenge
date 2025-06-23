# Pizza Restaurant API Challenge

This is a RESTful API for managing restaurants, pizzas, and their associations. Built using Flask, SQLAlchemy, and Flask-Migrate, the API allows clients to retrieve data, create relationships, and delete resources.


## Setup Instructions

### Environment Setup

1. Clone the repository:

```bash
git clone https://github.com/your-username/pizza-api-challenge.git
cd pizza-api-challenge

2. Install dependencies and activate shell:
pipenv install flask flask_sqlalchemy flask_migrate
pipenv shell

Database Setup 

1. Set Flask app environment variable:
  export FLASK_APP=server/app.py

2.Initialize and migrate the database:
  flask db init
  flask db migrate -m "Initial migration"
  flask db upgrade

Seed the database
  1.Edit server/seed.py to add sample data.
  2.Run the seed script:
    python server/seed.py

Testing with Postman
  1.Open Postman.
  2.Click "Import" and upload challenge-1-pizzas.postman_collection.json.
  3.Use the collection to test each route and confirm expected behavior.

Technologies Used
-Python 3
-Flask
-Flask-SQLAlchemy
-Flask-Migrate
-SQLite (development)






