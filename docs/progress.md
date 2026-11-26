# EduGenie Project Progress

# Day 3 — Responsive Navbar

## Goal

Make the EduGenie Navbar responsive for desktop and mobile screens.

## Completed

- Learned Responsive Web Design.
- Learned CSS Media Queries.
- Implemented Mobile Navbar.
- Added Hamburger Menu Button.
- Added JavaScript logic for opening and closing the mobile menu.
- Used `querySelector()` to select HTML elements.
- Used `addEventListener()` to detect the menu button click.
- Used `classList.toggle()` to add and remove the `active` class.
- Used CSS `.nav-links.active` to display the mobile menu.
- Learned how CSS rules can override each other.
- Made the navigation links appear vertically on mobile screens.

## New Concepts

- `@media`
- `max-width`
- `display: flex`
- `display: none`
- `querySelector()`
- `addEventListener()`
- `classList.toggle()`
- `.nav-links.active`
- Responsive Web Design
- CSS Override

## Viva Questions

### 1. What is Responsive Web Design?

Responsive Web Design means creating a website that automatically adjusts its layout according to the screen size of the device.

### 2. What is a Media Query?

A Media Query is a CSS feature used to apply different styles for different screen sizes.

### 3. Why do we use display:flex?

`display:flex` is used to arrange elements in a row or column and control their alignment and spacing easily.

### 4. What does classList.toggle() do?

`classList.toggle()` adds a class if it is not present and removes it if it is already present.

## Problems

- None

## Status

Responsive Navbar Completed ✅


# Day 4 — 14/08/26

## Goal

Complete the main frontend sections, connect Login/Register with Flask and SQLite, implement authentication, and create a responsive Dashboard.


## 1. Landing Page

### Completed

- Completed the main EduGenie Landing Page.
- Created the Hero Section.
- Added EduGenie heading and description.
- Added Get Started and Learn More buttons.
- Added responsive styling for the Hero Section.
- Improved spacing between different sections.


## 2. Features Section

### Completed

- Created the Features Section.
- Created multiple feature cards.
- Used CSS Grid to arrange feature cards.
- Used:

`grid-template-columns: repeat(3, 1fr);`

for desktop layout.

- Used:

`grid-template-columns: 1fr;`

for mobile layout.
- Added spacing using `gap`.
- Added `box-shadow` to feature cards.
- Added hover animation using `transform: translateY()`.
- Made the Features Section responsive.


## 3. About Section

### Completed

- Created the About EduGenie Section.
- Added information explaining the purpose of EduGenie.
- Connected the About section with the Navbar.
- Used `id="about"` for navigation.
- Adjusted the spacing between About and Features sections.


## 4. Footer Section

### Completed

- Created a professional Footer.
- Added EduGenie name and tagline.
- Added navigation links.
- Added copyright information.
- Made the Footer responsive.


## 5. Login Page

### Completed

- Created `login.html`.
- Added Login form.
- Added email input.
- Added password input.
- Added Login button.
- Added responsive Login page styling.
- Connected Login page with Flask.


## 6. Register Page

### Completed

- Created `register.html`.
- Added Name input.
- Added Email input.
- Added Password input.
- Added Register button.
- Added responsive Register page styling.
- Connected Register page with Flask.


## 7. Flask Backend

### Completed

- Created Flask application using `Flask`.
- Created the Home route `/`.
- Created the Login route `/login`.
- Created the Register route `/register`.
- Created the Dashboard route `/dashboard`.
- Used `render_template()` to display HTML pages.
- Used `request.form` to receive form data.
- Learned about GET and POST requests.
- Used:

`methods=["GET", "POST"]`

for form submission.


## 8. SQLite Database

### Completed

- Added SQLite database using Python's `sqlite3` module.
- Created `database.db`.
- Created the `users` table.
- Created a reusable `get_db_connection()` function.
- Created a `create_users_table()` function.
- Used `connection.commit()` to save database changes.
- Used `connection.close()` to close the database connection.

### Database Concepts Learned

- Primary Key
- Auto Increment
- NOT NULL
- UNIQUE
- SQL INSERT
- SQL SELECT
- Database Connection


## 9. Registration System

### Completed

