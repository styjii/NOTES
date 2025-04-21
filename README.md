# 📝 NOTES

[![CI](https://github.com/styjii/NOTES/actions/workflows/ci.yml/badge.svg)](https://github.com/styjii/NOTES/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.x-green.svg)](https://www.djangoproject.com/)
[![TinyDB](https://img.shields.io/badge/DB-TinyDB-lightgrey.svg)](https://tinydb.readthedocs.io/)
[![Tests](https://img.shields.io/badge/Tests-pytest-blue.svg)](https://docs.pytest.org/)
[![codecov](https://codecov.io/gh/styjii/NOTES/branch/main/graph/badge.svg)](https://codecov.io/gh/styjii/NOTES)

A Django-based web application for managing notes across multiple tables. Built to organize and persist structured note data using TinyDB under the hood.

## 🚀 Features

- Create, update, and delete notes
- Organize notes by custom-named tables
- Fast, lightweight backend using TinyDB
- Easy-to-use API for managing notes and tables
- Clean and simple Django-based structure

## 🛆 Requirements

- Python 3.8+
- Django 4.x
- TinyDB
- [Optional] pytest for testing

## 📁 Project Structure

```
NOTES/
├── src ├── api/
│       │   ├── __init__.py
│       │   ├── db.json      # TinyDB data file
│       │   ├── notes.py     # Note and TablesNotes logic
│       │   └── test_notes.py     # Pytest-based tests
│       ├── webapp/
│       │   ├── settings.py
│       │   ├── urls.py
│       │   └── ...
│       ├── notes/
│       │   ├── apps.py
│       │   ├── urls.py
│       │   └── ...
│       ├── manage.py
│       └── ...
├── README.md 
└── requirements.txt
```

## 🛠️ Setup Instructions

1. **Clone the repository**
   ```bash
   git clone git@github.com:styjii/NOTES.git
   cd NOTES
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations (if any)**
   > Note: If you're using only TinyDB, this step may not be necessary.

5. **Run the development server**
   ```bash
   python manage.py runserver
   ```

6. **Access the app**
   Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

## 🧪 Running Tests

Run all tests using `pytest`:

```bash
pytest
```

## 🧠 Notes Storage

Notes are saved in `db.json` using [TinyDB](https://tinydb.readthedocs.io/en/latest/), allowing for lightweight and schema-less data storage.

## 🤝 Contributing

Pull requests are welcome! If you have suggestions or want to report a bug, feel free to open an issue.

## 📝 License

This project is open-source and available under the MIT License. See `LICENSE` for more information.

---

> Built with ❤️ by [styjii](https://github.com/styjii) using Django + TinyDB
