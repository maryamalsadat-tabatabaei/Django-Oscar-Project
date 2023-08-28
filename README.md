# Customized Django Oscar App with Stripe Integration and Django Oscar API

This repository contains a customized Django Oscar app that has been integrated with Stripe for payment processing, includes additional features such as an "About" page, and incorporates a new app named "Boutique" for extended functionality. The app also utilizes the Django Oscar API to provide RESTful endpoints for resources.
<br/>


<img src="https://github.com/maryamalsadat-tabatabaei/Django-Oscar-Project/assets/87692864/6bbf481f-ec77-46ee-ad23-e64e64012f60" alt="Home Page" width="300px" height="300px">
<img src="https://github.com/maryamalsadat-tabatabaei/Django-Oscar-Project/assets/87692864/bdfc7498-3f9d-4d2a-98b9-2bf8ffd4b28d" alt="Boutique" width="300px" height="300px">
<img src="https://github.com/maryamalsadat-tabatabaei/Django-Oscar-Project/assets/87692864/dea76ca4-b9d3-4129-83ef-fa97729d6b7a" alt="Boutique-details" width="300px" height="300px">
<img src="https://github.com/maryamalsadat-tabatabaei/Django-Oscar-Project/assets/87692864/d01e4f98-8a5b-478d-b3e8-fc21bae6353f" alt="Boutique dashboard" width="300px" height="300px">
<img src="https://github.com/maryamalsadat-tabatabaei/Django-Oscar-Project/assets/87692864/aa2853c9-5014-4783-bd4e-cddcd0e1c9ac" alt="create new boutique" width="300px" height="300px">
<img src="https://github.com/maryamalsadat-tabatabaei/Django-Oscar-Project/assets/87692864/648ae077-37e8-4c96-b251-b6956c09ea62" alt="cart Page" width="300px" height="300px">
<img src="https://github.com/maryamalsadat-tabatabaei/Django-Oscar-Project/assets/87692864/947ead66-a80f-4f07-93d5-5d911c990d76" alt="Checkout Page" width="300px" height="300px">
<img src="https://github.com/maryamalsadat-tabatabaei/Django-Oscar-Project/assets/87692864/f454bffc-90a8-4f65-af80-f91c203fa872" alt="Stripe payment Page" width="300px" height="300px">
<img src="https://github.com/maryamalsadat-tabatabaei/Django-Oscar-Project/assets/87692864/0b0b34e1-14d7-4a22-87e9-7af52eaec0bd" alt="Order Page" width="300px" height="300px">
<img src="https://github.com/maryamalsadat-tabatabaei/Django-Oscar-Project/assets/87692864/44b8f7d7-4512-4e1d-95e7-812747974cca" alt="confirmation Page" width="300px" height="300px">


## Table of Contents

- [Installation](#installation)
- [Features](#features)



## Installation

1. Clone the repository: `git clone https://github.com/maryamalsadat-tabatabaei/Django-Oscar-Project.git`
2. Navigate to the project directory: `cd Django-Oscar-Project`
3. Create a virtual environment and activate it: `virtualenv venv source venv/bin/activate`
4. Configure Stripe API Keys: Update your `Stripe API keys in the appropriate settings file settings.py`
5. Run migrations: `python manage.py migrate`
6. Create a superuser account: `python manage.py createsuperuser`
7. Run the development server: `python manage.py runserver`
8. Access the site: Open your web browser and navigate to http://localhost:8000 to explore your customized Django Oscar app


## Features

The Django Oscar App includes the following features:

- Stripe Integration: The payment functionality has been enhanced by integrating Stripe, allowing smooth and secure payment processing for your e-commerce platform.
- Boutique App: A new app named "Boutique" has been developed and integrated into both the site and the dashboard. This app extends the functionality of your e-commerce platform and allows for CRUD (Create, Read, Update, Delete) operations related to boutique items.
- Template Customization: The app's template has been customized to include a personalized page title and brand, creating a consistent and unique user experience.
- Django Oscar API Integration: The Django Oscar API has been integrated to expose RESTful endpoints for resources. This enables external systems to interact with your e-commerce platform through well-defined API calls.
- Customized Catalogue: An "About" page has been added to the site by forking the catalogue app. This page provides a space for you to share information about your brand, company, or any other relevant content.