- Connected Register form with Flask.
- Used POST request to receive registration data.
- Used `request.form` to get user information.
- Inserted user information into SQLite database.
- Tested registration successfully.
- Confirmed that registered users are stored in the database.


## 10. Password Hashing

### Completed

- Learned why passwords should not be stored as plain text.
- Imported password hashing functions from `werkzeug.security`.
- Used `generate_password_hash()`.
- Converted the user's password into a hash before storing it.
- Stored the hashed password in SQLite.
- Tested the system successfully.
- Confirmed that the database stores the hashed password instead of the original password.

### Password Flow

User Password
        ↓
generate_password_hash()
        ↓
Hashed Password
        ↓
SQLite Database


## 11. Login Authentication

### Completed

- Updated the `/login` route to accept GET and POST requests.
- Received email from the Login form.
- Received password from the Login form.
- Searched the database for the entered email.
- Used `check_password_hash()` to verify the password.
- Tested correct login credentials successfully.
- Tested incorrect password successfully.
- Tested incorrect email successfully.

### Login Result

Correct Email + Password
        ↓
Login Successful ✅

Wrong Email / Password
        ↓
Invalid email or password ❌


## 12. Dashboard

### Completed

- Created `dashboard.html`.
- Created Flask `/dashboard` route.
- Connected successful login to the Dashboard.
- Replaced the temporary `Login Successful!` message with the Dashboard.
- Created Dashboard Navbar.
- Added Home link.
- Added Dashboard link.
- Added Logout link.
- Created Dashboard Welcome Card.
- Added Explore Features button.

### Dashboard Features Added

- 📚 Subjects
- 📝 Notes
- 🤖 AI Doubt Solver
- 📊 Attendance
- ✅ To-Do List
- 📅 Study Planner


## 13. Dashboard UI

### Completed

- Designed Dashboard Navbar.
- Added EduGenie logo.
- Added navigation links.
- Added hover effects.
- Created professional Welcome Card.
- Added Dashboard feature cards.
- Added card shadows.
- Added card hover animations.
- Added proper spacing and layout.


## 14. Dashboard Responsive Design

### Completed

- Made Dashboard Navbar responsive.
- Made Dashboard Welcome Card responsive.
- Made Dashboard feature cards responsive.
- Used CSS Grid for Dashboard cards.
- Desktop layout uses:

`grid-template-columns: repeat(3, 1fr);`

- Mobile layout uses:

`grid-template-columns: 1fr;`

- Added mobile-specific spacing.
- Reduced heading size on mobile.
- Adjusted card padding for smaller screens.
- Fixed CSS override/order issue.
- Tested Dashboard responsiveness successfully.


# New Concepts Learned

## HTML

- Forms
- Input fields
- `name` attribute
- `method="POST"`
- `action`
- Semantic sections
- Navigation links
- Responsive HTML structure


## CSS

- CSS Grid
- `grid-template-columns`
- `gap`
- `box-shadow`
- `border-radius`
- `transition`
- `transform`
- Media Queries
- Responsive layouts
- CSS Override
- Mobile-first adjustments


## JavaScript

- `querySelector()`
- `addEventListener()`
- `classList.toggle()`


## Flask

- Flask application
- Routes
- `@app.route()`
- `render_template()`
- `request.form`
- GET request
- POST request
- Route methods
- Template rendering


## SQLite

- SQLite database
- Database connection
- Tables
- Primary Key
- Auto Increment
- UNIQUE
- NOT NULL
- INSERT
- SELECT
- `commit()`
- `close()`


## Authentication

- Password hashing
- `generate_password_hash()`
- `check_password_hash()`
- Login verification
- Registration system


# Current Project Flow

Landing Page
      ↓
Login Page
      ↓
Register Page
      ↓
Flask Backend
      ↓
Password Hashing
      ↓
SQLite Database
      ↓
Users Table
      ↓
Login Authentication
      ↓
Dashboard
      ↓
Dashboard Features


# Current Project Status

