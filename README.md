# Internship Portal

A Django-based web application for managing intern and volunteer applications. This portal provides a comprehensive system for applicants to submit their information and for administrators to review and manage applications.

## Features

### For Applicants
- **Home Page**: Attractive landing page with information about opportunities
- **Application Form**: Comprehensive registration form with all necessary fields
- **File Upload**: Resume/CV upload functionality
- **Form Validation**: Client and server-side validation
- **Success Messages**: Confirmation of successful application submission

### For Administrators
- **Admin Dashboard**: Overview of all applications with statistics
- **Search & Filter**: Advanced filtering by status, position type, and search terms
- **Application Details**: Detailed view of individual applications
- **Status Management**: Approve, reject, or update application status
- **Admin Notes**: Add notes and comments for each application
- **Pagination**: Handle large numbers of applications efficiently

## Technology Stack

- **Backend**: Django 5.2.4
- **Frontend**: Bootstrap 5.3.0, Font Awesome 6.0.0
- **Database**: SQLite (default), can be configured for PostgreSQL/MySQL
- **File Storage**: Local file system for resume uploads

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Step 1: Clone or Download the Project
```bash
# If you have the project files, navigate to the project directory
cd /path/to/your/project
```

### Step 2: Create Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run Database Migrations
```bash
python manage.py migrate
```

### Step 5: Create Admin User
```bash
python manage.py createsuperuser
# Follow the prompts to create an admin account
```

### Step 6: Run the Development Server
```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

## Usage

### For Applicants
1. Visit the home page at `http://127.0.0.1:8000/`
2. Click "Apply Now" or navigate to the registration form
3. Fill out all required fields in the comprehensive application form
4. Upload your resume (optional)
5. Submit the application
6. You'll receive a confirmation message

### For Administrators
1. Login to the admin panel at `http://127.0.0.1:8000/admin/`
   - Username: `admin`
   - Password: `admin123`
2. Access the dashboard at `http://127.0.0.1:8000/admin-dashboard/`
3. Use the search and filter options to find specific applications
4. Click on individual applications to view details
5. Update application status and add admin notes
6. Use quick action buttons for common tasks

## Project Structure

```
internship_portal/
├── manage.py
├── requirements.txt
├── README.md
├── internship_portal/          # Main project settings
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── registration/              # Main application
│   ├── __init__.py
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── templates/                 # HTML templates
│   ├── base.html
│   └── registration/
│       ├── home.html
│       ├── register.html
│       ├── admin_dashboard.html
│       └── applicant_detail.html
├── media/                    # Uploaded files
└── db.sqlite3               # Database file
```

## Database Models

### Applicant Model
- **Personal Information**: Name, email, phone, date of birth
- **Application Details**: Position type, department, start/end dates
- **Education & Experience**: Current education, institution, graduation year, relevant experience
- **Motivation & Skills**: Why they want to join, skills and competencies
- **Additional Information**: Resume upload, cover letter
- **Application Status**: Pending, approved, or rejected with admin notes

## Customization

### Adding New Fields
1. Modify the `Applicant` model in `registration/models.py`
2. Create and run migrations: `python manage.py makemigrations && python manage.py migrate`
3. Update the form in `registration/forms.py`
4. Update templates to display new fields

### Styling Changes
- Modify `templates/base.html` for global styling
- Update individual template files for specific page styling
- Bootstrap classes are used throughout for responsive design

### Adding New Features
- Create new views in `registration/views.py`
- Add URL patterns in `registration/urls.py`
- Create corresponding templates in `templates/registration/`

## Security Features

- CSRF protection on all forms
- File upload validation
- Admin authentication required for sensitive operations
- Input validation and sanitization
- Secure file handling for resume uploads

## Production Deployment

For production deployment, consider:

1. **Database**: Use PostgreSQL or MySQL instead of SQLite
2. **Static Files**: Configure proper static file serving
3. **Media Files**: Use cloud storage (AWS S3, etc.) for file uploads
4. **Environment Variables**: Store sensitive settings in environment variables
5. **HTTPS**: Enable SSL/TLS encryption
6. **Web Server**: Use Gunicorn with Nginx

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the MIT License.

## Support

For questions or issues, please create an issue in the project repository or contact the development team. 