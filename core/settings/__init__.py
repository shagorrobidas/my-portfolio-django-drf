import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Determine environment based on DEBUG variable
# Default to True (dev) if not specified in .env
debug_val = os.environ.get('DEBUG', 'True').lower()

if debug_val in ('true', '1', 'yes', 'on'):
    from .dev import *
else:
    from .prod import *