- Landing Page: ✅ Completed
- Responsive Navbar: ✅ Completed
- Hamburger Menu: ✅ Completed
- Features Section: ✅ Completed
- About Section: ✅ Completed
- Footer: ✅ Completed
- Login UI: ✅ Completed
- Register UI: ✅ Completed
- Flask Backend: ✅ Completed
- Flask Routes: ✅ Completed
- SQLite Database: ✅ Completed
- Users Table: ✅ Completed
- Registration System: ✅ Working
- Password Hashing: ✅ Working
- Login Authentication: ✅ Working
- Dashboard: ✅ Completed
- Dashboard Navbar: ✅ Completed
- Dashboard Welcome Card: ✅ Completed
- Dashboard Feature Cards: ✅ Completed
- Dashboard Responsive Design: ✅ Completed


# Next Milestone

## Subject Management

Planned Tasks:

- Create Subjects database table.
- Create Subject Management page.
- Add subjects from the Dashboard.
- Store subjects in SQLite.
- Display saved subjects.
- Add Edit Subject functionality.
- Add Delete Subject functionality.
- Connect Subject Management with Dashboard.


# Overall Progress

EduGenie currently has a working frontend, Flask backend,
SQLite database, registration system, password hashing,
login authentication and responsive Dashboard.

The next major milestone is:

Subject Management + SQLite Database Integration 🚀
 
 # Day 5 — 23/08/26

# EduGenie Project Progress

## Today's Learning & Work

### 1. Subject Management Started

- Started working on the Subject Management feature.
- Planned a separate Subject Management page for students.
- Created `subjects.html`.
- Added a Subject Management heading.
- Added an input field for entering subject names.
- Added an "Add Subject" button.
- Added navigation links to return to the Dashboard and Home page.

### 2. Subjects Database Table

- Created a `subjects` table in the SQLite database.
- Added the following fields:
  - `id`
  - `user_id`
  - `subject_name`
- Learned why `user_id` is required.
- Understood that each subject should belong to a specific student.

### 3. Flask Subject Route

- Created the `/subjects` Flask route.
- Learned how a single route can handle both GET and POST requests.
- Used:

`methods=["GET", "POST"]`

- Connected the `/subjects` route with `subjects.html`.

### 4. Dashboard Integration

- Connected the Subjects card on the Dashboard with `/subjects`.
- Made the Subjects card clickable.
- Clicking the Subjects card now opens the Subject Management page.

### 5. HTML/CSS Debugging

- Found a problem caused by using the `dashboard-card` class twice.
- The outer `<div>` and inner `<a>` both had the same `dashboard-card` class.
- Removed the unnecessary nested card structure.
- Made the `<a>` element itself the clickable dashboard card.
- Fixed the text overlap/cut-off issue.

### 6. Database Design Concept

- Understood why subjects cannot simply be stored without identifying the student.
- Example:

Rahul
    ↓
Python
DBMS

Aman
    ↓
Java
Computer Networks

- Learned that `user_id` connects a subject with its owner.

## New Concepts Learned

- Subject Management
- Flask GET and POST handling
- HTML form submission
- `method="POST"`
- `action="/subjects"`
- SQLite table relationships
- `user_id`
- Connecting Dashboard cards with Flask routes
- Debugging nested HTML elements
- Clickable cards using `<a>` tags

## Current Project Flow

Dashboard
    ↓
Subjects Card
    ↓
Subject Management Page
    ↓
Add Subject Form
    ↓
Flask `/subjects` Route
    ↓
SQLite Database

## Current Status

- Subject Database Table: ✅ Completed
- Subject Management Page: ✅ Created
- Subject Input Form: ✅ Completed
- `/subjects` Flask Route: ✅ Completed
- Dashboard → Subjects Link: ✅ Working
- Clickable Subjects Card: ✅ Working
- Card Layout Issue: ✅ Fixed
- Save Subject to Database: ⏳ Pending
- User Session: ⏳ Pending
- User-specific Subjects: ⏳ Pending

## Next Task

### Flask Session + User ID

Next we will:

- Learn Flask `session`.
- Store the logged-in user's ID in the session.
- Identify which student is currently logged in.
- Save `user_id` along with `subject_name`.
- Store subjects for individual users.
- Display only the logged-in student's subjects.

## Overall Progress

EduGenie now has a working frontend, Flask backend,
SQLite database, registration system, password hashing,
login authentication, responsive Dashboard and the initial
Subject Management feature.

The next major milestone is:

**Flask Session + User-specific Subject Management 🚀**s