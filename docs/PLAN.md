# Developer Implementation Plan (PLAN.md)

Welcome to the developer documentation for the **Smart Farming Dashboard**! This document explains what was built in this initial phase, the underlying technical decisions, and how to verify, configure, and expand the code.

---

## 1. What was Implemented
In this phase, we established the fundamental architecture and user security framework for the application:
1. **Django Project Skeleton:** Created a modular application architecture consisting of seven core apps (`accounts`, `dashboard`, `recommendations`, `predictions`, `reports`, `notifications`, `feedback`).
2. **Custom User Authentication:** Designed a Custom User model extending Django's `AbstractUser` to support roles (`Farmer` vs. `Admin`) and built combined edit actions for `FarmerProfile` details.
3. **Database Schema Setup:** Designed and migrated standard relational database structures representing farms, crop categories, meteorological metrics, recommendations, and ratings.
4. **Cohesive Base Layout & Responsive Styling:** Designed a premium agricultural user interface using modern Google fonts (Outfit), custom green-earth css variables, interactive sidebar toggles, and responsive canvas visualizers.
5. **Interactive Reports Panel:** Integrated Microsoft's public sample Power BI iframe dashboard inside a responsive container with filter widgets for regions and crop seasons.
6. **Form Persistence & Mock Simulators:** Implemented views and templates for crop recommendations and yield calculations using persistence logs and baseline rule simulators.

---

## 2. Why it is Needed
- **Role-Based Workflows:** Farmers need isolated dashboards and data storage to track their soil characteristics, whereas Administrators need central views to review satisfaction scores.
- **Robust Database Foundation:** Defining concrete models (such as `Farm`, `WeatherData`, `Recommendation`, and `Feedback`) early protects data integrity and guarantees clean table migrations.
- **Professional Visual Evaluation:** College evaluators expect state-of-the-art interactive charts (Chart.js) and active analytics interfaces (Power BI) instead of static mockups.

---

## 3. Prerequisites
To run this application, make sure you have:
1. Python 3.10 or higher.
2. An active virtual environment containing dependencies defined in `requirements.txt` (Pillow, Django, REST framework, scikit-learn, etc.).

---

## 4. Step-by-Step Execution Plan
1. **Virtual Environment & Dependencies:** Initialize venv and run package installs.
2. **StartProject & startapp:** Generate project layout and individual apps folders.
3. **Settings & Schema Configurations:** Modify `settings.py` for apps inclusion, static/media roots, and `AUTH_USER_MODEL` declaration.
4. **Implement Models & Forms:** Build tables in `models.py` and register forms targeting user input fields.
5. **Implement Views & Routings:** Map requests to templates inside each app's `views.py` and hook up `urls.py`.
6. **Create Templates & Styling Assets:** Write styles sheet and HTML layouts using Bootstrap 5.
7. **Database Migrations:** Apply model structures to SQLite.
8. **Create Administrator Superuser:** Seed basic credentials for quick evaluation.

---

## 5. Folder Structure Changes
The following folder layout has been created:
```
smart_farming/
│
├── accounts/               # Custom User & Profile management
│   ├── forms.py            # Login, registration, and edit profile forms
│   ├── models.py           # User and FarmerProfile models with signal hooks
│   └── views.py            # Auth view routing controllers
├── dashboard/              # Home portal statistics & charts
│   ├── models.py           # Farm, Crop, and WeatherData models
│   └── views.py            # Landing view & stats calculator
├── recommendations/        # Crop recommendation inputs & runs
│   ├── forms.py            # Soil chemistry forms
│   ├── models.py           # Recommendation run history logs
│   └── views.py            # Persistent recommendations view
├── predictions/            # Crop yield predictions inputs & logs
│   ├── forms.py            # Crop yield factors form
│   ├── models.py           # YieldPrediction run history logs
│   └── views.py            # Yield prediction regression calculator
├── reports/                # Embedded analytics
│   └── views.py            # Power BI reports screen controller
├── feedback/               # Farmer ratings and reviews
│   ├── forms.py            # Dual feedback comments & rating stars form
│   ├── models.py           # Feedback text & Star Rating models
│   └── views.py            # Role-based review portal view
├── static/
│   └── css/
│       └── style.css       # Deep green styling variables & transitions
├── templates/              # Shared HTML documents
│   ├── base.html           # Frame template containing navigation side-drawer
│   ├── accounts/           # Login, Register, Profile edit screens
│   ├── dashboard/          # Public landing & farmer stats screens
│   ├── recommendations/    # Recommender form screen
│   ├── predictions/        # Predictor form screen
│   ├── reports/            # Power BI reports screen
│   └── feedback/           # Feedback & reviews dashboard
├── docs/
│   └── PLAN.md             # This document
├── requirements.txt        # Package dependencies list
└── manage.py               # Django execution script
```

---

## 6. Database Migrations Required
The following initial migrations are configured and applied:
- **`accounts.0001_initial`:** Custom user table `User` and profile relation `FarmerProfile`.
- **`dashboard.0001_initial`:** Tables for `Crop`, `Farm`, and `WeatherData`.
- **`recommendations.0001_initial`:** Recommendation history logs.
- **`predictions.0001_initial`:** Yield estimation logs.
- **`feedback.0001_initial`:** `Feedback` and `Rating` tables.

To run migrations in any new environment:
```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 7. APIs Involved
While this phase focuses on Django Templates and forms for maximum visual consistency, the backend is equipped with Django REST Framework for API compliance.
- Future phases will add API end-points (e.g. `/api/recommendations/`, `/api/predictions/`) returning serialized JSON responses.

---

## 8. Testing Checklist
Verify that:
- [x] Unauthenticated users landing on `http://127.0.0.1:8000/` are shown the public layout.
- [x] Attempting to access sub-modules redirects users to the login portal.
- [x] Registering a new farmer creates a User instance and an inline FarmerProfile table.
- [x] Inputting correct credentials logs in the user and redirects to the statistics page.
- [x] Logging in as an administrator shows the "ADMIN MODE" indicator and accesses the Django Admin Panel.
- [x] Crop recommendation and yield estimation forms persist metrics to the tables on save.
- [x] Profile page correctly updates usernames, phone numbers, and location details.

---

## 9. Deployment Considerations (Render & PostgreSQL)
When deploying the dashboard:
1. **Database:** Use Render's managed PostgreSQL database. Configure it via `dj-database-url` in `settings.py`.
2. **Environment Variables:** Define secret keys and debug states in a `.env` file (never commit secrets to GitHub).
3. **Static Assets:** Use Django's `collectstatic` script. Gunicorn acts as the production server.

---

## 10. Future Improvements
- **Integration of Random Forest Models:** Replace placeholder rules in views with loaded `.joblib` models trained on scikit-learn.
- **Live Notifications Delivery:** Integrate django email backend configs and map architectural logic for Twilio SMS/WhatsApp notifications.
- **Power BI Embed Security:** Replace public iframe embeds with Power BI Embedded Azure REST API tokens for secure access.
