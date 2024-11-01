# Shortest-Path-Problems

Mini Project for Data Engineering

## Tasks

https://docs.google.com/spreadsheets/d/14TMLGl_cz5-rTlw0RBJLjxHiyW_X4OVjMlzZTzEPLGE/edit?gid=0#gid=0

## API

- Create a virtual environment using `virtualenv` module in python.

```bash
# Install module (globally)
pip install virtualenv
sudo apt install python3-virtualenv

# Generate virtual environment
virtualenv --python=<your-python-runtime-version> venv

# Activate virtual environment
source venv/bin/activate

# Install depdendency packages
pip install -r requirements.txt
```

- Run `uvicorn` web server from `backend` directory (`reload` mode is for development purposes)

```bash
uvicorn main:app --reload
```

- Go to `http://localhost:8000/docs` to see the documentation of the API
