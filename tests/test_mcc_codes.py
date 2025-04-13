"""
Tests for MCC codes module.
"""
import pytest

from src.mcc_codes import (
    MCCCategory,
    MCCInfo,
    get_all_codes,
    get_codes_by_category,
    get_mcc_from_google_place_type,
    get_mcc_info,
    validate_mcc_code,
)


def test_mcc_info_dataclass():
    """Test MCCInfo dataclass initialization."""
    info = MCCInfo(
        code="5411",
        category="Retail",
        description="Test description",
        examples=["Example 1", "Example 2"],
        notes="Test notes",
    )

    assert info.code == "5411"
    assert info.category == "Retail"
    assert info.description == "Test description"
    assert info.examples == ["Example 1", "Example 2"]
    assert info.notes == "Test notes"


def test_get_mcc_from_google_place_type():
    """Test getting MCC code from Google Place type."""
    # Test known place types
    code, category = get_mcc_from_google_place_type("restaurant")
    assert code == "5812"
    assert category == "Food & Beverage"

    code, category = get_mcc_from_google_place_type("store")
    assert code == "5399"
    assert category == "Retail"

    # Test unknown place type
    try:
        get_mcc_from_google_place_type("invalid_type")
        assert False, "Should have raised ValueError"
    except ValueError:
        pass


def test_get_mcc_info():
    """Test getting MCC information for a business type."""
    # Test valid business type
    info = get_mcc_info("restaurant")
    assert isinstance(info, MCCInfo)
    assert info.code is not None
    assert info.category is not None
    assert info.description is not None
    assert info.examples is not None
    assert info.mcc_category == MCCCategory.FOOD

    # Test invalid business type
    with pytest.raises(ValueError):
        get_mcc_info("invalid_type")


def test_validate_mcc_code():
    """Test MCC code validation."""
    # Test valid MCC code
    assert validate_mcc_code("5812")  # Restaurant code
    assert validate_mcc_code("5411")  # Grocery code

    # Test invalid MCC code
    assert not validate_mcc_code("0000")
    assert not validate_mcc_code("9999")


def test_get_all_codes():
    """Test getting all MCC codes."""
    codes = get_all_codes()
    assert isinstance(codes, dict)
    assert len(codes) > 0

    # Test structure of returned data
    for business_type, (code, category) in codes.items():
        assert isinstance(business_type, str)
        assert isinstance(code, str)
        assert isinstance(category, str)
        assert len(code) == 4  # MCC codes are 4 digits


def test_get_codes_by_category():
    """Test getting codes by category."""
    # Test valid category
    retail_codes = get_codes_by_category(MCCCategory.RETAIL)
    assert isinstance(retail_codes, dict)
    assert len(retail_codes) > 0

    # Verify all returned codes are in the specified category
    for mcc_info in retail_codes.values():
        assert mcc_info.mcc_category == MCCCategory.RETAIL


def test_mcc_categories():
    """Test MCC category structure."""
    # Test that all categories are unique
    categories = set(category.value for category in MCCCategory)
    assert len(categories) == len(MCCCategory)

    # Test that all categories are strings
    for category in MCCCategory:
        assert isinstance(category.value, str)


def test_mcc_info_structure():
    """Test MCCInfo data structure."""
    # Test that all required fields are present
    info = get_mcc_info("restaurant")
    assert hasattr(info, "code")
    assert hasattr(info, "category")
    assert hasattr(info, "description")
    assert hasattr(info, "examples")
    assert hasattr(info, "notes")
    assert hasattr(info, "mcc_category")
    assert hasattr(info, "google_place_types")

    # Test that optional fields have default values
    assert info.notes == "" or isinstance(info.notes, str)
    assert info.google_place_types is None or isinstance(info.google_place_types, list)
