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
git clone https://github.com/your-username/django-product-search.git
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

### 5.5. Clone the product data (Optional)
```bash
python manage.py loaddata data.json
```

### 6. Start the Development Server
```bash
python manage.py runserver 
```
- Open your browser and go to http://127.0.0.1:8000/ to access the product search page.
- Go to http://127.0.0.1:8000/admin to manage products, categories, and tags through the Django admin panel.


## 🤖 AI Usage Disclosure

Since I haven't been working with Django before, some parts were created with the help of ChatGPT.

### 🔍 Where AI Was Used:
- **Project Setup**: Instructions for setting up the Django environment, models, and admin configuration.
- **Code Snippets**: Assistance with the HTML template structure.
- **README.md Content**: The gorgeous formatting of the readme file.

### ✅ Compliance with AI Policy:
- **Understanding and Ownership**: I have reviewed and tested all code generated with AI assistance, and I fully understand how each part works.
- **Enhancement and Originality**: AI-generated code has been manually edited, integrated, and extended to suit the project’s specific requirements.
- **Attribution**: This section and comments in the code acknowledge AI contributions where applicable.

By submitting this assignment, I confirm that I take full ownership of the implementation and that I can explain every part of the codebase.


