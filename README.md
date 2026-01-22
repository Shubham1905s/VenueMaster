# VenueMaster

A comprehensive venue management system built with Django that facilitates booking and management of auditoriums and seminar halls.

## 🎯 Features

- **Dual Venue Management**: Manage both Auditorium and MV Hall bookings
- **User Authentication**: Secure user registration and login system
- **Real-time Booking**: Check availability and book time slots instantly
- **Conflict Detection**: Automatic detection of booking conflicts
- **File Management**: Upload and manage venue-related documents
- **Admin Interface**: Django admin integration for easy management
- **Responsive Design**: Clean, user-friendly interface

## 🏗️ Project Structure

```
VenueMaster/
├── home/                 # Django project configuration
│   ├── settings.py      # Project settings
│   ├── urls.py          # Main URL configuration
│   └── wsgi.py          # WSGI configuration
├── myapp/               # Main application
│   ├── models.py        # Database models
│   ├── views.py         # View functions
│   ├── urls.py          # App URL configuration
│   ├── forms.py         # Django forms
│   ├── managers.py      # Custom user managers
│   ├── migrations/      # Database migrations
│   └── templates/       # HTML templates
├── mvhall_uploads/      # File uploads for MV Hall
├── db.sqlite3          # SQLite database
└── manage.py           # Django management script
```

## 🚀 Installation

### Prerequisites
- Python 3.8+
- Django 5.0+
- SQLite3

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd VenueMaster
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # Linux/Mac
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install django
   ```

4. **Run database migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Main application: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

## 📋 Database Models

### Booking Models
- **Booking**: Auditorium booking management
- **MVHallBooking**: MV Hall booking management

### Information Models
- **AuditoriumInfo**: Auditorium details (capacity, facilities, description)
- **MVHallInfo**: MV Hall details (capacity, facilities, description)

### File Management
- **AuditoriumFiles**: File uploads for auditorium
- **MVHallFiles**: File uploads for MV Hall

## 🔐 Authentication System

The application includes:
- User registration and login
- Session-based authentication
- Protected views for booking management
- Custom user management capabilities

## 📅 Booking System Features

### Auditorium Booking
- View existing bookings
- Check time slot availability
- Book new time slots
- Conflict detection and prevention

### MV Hall Booking
- Similar functionality as Auditorium
- Separate booking management
- Independent file upload system

## 🎨 Templates

The application uses the following key templates:
- `home.html` - Main dashboard
- `audi.html` - Auditorium booking interface
- `MVhall.html` - MV Hall booking interface
- `registerPage.html` - User registration
- `loginPage.html` - User login
- `base.html` - Base template with common elements

## 🔧 Configuration

### Database Configuration
- Uses SQLite3 by default
- Database file: `db.sqlite3`
- Configured in `home/settings.py`

### Static Files
- Static URL: `/static/`
- Static root: `myapp/static/`

### Email Configuration (Optional)
Email settings are commented out in `settings.py` but can be configured for:
- User registration emails
- Booking confirmations
- Notifications

## 📝 Usage

1. **Register an account** or use existing credentials
2. **Login** to access the booking system
3. **View venue information** for both Auditorium and MV Hall
4. **Check availability** by viewing existing bookings
5. **Book time slots** by selecting date and time range
6. **Upload files** related to your booking if needed

## 🛠️ Development

### Running Tests
```bash
python manage.py test
```

### Creating New Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Django Admin
Access the admin panel at `/admin` to:
- Manage users
- View/edit bookings
- Update venue information
- Manage uploaded files

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📞 Support

For support and queries:
- Create an issue in the repository
- Contact the development team

---

**Built with Django 5.0.1** | **SQLite Database** | **Python 3.8+**