# FastApiRAM

Overview:

This project is a FastAPI application for monitoring and managing RAM information. It includes endpoints to save RAM usage data, retrieve historical records, and integrates with an SQLite database for storage.

Features:

    Save RAM usage data
    Retrieve historical RAM usage records
    Integrated with SQLite for data storage

Installation:

Prerequisites:

    Python 3.8+
    SQLite (included with Python)
    Virtualenv (recommended)

Setup:
    Clone the repository:
    
bash:
    
    git clone https://github.com/shokooh-rigi/FastApiRAM.git
    cd FastApiRAM

Create and activate a virtual environment:

bash:

    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install the required dependencies:

bash:

    pip install -r requirements.txt

Configuration

    Set up the environment variables (if needed):
    Create a .env file in the root directory and add necessary environment variables.
    Initialize the database:


Running the Application
    Start the FastAPI server:

  bash:
  
    uvicorn main:app --host 127.0.0.1 --port 8080

  Access the API documentation at:
  
        Swagger UI: http://127.0.0.1:8080/ram-swagger/docs
        ReDoc: http://127.0.0.1:8080/ram-swagger/redoc

Running Tests

    Ensure the virtual environment is activated.
    Run the tests using pytest:
    
bash:
  
    pytest

Common Commands

    Create Database Migrations:
    bash:
    
          alembic revision --autogenerate -m "Your migration message"

Apply Database Migrations:

bash:

    alembic upgrade head

Generate Requirements File:

bash:

    pip freeze > requirements.txt

Contributing

If you want to contribute to this project, please follow these steps:

    Fork the repository.
    Create a feature branch (git checkout -b feature-branch).
    Commit your changes (git commit -am 'Add new feature').
    Push to the branch (git push origin feature-branch).
    Create a new Pull Request.
