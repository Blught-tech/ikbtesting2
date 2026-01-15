## Secure Task Manager - Django Framework
A high-security Django application featuring audit logging, and zero-vulnerability dependency management.

## Installation & Setup:
Follow these steps to get the environment running on your local machine:

1. Clone the Repository:
git clone (https://github.com/afiqdan414-design/IKB-21503-DjangoFrameworks)
cd into the repository-folder

2. Create and Activate a Virtual Environment:
python3 -m venv venv
source venv/bin/activate
On Windows use: venv\Scripts\activate

4. Install Dependencies:
pip install -r requirements.txt
   
5. Initialize the Database:
python manage.py migrate

If you pull new changes (like adding task attachments), apply the latest migrations:
python manage.py migrate

6. Create an Admin User (For Audit Log access):
python manage.py createsuperuser

## How to Run the App

1. Start the Development Server:
python manage.py runserver

Uploaded task attachments are saved under the `uploads/` folder (outside the web root) and served at `/media/`.

2. Access the Application:
HomePage: http://127.0.0.1:8000/

Admin Portal: http://127.0.0.1:8000/admin/

## Functional Requirements Implemented:

* Audit Logging: Every task creation and status change is manually hooked into the Django LogEntry system.

* Data Isolation: Strict owner filtering in views ensures users cannot see or modify tasks belonging to others.

* CSRF Protection: All state-changing actions (Task Toggle, Logout) use POST requests with CSRF tokens to prevent cross-site attacks.

* Role Separation: Admin and User logout flows are isolated to prevent unauthorized navigation between roles.

* Secure UI/UX: A unified dark theme applied across all user-facing pages for consistent looks.

## Security Requirements Implemented (Mandatory):

Configuration Security (Requirement #7)
* **Environment Isolation**: Sensitive keys (SECRET_KEY, DB_CREDENTIALS) are stored in `.env` files and never committed to version control.
* **Hardened Production Settings**: `DEBUG` is set to `False` and password validation is strictly enforced to prevent weak credentials.

Audit Logging (Requirement #8)
* **Failed Login Interception**: Custom Django signals monitor and record failed login attempts.
* **Administrator Oversight**: All security events are logged to the Django Admin dashboard for transparent auditing.
* **User Notification**: The login interface explicitly notifies users that all access attempts are recorded.

Dependency Scanning (Requirement #9)
* **Zero Vulnerabilities**: The project has been dual-scanned using `pip-audit` and the Snyk Web Interface.
* **Verified Libraries**: All third-party packages are pinned to secure versions in `requirements.txt`.

Output Encoding & XSS Prevention (Requirement #10)
* **Auto-Escaping**: All user-generated content and system messages (like account creation success prompts) are rendered via the Django template engine, which automatically encodes HTML entities to block XSS attacks.
* **Template Inheritance**: Used a centralized `base.html` skeleton to ensure security headers and safe rendering logic are applied consistently across the Home, Login, and Register pages.
