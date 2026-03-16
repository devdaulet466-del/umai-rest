import sys
import os

# Adjust this path based on where Plesk creates the virtual environment. 
# Typically, if your app root is /httpdocs/backend, the venv is created there.
# You might need to change this if your Plesk setup uses a different venv path.

INTERP = os.path.expanduser("~/httpdocs/backend/venv/bin/python")
if os.path.exists(INTERP) and sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)

# Add the current directory to the path so main.py can be found
sys.path.append(os.getcwd())

# Import the FastAPI app as 'application' for Passenger WSGI
from main import app as application
