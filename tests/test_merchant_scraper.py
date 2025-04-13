import os
from unittest.mock import patch

import pytest

from src.merchant_scraper.scraper import Merchant, MerchantScraper


@pytest.fixture
def mock_gmaps():
    """Create a mock Google Maps client."""
    with patch("src.merchant_scraper.scraper.googlemaps.Client") as mock:
        yield mock


@pytest.fixture
def scraper(mock_gmaps):
    """Create a MerchantScraper instance with mocked dependencies."""
    api_key = "test_api_key"
    output_dir = "test_output"
    os.makedirs(output_dir, exist_ok=True)
    scraper = MerchantScraper(api_key, output_dir)
    return scraper


@pytest.fixture
def sample_place_data():
    """Sample place data from Google Places API."""
    return {
        "name": "Test Restaurant",
        "vicinity": "123 Test St",
        "geometry": {"location": {"lat": 40.7128, "lng": -74.0060}},
        "types": ["restaurant", "food", "point_of_interest"],
        "place_id": "test_place_id",
        "rating": 4.5,
        "user_ratings_total": 100,
        "price_level": 2,
        "opening_hours": {"open_now": True},
    }


@pytest.fixture
def sample_merchant():
    """Create a sample Merchant instance."""
    return Merchant(
        name="Test Restaurant",
        address="123 Test St",
        latitude=40.7128,
        longitude=-74.0060,
        business_types=["restaurant", "food", "point_of_interest"],
        mcc_code="5812",
        mcc_category="Food & Beverage",
        place_id="test_place_id",
        rating=4.5,
        user_ratings_total=100,
        price_level=2,
        is_open=True,
        phone="+1234567890",
        website="http://test.com",
    )


def test_merchant_scraper_initialization(scraper):
    """Test MerchantScraper initialization."""
    assert scraper.output_dir == "test_output"
    assert isinstance(scraper.seen_place_ids, set)
    assert scraper.request_count == 0
    assert scraper.last_request_time == 0


def test_rate_limiting(scraper):
    """Test rate limiting functionality."""
    # First request should pass
    scraper._rate_limit()
    assert scraper.request_count == 1

    # Simulate exceeding daily limit
    scraper.request_count = 1000
    with pytest.raises(Exception, match="Daily API quota exceeded"):
        scraper._rate_limit()


def test_is_b2c_business(scraper):
    """Test B2C business type detection."""
    # Test with B2C business types
    assert scraper._is_b2c_business(["restaurant", "food"])
    assert scraper._is_b2c_business(["store", "clothing_store"])
    assert scraper._is_b2c_business(["beauty_salon", "spa"])
    assert scraper._is_b2c_business(["grocery_or_supermarket"])
    assert scraper._is_b2c_business(["pharmacy"])
    assert scraper._is_b2c_business(["movie_theater"])
    assert scraper._is_b2c_business(["gym"])

    # Test with non-B2C business types
    assert not scraper._is_b2c_business(["real_estate_agency"])
    assert not scraper._is_b2c_business(["unknown_type"])


def test_map_business_type_to_mcc(scraper):
    """Test MCC code mapping."""
    # Test with known business types
    code, category = scraper._map_business_type_to_mcc(["restaurant"])
    assert code == "5812"
    assert category == "Food & Beverage"

    code, category = scraper._map_business_type_to_mcc(["grocery_or_supermarket"])
    assert code == "5411"
    assert category == "Food & Beverage"

    # Test with unknown business types
    code, category = scraper._map_business_type_to_mcc(["unknown_type"])
    assert code == "5399"
    assert category == "Miscellaneous General Merchandise"


def test_process_place_data(scraper, sample_place_data):
    """Test place data processing."""
    # Mock the place details API call
    with patch.object(scraper, "_make_api_request") as mock_api:
        mock_api.return_value = {
            "result": {
                "formatted_phone_number": "+1234567890",
                "website": "http://test.com",
            }
        }

        merchant = scraper._process_place_data(sample_place_data)

        assert isinstance(merchant, Merchant)
        assert merchant.name == "Test Restaurant"
        assert merchant.address == "123 Test St"
        assert merchant.business_types == ["restaurant", "food", "point_of_interest"]
        assert merchant.place_id == "test_place_id"


def test_save_to_excel(scraper, sample_merchant, tmp_path):
    """Test Excel file creation."""
    # Set output directory to temporary path
    scraper.output_dir = str(tmp_path)

    # Test saving merchants to Excel
    filename = "test_merchants"
    scraper._save_to_excel([sample_merchant], filename)

    # Verify file was created
    expected_file = tmp_path / f"{filename}.xlsx"
    assert expected_file.exists()

    # Clean up
    os.remove(expected_file)


def test_fetch_merchants(scraper, mock_gmaps):
    """Test merchant fetching functionality."""
    # Mock geocoding response
    mock_gmaps.return_value.geocode.return_value = [
        {"geometry": {"location": {"lat": 40.7128, "lng": -74.0060}}}
    ]

    # Mock places nearby response
    mock_gmaps.return_value.places_nearby.return_value = {
        "results": [
            {
                "name": "Test Restaurant",
                "vicinity": "123 Test St",
                "geometry": {"location": {"lat": 40.7128, "lng": -74.0060}},
                "types": ["restaurant"],
                "place_id": "test_place_id",
                "rating": 4.5,
                "user_ratings_total": 100,
                "price_level": 2,
                "opening_hours": {"open_now": True},
            }
        ]
    }

    # Mock place details response
    mock_gmaps.return_value.place.return_value = {
        "result": {
            "formatted_phone_number": "+1234567890",
            "website": "http://test.com",
        }
    }

    # Test fetching merchants
    merchants = scraper.fetch_merchants("New York, NY")
    assert len(merchants) > 0
    assert isinstance(merchants[0], Merchant)


def test_run_method(scraper, mock_gmaps, tmp_path):
    """Test the main run method."""
    # Set output directory to temporary path
    scraper.output_dir = str(tmp_path)

    # Create a sample merchant
    sample_merchant = Merchant(
        name="Test Restaurant",
        address="123 Test St",
        latitude=40.7128,
        longitude=-74.0060,
        business_types=["restaurant"],
        mcc_code="5812",
        mcc_category="Food & Beverage",
        place_id="test_place_id",
        rating=4.5,
        user_ratings_total=100,
        price_level=2,
        is_open=True,
    )

    # Mock the fetch_merchants method
    with patch.object(scraper, "fetch_merchants") as mock_fetch:
        mock_fetch.return_value = [sample_merchant]

        # Run the scraper
        scraper.run("New York, NY")

        # Verify fetch_merchants was called
        mock_fetch.assert_called_once_with("New York, NY", 5000)

        # Verify Excel file was created
        files = list(tmp_path.glob("merchants_*.xlsx"))
        assert len(files) == 1

        # Clean up
        for file in files:
            os.remove(file)
