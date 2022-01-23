
# About

A RESTful Flask API that provides grocery details. 
This project gets data from data stored in SQLite DB from [grocery-scraper](https://github.com/sohaibrahman64/grocery-scraper).

# Pre-requisites
1. Flask
2. Flask SQLAlchemy
3. Flask Marshmallow
4. Marshmallow SQLAlchemy

# Installation
```bash
pip install flask 
pip install flask-sqlalchemy 
pip install flask-marshmallow 
pip install marshmallow-sqlalchemy
```

# Request APIs Provided
## 1. Categories
```bash
http://localhost:5000/api/v1/groceries/categories
```
## 2. Single Category
```bash
http://localhost:5000/api/v1/groceries/categories/<id>
```
## 3. Home Products
```bash
http://localhost:5000/api/v1/groceries/home
```
## 4. Single Home Product
```bash
http://localhost:5000/api/v1/groceries/home/<id>
```
## 5. Products
```bash
http://localhost:5000/api/v1/groceries/products
```
## 6. Single Product
```bash
http://localhost:5000/api/v1/groceries/product/<id>
```
## 7. Product as per Category
```bash
http://localhost:5000/api/v1/groceries/products_as_per_category
```
## 8. Single Category Product
```bash
http://localhost:5000/api/v1/groceries/products_as_per_category/<id>
```












## Related

Find out more on [grocery-scraper](https://github.com/sohaibrahman64/grocery-scraper)

