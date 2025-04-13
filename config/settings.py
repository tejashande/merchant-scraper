"""
Configuration settings for the merchant scraper.
"""

import os
from typing import Dict, List

# API Configuration
GOOGLE_PLACES_API_KEY = os.getenv('GOOGLE_PLACES_API_KEY')

# Rate limiting constants
MAX_REQUESTS_PER_DAY = 1000
MAX_REQUESTS_PER_SECOND = 50
MIN_DELAY_BETWEEN_REQUESTS = 1.0 / MAX_REQUESTS_PER_SECOND  # 0.02 seconds
PAGINATION_DELAY = 2  # seconds between pagination requests

# Output configuration
OUTPUT_DIR = 'output'
DEFAULT_RADIUS = 5000  # meters

# Logging configuration
LOG_LEVEL = 'INFO'
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s' 