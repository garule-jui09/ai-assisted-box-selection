# AI-Assisted Box Selection System

## 1. Project Overview

The AI-Assisted Box Selection System is a Django web application that recommends a suitable shipping box for a product.

The system checks the product's length, width, height, and weight against the available shipping boxes. It selects the lowest-cost box that satisfies the dimension and weight requirements.

**Note:** The current implementation uses rule-based recommendation logic. It does not use a trained machine learning model.

## 2. Objectives

- Store product dimensions and weight.
- Store shipping box dimensions, maximum weight capacity, and cost.
- Recommend a suitable box for a selected product.
- Choose the lowest-cost suitable box.
- Display a message when no suitable box is available.
- Manage products and boxes through Django Admin.

## 3. Technologies Used

- Python
- Django
- SQLite
- HTML
- Django Template Language

## 4. Features

- Product management through Django Admin.
- Shipping box management through Django Admin.
- Product selection from a dropdown list.
- Dimension and weight validation.
- Lowest-cost suitable box recommendation.
- Handles products that do not fit any available box.

## 5. Project Structure

```text
box_Selection/
├── manage.py
├── project/
│   ├── settings.py
│   └── urls.py
├── box_selector/
│   ├── migrations/
│   ├── templates/
│   │   └── box_selector/
│   │       └── home.html
│   ├── admin.py
│   ├── models.py
│   ├── recommendation.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── README.md
├── requirements.txt
├── AI_USAGE.md
└── TEST_OUTPUT.md
```

## 6. Setup and Installation

### Prerequisites

- Python installed
- pip installed
- Visual Studio Code or another code editor

### Step 1: Open the project directory

Open the terminal in the project folder.

### Step 2: Create a virtual environment

```bash
python -m venv venv
```

### Step 3: Activate the virtual environment

For Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### Step 4: Install dependencies

```bash
python -m pip install -r requirements.txt
```

### Step 5: Apply database migrations

```bash
python manage.py migrate
```

### Step 6: Create an admin account

```bash
python manage.py createsuperuser
```

Follow the terminal prompts to create the account.

### Step 7: Start the development server

```bash
python manage.py runserver
```

Open the application:

http://127.0.0.1:8000/

Open Django Admin:

http://127.0.0.1:8000/admin/

## 7. How to Use the Application

1. Start the Django development server.
2. Open Django Admin.
3. Add products with their dimensions and weight.
4. Add shipping boxes with their dimensions, maximum weight capacity, and cost.
5. Open the main application page.
6. Select a product from the dropdown.
7. Click the Recommend Box button.
8. Review the recommended box or the message indicating that no suitable box is available.

## 8. Recommendation Logic

The application sorts the three product dimensions and the three box dimensions before comparing them. This allows the product to fit in a different orientation.

A box is considered suitable when:

- All three product dimensions fit within the corresponding box dimensions.
- The product weight does not exceed the box's maximum weight capacity.

Among suitable boxes, the application selects the box with the lowest cost.

If no box satisfies both conditions, the application returns no recommendation.

## 9. Running Tests

Run the automated tests using:

```bash
python manage.py test box_selector
```

The tests cover dimension fitting, weight capacity, lowest-cost selection, rotation, exact limits, and the no-suitable-box case.

Record the actual test results in `TEST_OUTPUT.md`.

## 10. AI Usage and Learning

AI tool usage, prompts, accepted or rejected suggestions, errors encountered, and verification steps are documented in `AI_USAGE.md`.

The learning reflection should describe my own understanding and experience while building and testing this project.

## 11. Future Improvements

- Add support for multiple products in a single order.
- Add more advanced packing logic for products with complex shapes.
- Improve the user interface.
- Add further validation and test cases.

## 12. Project Status

This project is intended as a Django hiring assignment. Features and test results should be verified before submission.


## Project Development Transcript

The project conversation transcript is available here:

[View ChatGPT Project Transcript](transcript/django_project_chat_transcript.pdf)    