# 🛍️ Django Product Search App

This is a simple Django application that allows users to search and filter products by description, category, and tags.

## 🚀 Features

- Add and manage Products, Categories, and Tags via Django Admin
- Search products by description (case-insensitive)
- Filter products by:
  - Category (single select)
  - Tags (multi-select)
- Combine search and filter options

## 🧰 Tech Stack

- Python 3
- Django 4+
- SQLite (default)

---

## 📦 Setup Instructions

### 1. Clone the repository

```bash
git clone [https://github.com/your-username/django-product-search.git](https://github.com/VladislavYarovenko/django-product-search.git)
cd django-product-search
```
### 2. Setup the Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```
### 3. Requirements

```bash
pip install -r requirements.txt
```
### 4. Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```
### 5. Create Superuser
```bash
python manage.py createsuperuser
```
### 6. Start the Development Server
```bash
python manage.py runserver 
```
- Open your browser and go to http://127.0.0.1:8000/ to access the product search page.
- Go to http://127.0.0.1:8000/admin to manage products, categories, and tags through the Django admin panel.




