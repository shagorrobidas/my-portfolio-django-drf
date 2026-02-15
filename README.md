# 🌟 Django Portfolio Suite

> A premium, modern, and professional portfolio application powered by **Django 6.0** and **Django REST Framework**.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-6.0-092E20?style=for-the-badge&logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/DRF-3.16-A51111?style=for-the-badge&logo=django&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-Modern-1572B6?style=for-the-badge&logo=css3&logoColor=white)

---

## ✨ Core Features

### 👤 Dynamic Profile Management
- Fully customizable profile through Django Admin.
- Social integration (GitHub, LinkedIn).
- Modern "About Me" sections with extended content support.

### 📁 Project Showcase
- Interactive project grid with **Category Filtering**.
- Detailed project documentation including tags, source links, and live demos.
- Robust media handling for project previews.

### ✍️ Professional Blog
- Clean, focused blogging experience.
- Category-based filtering and rich media support.
- Optimized for readability and engagement.

### 📄 Digital Resume
- Structured tracking for **Experience** and **Education**.
- Dynamic **Skills Matrix** with proficiency markers.
- Organized layout for professional presentation.

### 🚀 Premium User Experience
- **The Stellar Nexus Preloader**: A unique 3D orbital animation for a high-end first impression.
- **Dark Mode First**: A sleek, accessibility-focused "Dark Portfolio UI".
- **Responsive Design**: Fully optimized for Mobile, Tablet, and Desktop.

---

## 🛠️ Technical Stack

- **Backend**: Python 3.10+, Django 6.0
- **API Layer**: Django REST Framework (DRF)
- **Database**: SQLite (Production-ready for small instances, easily swappable)
- **Styling**: Modern Vanilla CSS with CSS Variables and 3D Transforms
- **Media**: Pillow for high-quality image processing

---

## 🚀 Quick Start

### 1. Clone & Setup Environment
```bash
git clone <repository-url>
cd "my protfolio"
python -m venv venv
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate  # Windows
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Initialize Database
```bash
python manage.py migrate
python manage.py createsuperuser
```

### 4. Launch Application
```bash
python manage.py runserver
```
Visit `http://127.0.0.1:8000/` to see your portfolio and `http://127.0.0.1:8000/admin/` to manage your data.

---

## 📂 Project Structure

- `/core`: Project configuration and settings.
- `/main`: Core profile and global settings logic.
- `/project`: Portfolio and project management.
- `/resume`: Professional history and skills.
- `/blog`: Content management and blogging logic.
- `/api`: Centralized API routing and views.

---

### 🤝 Contributing
Feel free to fork this project and submit pull requests for any features or bug fixes.

### 📜 License
This project is licensed under the MIT License - see the LICENSE file for details.
