# Flask Boilerplate

## Overview
This is a minimal yet powerful Flask boilerplate to kickstart your web applications. It provides a basic structure for developing and deploying Flask applications seamlessly.

## Features
- Simple and clean folder structure
- Pre-configured Flask setup
- Basic routing and templates
- Lightweight and easy to customize

## Installation

### Prerequisites
Ensure you have the following installed:
- Python 3.x
- pip (Python package manager)

### Steps to Run the Project
1. **Clone the Repository**
   ```bash
   git clone https://github.com/YuheshPandian/flask-boilerplate.git
   cd flask-boilerplate
   ```

2. **Create a Virtual Environment (Optional but Recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask App**
   ```bash
   python app.py
   ```
   The application should now be running on `http://127.0.0.1:5000/`

## Project Structure
```
flask-boilerplate/
  app/
    │-- static/        # Static files (CSS, JS, images)
    │-- templates/     # HTML templates
    │-- config.py      # Main Flask application configuration
    |-- views.py       # Contains all routes of the site
    |-- __init__.py    # Basic registrations and setup
    │-- requirements.txt # List of dependencies
    │-- README.md      # Project documentation
  run.py               # helps to run the site from the terminal easily
  errorlog.txt         # registers the errors that occur when debug is set to false

```

## Contributing
Feel free to fork the repository and submit pull requests. Contributions are always welcome!

## License
This project is licensed under the MIT License.

---
Developed by [YuheshPandian](https://github.com/YuheshPandian) 🚀

