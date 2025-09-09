# MimSoft Corporation Website

A professional Django-based website for MimSoft Corporation, a software development and digital solutions company.

## 🚀 Features

- **Modern, Responsive Design** - Built with Bootstrap 5 and custom CSS
- **Modular Django Apps** - Well-organized structure for easy maintenance
- **Professional Content Management** - Admin interface for managing all content
- **Contact Form with reCAPTCHA** - Spam protection and GDPR compliance
- **Portfolio Management** - Showcase projects with filtering capabilities
- **Team Management** - Display team members by department
- **Testimonials System** - Client feedback with featured highlighting
- **Service Catalog** - Organized service offerings by category

## 🏗️ Project Structure

```
mimsoft_co/
├── mimsoft_co/          # Main project configuration
│   ├── settings.py      # Django settings
│   ├── urls.py          # Main URL configuration
│   └── admin.py         # Admin site customization
├── core/                # Core app (homepage, about)
├── services/            # Services management
├── team/                # Team member management
├── projects/            # Portfolio/projects
├── testimonials/        # Client testimonials
├── contact/             # Contact form handling
├── templates/           # HTML templates
├── static/              # Static files (CSS, JS, images)
├── media/               # User-uploaded files
└── requirements.txt     # Python dependencies
```

## 🛠️ Technology Stack

- **Backend**: Django 4.2.7
- **Frontend**: Bootstrap 5, HTML5, CSS3, JavaScript
- **Database**: SQLite (development), PostgreSQL (production ready)
- **Forms**: Django Crispy Forms with Bootstrap 5 styling
- **Security**: reCAPTCHA v3 integration
- **Icons**: Font Awesome 6
- **Fonts**: Google Fonts (Inter)

## 📋 Requirements

- Python 3.8+
- Django 4.2.7
- Pillow (for image handling)
- django-crispy-forms
- crispy-bootstrap5
- django-recaptcha

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd mimsoft_co
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

4. **Set up environment variables**
   ```bash
   # Create .env file with your configuration
   SECRET_KEY=your-secret-key
   DEBUG=True
   RECAPTCHA_PUBLIC_KEY=your-recaptcha-public-key
   RECAPTCHA_PRIVATE_KEY=your-recaptcha-private-key
   ```

5. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the website**
   - Website: http://127.0.0.1:8000/
   - Admin: http://127.0.0.1:8000/admin/

## 🎯 Key Features

### Homepage
- Hero section with company tagline and call-to-action
- Achievement statistics display
- Featured services, projects, team members, and testimonials
- Professional design with smooth animations

### Services
- Categorized service listings
- Detailed service pages with process information
- Professional service descriptions

### Portfolio
- Project showcase with filtering by category and service
- Project details with client information
- Image galleries and project descriptions

### Team
- Team member profiles organized by department
- Professional photos and LinkedIn integration
- Role and bio information

### Testimonials
- Client feedback display
- Featured testimonial highlighting
- Project linking capabilities

### Contact Form
- Professional contact form with reCAPTCHA
- GDPR compliance with consent checkbox
- Multiple contact methods display

## 🔧 Configuration

### reCAPTCHA Setup
1. Get your reCAPTCHA keys from [Google reCAPTCHA](https://www.google.com/recaptcha/)
2. Update the settings in `mimsoft_co/settings.py`:
   ```python
   RECAPTCHA_PUBLIC_KEY = 'your-public-key'
   RECAPTCHA_PRIVATE_KEY = 'your-private-key'
   ```

### Company Information
Update company details in `mimsoft_co/settings.py`:
```python
COMPANY_NAME = 'Your Company Name'
COMPANY_TAGLINE = 'Your Company Tagline'
COMPANY_MISSION = 'Your Company Mission'
COMPANY_ACHIEVEMENTS = {
    'projects_completed': 50,
    'client_satisfaction': 98,
    'years_experience': 5,
    'team_members': 15,
}
```

## 📱 Responsive Design

The website is fully responsive and optimized for:
- Desktop computers
- Tablets
- Mobile devices
- All modern browsers

## 🎨 Customization

### Colors
Update CSS variables in `templates/base.html`:
```css
:root {
    --primary-color: #2563eb;
    --secondary-color: #1e40af;
    --accent-color: #3b82f6;
    --text-dark: #1f2937;
    --text-light: #6b7280;
    --bg-light: #f8fafc;
}
```

### Content
- Update company information in Django admin
- Modify templates for branding changes
- Add custom CSS for specific styling needs

## 🚀 Deployment

### Production Settings
1. Set `DEBUG = False`
2. Configure production database (PostgreSQL recommended)
3. Set up static file serving
4. Configure media file storage
5. Set secure `SECRET_KEY`
6. Configure `ALLOWED_HOSTS`

### Static Files
```bash
python manage.py collectstatic
```

### Database
```bash
python manage.py migrate
```

## 📊 Admin Interface

Access the admin interface at `/admin/` to manage:
- Services and categories
- Team members and departments
- Projects and portfolio items
- Client testimonials
- Contact form submissions

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

For support and questions:
- Email: info@mimsoft.com
- Phone: +1 (555) 123-4567
- Website: https://mimsoft.com

## 🔮 Future Enhancements

- Blog system for company updates
- E-commerce integration for service packages
- Advanced analytics and reporting
- Multi-language support
- API endpoints for mobile apps



- Advanced search functionality
- Newsletter subscription system

---

**Built with ❤️ by MimSoft Corporation**
