# AI Usage Documentation

## 1. AI Tools Used

- **Tool:** ChatGPT
- **Purpose:** I used ChatGPT to understand Django concepts, plan the project structure, troubleshoot errors, improve the user interface, and understand how to test the box recommendation logic.

## 2. Prompts Used

The following are examples of the types of prompts I used during development. They are not a complete verbatim transcript of every prompt.

- How do I create a Django project and app?
- How can I recommend a shipping box based on product dimensions, weight capacity, and box cost?
- How do I fix Django URL and view errors?
- How can I write automated tests for the recommendation logic?
- How can I improve the CSS and layout of the Django application?
- How should I prepare the README and test documentation?

## 3. AI Suggestions Accepted

I used AI assistance to help with the following parts of the project:

- Organizing the Django project and application.
- Creating the `Product` and `ShippingBox` models.
- Comparing product and box dimensions.
- Checking whether a product's weight is within a box's maximum weight capacity.
- Selecting the lowest-cost suitable box.
- Creating automated test cases.
- Improving the HTML template and CSS styling.
- Preparing project documentation.

I reviewed the suggested code and ran the application and tests to check the implementation.

## 4. AI Suggestions Rejected or Modified

During development, I made changes while integrating and testing the suggested code.

I first used a simple `HttpResponse` view to check whether the homepage URL was working after encountering a view-related error. The intended view was then restored to render the Django template and perform the box recommendation.

I also ran the project checks and automated tests after making changes.

I will document any additional suggestions I reject or modify based on what I actually do during development.

## 5. Errors and Debugging

During development, I encountered an error indicating that `box_selector.views` had no attribute named `home`.

To investigate the problem, I checked the Django view and URL configuration. I temporarily used a simple `HttpResponse` view to verify that the URL could respond. After confirming that the URL worked, I restored the intended view logic.

I also checked the project configuration and tested the website in the browser.

## 6. Verification

The following checks were performed:

- Ran `python manage.py check`.
- Started the application using `python manage.py runserver`.
- Opened the homepage in the browser.
- Confirmed that the CSS file loaded successfully.
- Submitted product selections through the homepage.
- Ran `python manage.py test box_selector`.

The latest recorded test run reported six tests passing with no failures or errors.

## 7. Limitations

The current recommendation system uses rule-based logic. It checks product dimensions, box dimensions, maximum weight capacity, and box cost.

It selects the lowest-cost box that satisfies the implemented conditions. The current implementation does not use a trained machine learning model or an AI model to make the recommendation.

## 8. Human Review and Responsibility

I reviewed the application by running it and executing the automated tests. I am responsible for understanding the project code and verifying the final implementation before submission.

ChatGPT was used as an assistance tool during development. The actual conversation transcript will be provided separately as required by the assignment.
