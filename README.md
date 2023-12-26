# Django Notifications POC

This Django project implements a simple notification system that allows sending notifications to users via email. It includes a basic user interface to view notifications.

## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Setup](#setup)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Overview

The project consists of a Django application named `notificaciones`, which handles the creation and sending of notifications. Users are represented by the `Usuario` model, and notifications are stored in the `Notificacion` model.

## Project Structure

The project has the following structure:


- `your_project`: Main project directory.
- `notificaciones`: Django application handling notifications.
- `notificaciones/models.py`: Models for notifications and users.
- `notificaciones/views.py`: Views including the notification-sending logic.
- `notificaciones/urls.py`: URL configurations for the application.
- `notificaciones/templates/`: HTML templates for the application.

## Setup

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your_username/Django-notifications_POC.git
    cd Django-notifications_POC
    ```

2. **Create a virtual environment:**

    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment:**

    ```bash
    source venv/bin/activate  # On Windows: .\venv\Scripts\activate
    ```

4. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

5. **Run migrations:**

    ```bash
    python manage.py migrate
    ```

## Usage

1. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

2. **Visit `http://127.0.0.1:8000/notificaciones/ver_notificaciones/` in your browser to view notifications.**

3. **Send a notification:**

    Visit `http://127.0.0.1:8000/notificaciones/enviar_notificacion/1/1/` to simulate sending a notification to the user with ID 1.

## Contributing

Feel free to contribute by opening issues or submitting pull requests. Please follow the project's coding standards.

## License

This project is licensed under the [MIT License](LICENSE).
