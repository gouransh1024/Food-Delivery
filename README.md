# 🍔 FDelivery - Online Food Delivery Web Application

FDelivery is a full-featured web application built with **Python** and **Django 5.0**. It allows users to browse food menus, add items to their shopping cart, manage quantities, place orders, and maintain user profiles.

---

## ✨ Features

- **🍽️ Dynamic Food Menu**: Browse delicious dishes with images, prices, and descriptions.
- **🛒 Interactive Shopping Cart**:
  - Add items directly to cart from the menu.
  - Automatic quantity increments and session persistence.
  - Real-time subtotal and grand total calculation.
  - Easy item removal and order checkout flow.
- **👤 User Authentication & Profiles**:
  - Secure User Registration, Login, and Logout.
  - User profile management with customizable avatar/profile picture, title, and bio.
- **⚡ Modern Responsive UI**:
  - Clean, responsive layouts across desktop and mobile devices.
  - Interactive animations powered by GSAP and Remix Icons.
- **🛠️ Admin Dashboard**:
  - Manage menu items, prices, descriptions, and product images using Django's built-in administration panel.

---

## 🛠️ Tech Stack

- **Backend**: Python 3.12, Django 5.0
- **Database**: SQLite3
- **Frontend**: HTML5, Vanilla CSS3, JavaScript, GSAP, Remix Icons
- **Image Processing**: Pillow (PIL)

---

## 🚀 Getting Started

### Prerequisites

Ensure you have Python 3.12+ and Git installed on your system:
```bash
python --version
git --version
```

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/gouransh1024/Food-Delivery.git
   cd Food-Delivery
   ```

2. **Create and activate a virtual environment:**
   - **Windows:**
     ```bash
     python -m venv env
     env\Scripts\activate
     ```
   - **macOS / Linux:**
     ```bash
     python3 -m venv env
     source env/bin/activate
     ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply database migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

6. **Open your browser:**
   Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 📂 Project Structure

```text
Food-Delivery/
├── fdelivery/              # Django project settings & URL configuration
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── home/                   # Core application
│   ├── migrations/         # Database migrations
│   ├── static/             # Static assets (CSS, JS, SVGs, images)
│   ├── templates/          # HTML templates (home, menu, cart, profile, auth)
│   ├── admin.py            # Model registration in admin
│   ├── forms.py            # User registration & profile forms
│   ├── models.py           # Product, Cart, and Profile models
│   ├── views.py            # View controllers and cart logic
│   └── signals.py          # Automatic profile creation signals
├── media/                  # Uploaded food and user profile images
├── db.sqlite3              # SQLite database (includes sample food items)
├── manage.py               # Django CLI utility
├── requirements.txt        # Python package dependencies
└── README.md               # Project documentation
```

---

## 🔑 Default Routes

| URL | Description |
| --- | ----------- |
| `/` | Landing / Home Page |
| `/home/` or `/menu/` | Food Menu & Add to Cart |
| `/cart/` | Shopping Cart & Order Summary |
| `/login/` | User Login |
| `/sign/` | New User Registration |
| `/profile/` | View and Edit Profile |
| `/admin/` | Django Admin Dashboard |

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
