# Tableau Dashboard Integration Plan

## Objective
The objective of this task is to integrate four key interactive Tableau Public dashboards into the existing Django Smart Farming Dashboard application, replacing all previous placeholder references to Power BI.

The dashboards integrated are:
1. **Crop Analysis Dashboard**
2. **Weather Analytics Dashboard**
3. **Yield Prediction Dashboard**
4. **Farmer Statistics Dashboard**

---

## Why Tableau is being Integrated
Tableau Public provides rich, interactive, and high-fidelity visual representations of agricultural data, making it easier for farmers and stakeholders to consume complex intelligence:
- **Rich Visual Analytics:** Interactive charts for crop distribution, seasonal trends, and predictive modeling results.
- **Ease of Access:** Seamless public link embedding without complex backend auth configurations.
- **Production-Ready Visuals:** Immediate rendering of beautiful dashboards, optimized for modern browsers.

---

## Files Modified
1. `reports/views.py`: Modified to import Django's redirect module and updated the default reports view to redirect to Crop Analysis. Added views for each of the four Tableau dashboards that inject their respective URLs and metadata through context variables.
2. `reports/urls.py`: Updated URL routes to register sub-paths `/reports/crop/`, `/reports/weather/`, `/reports/yield/`, and `/reports/farmers/`.
3. `templates/base.html`: Replaced the singular "Reports (BI)" navigation item with a collapsible Bootstrap Accordion menu containing links to the four dashboards. Added transition styling for arrow animations.

---

## URLs Created
- `/reports/` (Redirects to Crop Analysis Dashboard)
- `/reports/crop/`
- `/reports/weather/`
- `/reports/yield/`
- `/reports/farmers/`

---

## Templates Created
- `templates/reports/crop.html`: Embedded with Crop Analysis Tableau viz URL.
- `templates/reports/weather.html`: Embedded with Weather Analytics Tableau viz URL.
- `templates/reports/yield.html`: Embedded with Yield Prediction Tableau viz URL.
- `templates/reports/farmers.html`: Embedded with Farmer Statistics Tableau viz URL.

All templates extend `base.html` and are wrapped in premium Bootstrap card layouts. They feature:
- Title and descriptive panels.
- Refresh action buttons.
- A responsive, horizontally-scrollable overflow container to allow touch and drag interaction on smaller devices (tablets and mobile screens) without scaling or text compression.

---

## Testing Procedure
1. **System Health Verification:** Run the command `python manage.py check` to check for syntax and configuration issues.
2. **Visual Inspection:**
   - Run the development server: `python manage.py runserver`
   - Log in and verify that the sidebar menu displays the "Reports" drop-down.
   - Click on each dashboard item to check if the specific page renders and initiates the Tableau Public loader successfully.
3. **Responsive Checks:**
   - Resize browser to mobile breakpoints to ensure that the sidebar collapses into a hamburger menu and the Tableau dashboard container remains scrollable horizontally.
   - Use the "Refresh Report" button to ensure it reloads the iframe successfully.

---

## Deployment Considerations
- **Tableau Public Availability:** Ensure that the Tableau dashboards remain published as public dashboards. If privacy is required in the future, Tableau Embedded Analytics with Single Sign-On (SSO) authentication should be configured.
- **Security Headers:** Verify that `X-Frame-Options` on Tableau side is configured to allow embedding on the domain where Django is hosted (Tableau Public allows embedding by default).
- **Iframes Permissions:** We use standard `allowfullscreen="true"` tags to enable full-screen presentation mode for presentations.
