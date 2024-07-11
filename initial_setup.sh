#!/bin/bash

# Ensure the script is run from the root directory of the project
# Exit if the script is run from a different directory
if [ ! -f "manage.py" ]; then
    echo "This script must be run from the root directory of the project."
    exit 1
fi

# Create a virtual environment
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python -m venv venv
else
    echo "Virtual environment already exists."
fi

# Activate the virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "Installing dependencies from requirements.txt..."
pip install -r requirements.txt

# Make and apply migrations
echo "Making migrations..."
python manage.py makemigrations

echo "Applying migrations..."
python manage.py migrate

# Populate the database
echo "Populating the database..."
python manage.py populate_db

# Start the Django development server
echo "Starting the Django development server..."
python manage.py runserver

echo "Setup complete. The Django development server is running."

# Deactivate the virtual environment (optional)
# echo "Deactivating the virtual environment..."
# deactivate
