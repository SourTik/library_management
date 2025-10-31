# Django Library Management System

A functional Library Management System built with Django to efficiently handle books, students, and borrowing activities. The system provides a simple and user-friendly interface for managing all library operations, from book registration to tracking borrowed items.

---

## Features

- Book Management – Add, update, view, and delete book records.  
- Student Management – Register and manage student information.  
- Borrow and Return System – Track borrowed and returned books.  
- Admin Dashboard – Manage users, books, and transactions via Django’s built-in admin panel.  
- Search Functionality – Search for books or students by name or ID.  
- Due Date Tracking – View overdue books and their return status.

---

## Tech Stack

| Layer | Technology |
|-------|-------------|
| Backend | Django (Python) |
| Frontend | HTML, CSS, Bootstrap |
| Database | SQLite (default) or MySQL |
| Authentication | Django Authentication System |
| Deployment | Localhost / PythonAnywhere / Render |

---

## Installation

Follow these steps to set up the project locally:

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/library-management-system.git
   cd library-management-system
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate      # On Windows
   source venv/bin/activate   # On Mac/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   Open your browser and go to:
   ```
   http://127.0.0.1:8000/
   ```

---

## Future Enhancements

- Email reminders for due or overdue books  
- Student dashboard for viewing borrowed books  
- Fine calculation system  
- REST API integration for mobile or frontend apps

---

## Author

**Saad Mahmoud**  
Software Engineering Student & Aspiring Full-Stack Developer  
Email: saadamahmoud525@outlook.com  
LinkedIn: [https://www.linkedin.com/in/saad-ahmed-mahmoud/]
