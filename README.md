# Surveillance-House

A web application for managing and selling CCTV products.

## Features

- Product inventory management for CCTV cameras and accessories
- User registration, login, and authentication
- Product detail and listing pages
- Admin interface for managing products and sales
- Newsletter subscription (optional)
- Responsive frontend with modern UI

## Tech Stack

- Python 3
- Django (backend framework)
- HTML, CSS, JavaScript (frontend)
- Bootstrap (UI styling)
- SQLite (default database, can be changed)

## Project Structure

```
SurveillanceHouse/
├── inventory/         # Product and inventory management
├── sale/              # Sales and order management
├── users/             # User authentication and profiles
├── static/            # Static files (CSS, JS, images)
├── media/             # Uploaded media (product images)
├── SurveillanceHouse/ # Project settings and URLs
├── manage.py          # Django management script
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone https://github.com/yourusername/Surveillance-House.git
   cd Surveillance-House
   ```

2. **Create a virtual environment and activate it:**
   ```
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Apply migrations:**
   ```
   python manage.py migrate
   ```

5. **Create a superuser (admin):**
   ```
   python manage.py createsuperuser
   ```

6. **Run the development server:**
   ```
   python manage.py runserver
   ```

7. **Access the app:**
   - Visit `http://127.0.0.1:8000/` in your browser.

## 📸 Screenshots
![SurveillanceHouse](https://github.com/user-attachments/assets/d3b83579-af8d-4fcc-8503-cc97d2573915)


## License

This project is licensed under the MIT License.
