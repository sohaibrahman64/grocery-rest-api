from flask import Flask, request, jsonify, Blueprint, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

import os

# Init
app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

# groceries = Blueprint("groceries", __name__, url_prefix="/api/v1/groceries")

# app.register_blueprint(groceries)

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'groceries.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['APPLICATION_ROOT'] = '/api/v1/groceries'

# Init DB
db = SQLAlchemy(app)

# Init Marshmallow
ma = Marshmallow(app)


class Categories(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    url = db.Column(db.String(100))
    alias = db.Column(db.String(100))
    product = db.relationship('Products', backref='categories')

    def __init__(self, name, url, alias):
        self.name = name
        self.url = url
        self.alias = alias


class Home(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description_1 = db.Column(db.String(100))
    description_2 = db.Column(db.String(100))
    description_3 = db.Column(db.String(100))
    description_4 = db.Column(db.String(100))
    description_5 = db.Column(db.String(100))
    image_1 = db.Column(db.String(100))
    image_2 = db.Column(db.String(100))
    image_3 = db.Column(db.String(100))
    image_4 = db.Column(db.String(100))
    image_5 = db.Column(db.String(100))
    old_price = db.Column(db.String(100))
    new_price = db.Column(db.String(100))
    availability = db.Column(db.String(100))
    product_code = db.Column(db.String(100))


class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    name = db.Column(db.String(100))
    description_1 = db.Column(db.String(100))
    description_2 = db.Column(db.String(100))
    description_3 = db.Column(db.String(100))
    description_4 = db.Column(db.String(100))
    description_5 = db.Column(db.String(100))
    image_1 = db.Column(db.String(100))
    image_2 = db.Column(db.String(100))
    image_3 = db.Column(db.String(100))
    image_4 = db.Column(db.String(100))
    image_5 = db.Column(db.String(100))
    old_price = db.Column(db.String(100))
    new_price = db.Column(db.String(100))
    availability = db.Column(db.String(100))
    product_code = db.Column(db.String(100))


# Category Schema
class CategorySchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'url', 'alias')


# Home Schema
class HomeSchema(ma.Schema):
    class Meta:
        fields = (
            'id', 'name', 'description_1', 'description_2', 'description_3', 'description_4', 'description5',
            'image_1', 'image_2', 'image_3', 'image_4', 'image_5', 'old_price', 'new_price', 'availability',
            'product_code'
        )


class ProductSchema(ma.Schema):
    class Meta:
        fields = (
            'id', 'category_id', 'name', 'description_1', 'description_2', 'description_3', 'description_4',
            'description5', 'image_1', 'image_2', 'image_3', 'image_4', 'image_5', 'old_price', 'new_price',
            'availability', 'product_code'
        )


# Init Schemas
category_schema = CategorySchema()
categories_schema = CategorySchema(many=True)

home_schema = HomeSchema()
homes_schema = HomeSchema(many=True)

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

prefix = '/api/v1/groceries'

@app.route('/')
def index():
    return render_template('landing_page.html')


@app.route(prefix + '/categories', methods=['GET'])
# @groceries.route('/categories', methods=['GET'])
def get_categories():
    all_categories = Categories.query.all()
    result = categories_schema.dump(all_categories)
    return jsonify(result)


@app.route(prefix + '/categories/<id>', methods=['GET'])
# @groceries.route('/categories/<id>', methods=['GET'])
def get_category(id):
    category = Categories.query.get(id)
    return category_schema.jsonify(category)


@app.route(prefix + '/home', methods=['GET'])
# @groceries.route('/home', methods=['GET'])
def get_home_products():
    all_home_products = Home.query.all()
    result = homes_schema.dump(all_home_products)
    return jsonify(result)


@app.route(prefix + '/home/<id>', methods=['GET'])
# @groceries.route('/home/<id>', methods=['GET'])
def get_single_home_product(id):
    home = Home.query.get(id)
    return home_schema.jsonify(home)


@app.route(prefix + '/products', methods=['GET'])
# @groceries.route('/products', methods=['GET'])
def get_products():
    all_products = Products.query.all()
    result = products_schema.dump(all_products)
    return jsonify(result)


@app.route(prefix + '/products/<id>', methods=['GET'])
# @groceries.route('/products/<id>', methods=['GET'])
def get_single_product(id):
    product = Products.query.get(id)
    return product_schema.jsonify(product)


@app.route(prefix + '/products_as_per_category/<category_id>', methods=['GET'])
def get_products_as_per_category(category_id):
    all_products = Products.query.filter_by(category_id=category_id, availability="In Stock").all()
    result = products_schema.dump(all_products)
    return jsonify(result)


# Run Server
if __name__ == '__main__':
    app.run(debug=True)
