# Merchant Scraper

A Python application that scrapes merchant data from Google Places API and saves it to an Excel file. It uses MCC (Merchant Category Codes) to categorize businesses.

## Project Structure

```
nexus/
├── src/
│   ├── merchant_scraper/
│   │   ├── __init__.py
│   │   ├── scraper.py
│   │   ├── models.py
│   │   ├── utils.py
│   │   └── constants.py
│   └── mcc_codes/
│       ├── __init__.py
│       ├── codes.py
│       └── categories.py
├── tests/
│   ├── __init__.py
│   ├── test_merchant_scraper.py
│   └── test_mcc_codes.py
├── output/
├── requirements/
│   ├── dev.txt
│   └── main.txt
├── scripts/
│   └── run_scraper.py
├── config/
│   └── settings.py
├── Dockerfile
├── docker-compose.yml
├── Makefile
└── README.md
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/tejashande/merchant-scraper.git
cd merchant-scraper
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements/dev.txt  # For development
# or
pip install -r requirements/main.txt  # For production
```

4. Set up environment variables:
```bash
export GOOGLE_PLACES_API_KEY=your_api_key  # On Windows: set GOOGLE_PLACES_API_KEY=your_api_key
```

## Usage

Run the scraper with:
```bash
python scripts/run_scraper.py "Haarlem, Netherlands" --radius 5000
```

Arguments:
- `location`: Location to search (address or coordinates)
- `--radius`: Search radius in meters (default: 5000)

## Development

### Running Tests
```bash
pytest
```

### Code Formatting
```bash
black .
isort .
```

### Type Checking
```bash
mypy .
```

### Linting
```bash
flake8
```

## License

MIT 