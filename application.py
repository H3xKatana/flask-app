from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import requests                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
from py_edamam import Edamam  # Fixed indentation issue
from models import *
from auth import *
app = Flask(__name__)

# Database configuration (uncomment if needed)
# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

# Edamam API configuration (uncomment and replace with your credentials)
# APP_ID = 'your_app_id'
# APP_KEY = 'your_app_key'
# edamam = Edamam(recipes_appid=APP_ID, recipes_appkey=APP_KEY)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        search_text = request.form.get("search-textbox", "").strip()
        if search_text:
            return redirect(url_for("search_page", text=search_text))
        else:
            return ("", 204)
    return render_template("index.html")

@app.route("/search/<text>", methods=["GET", "POST"])
def search_page(text):
    return render_template("search-page.html", text=text)

@app.route("/<param>")
def go_to(param):
    template_name = f"{param}.html"
    return render_template(template_name)

# Adding missing routes to fix BuildError
@app.route("/trending")
def trending():
    return render_template("trending.html")

@app.route("/classics")
def classics():
    return render_template("classics.html")

@app.route("/desserts")
def desserts():
    return render_template("desserts.html")

@app.route("/lunch")
def lunch():
    return render_template("lunch.html")

# Uncomment the following block if using SQLAlchemy for recipes
# use postegerss when ready 
"""


@app.route('/recipes', methods=['GET'])
def get_recipes():
    recipes = Recipe.query.all()
    output = []
    for recipe in recipes:
        recipe_data = {
            "name": recipe.name,
            "page_link": recipe.page_link,
            "rating": recipe.rating,
            "cost": recipe.cost,
            "time": recipe.time,
        }
        output.append(recipe_data)
    return {"recipes": output}

@app.route('/recipe/<int:id>', methods=['GET'])
def get_recipe(id):
    recipe = Recipe.query.get_or_404(id)
    return {
        "name": recipe.name,
        "description": recipe.page_link,
        "rating": recipe.rating,
        "cost": recipe.cost,
        "time": recipe.time,
    }

@app.route('/recipes', methods=['POST'])
def add_recipe():
    data = request.json
    recipe = Recipe(
        name=data['name'],
        page_link=data['description'],
        rating=data['rating'],
        cost=data['cost'],
        time=data['time']
    )
    db.session.add(recipe)
    db.session.commit()
    return {"message": "Recipe added successfully"}, 201
"""

if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=5000, debug=True) 
    # set debug to false when deploying
    app.run(debug=True)
