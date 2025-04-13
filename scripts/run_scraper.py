"""
Script to run the merchant scraper.
"""

import sys
import os
from pathlib import Path

# Add the project root directory to the Python path
project_root = Path(__file__).parent.parent
sys.path.append(str(project_root))

import argparse
from src.merchant_scraper.scraper import MerchantScraper
from config.settings import GOOGLE_PLACES_API_KEY

def main():
    """Main function to run the scraper."""
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Run the merchant scraper')
    parser.add_argument('location', help='Location to search (address or coordinates)')
    parser.add_argument('--radius', type=int, default=5000, help='Search radius in meters')
    args = parser.parse_args()
    
    # Get API key from environment variable
    api_key = os.getenv('GOOGLE_PLACES_API_KEY')
    if not api_key:
        raise ValueError("GOOGLE_PLACES_API_KEY environment variable not set")
    
    # Initialize scraper
    scraper = MerchantScraper(api_key)
    
    # Run scraper
    scraper.run(args.location, args.radius)

if __name__ == '__main__':
    main() 