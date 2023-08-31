# Customized Django Oscar App with Stripe Integration and Django Oscar API

This repository contains a customized Django Oscar app that has been integrated with Stripe for payment processing, includes additional features such as an "About" page, and incorporates a new app named "Boutique" for extended functionality. The app also utilizes the Django Oscar API to provide RESTful endpoints for resources.
<br/>




<img src="https://github.com/maryamalsadat-tabatabaei/Django-Oscar-Project/assets/87692864/d6515aab-3baf-4a40-9a7d-57277b8a5cba" alt="Home Page" width="30%" height="250px">
<img src="https://github.com/maryamalsadat-tabatabaei/Django-Oscar-Project/assets/87692864/99d5e276-8ebb-4d61-a7c8-9ff7b298acf2" alt="cart Page" width="30%" height="250px">
<img src="https://github.com/maryamalsadat-tabatabaei/Django-Oscar-Project/assets/87692864/527ce821-6bc4-4758-8172-b330e9b544b2" alt="Checkout Page" width="30%" height="250px">
<img src="https://github.com/maryamalsadat-tabatabaei/Django-Oscar-Project/assets/87692864/cebaf521-6fc2-4ac0-a3b4-de3419e4f26c" alt="Order Page" width="30%" height="250px">
<img src="https://github.com/maryamalsadat-tabatabaei/Django-Oscar-Project/assets/87692864/ed382ea1-2495-4de5-bce7-a4b4c3a06abc" alt="confirmation Page" width="30%" height="250px">
<img src="https://github.com/maryamalsadat-tabatabaei/Django-Oscar-Project/assets/87692864/5724c854-5935-495b-a16b-582f5491e3d8" alt="Boutique" width="30%" height="150px">
<img src="https://github.com/maryamalsadat-tabatabaei/Django-Oscar-Project/assets/87692864/15acd843-f2eb-4c00-91b3-8e8795a89ef1" alt="Boutique-details" width="30%" height="150px">
<img src="https://github.com/maryamalsadat-tabatabaei/Django-Oscar-Project/assets/87692864/732225c2-0ce6-434d-8198-43d05a9c8558" alt="Boutique dashboard" width="30%" height="150px">
<img src="https://github.com/maryamalsadat-tabatabaei/Django-Oscar-Project/assets/87692864/f98817cd-9930-4c15-b56f-a4ba4459789f" alt="create new boutique" width="30%" height="150px">

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


