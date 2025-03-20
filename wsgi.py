# Code to configure the WSGI file on the server

import sys
import os

# Add your project directory to sys.path
project_home = "/home/morel/content-creator"
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Set the Flask app path
from upload import app as application
