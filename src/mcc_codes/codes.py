"""
MCC (Merchant Category Codes) mapping functionality.
"""

from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Optional, Tuple


@dataclass
class MCCInfo:
    """Data class for MCC information."""

    code: str
    category: str
    description: str
    examples: List[str]
    notes: str = ""
    mcc_category: Optional["MCCCategory"] = None
    google_place_types: Optional[List[str]] = None


class MCCCategory(Enum):
    """Enum for MCC categories."""

    RETAIL = "Retail"
    FOOD = "Food & Beverage"
    SERVICES = "Services"
    ENTERTAINMENT = "Entertainment"
    TRAVEL = "Travel"
    FINANCIAL = "Financial"
    RELIGIOUS = "Religious"
    ARTS = "Arts & Crafts"


# Mapping of Google Places business types to MCC codes
GOOGLE_TO_MCC_MAPPING = {
    # Retail
    "store": ("5399", MCCCategory.RETAIL),
    "clothing_store": ("5651", MCCCategory.RETAIL),
    "electronics_store": ("5732", MCCCategory.RETAIL),
    "book_store": ("5942", MCCCategory.RETAIL),
    "jewelry_store": ("5944", MCCCategory.RETAIL),
    "shoe_store": ("5661", MCCCategory.RETAIL),
    "bicycle_store": ("5940", MCCCategory.RETAIL),
    "convenience_store": ("5411", MCCCategory.RETAIL),
    "department_store": ("5311", MCCCategory.RETAIL),
    "furniture_store": ("5712", MCCCategory.RETAIL),
    "hardware_store": ("5251", MCCCategory.RETAIL),
    "home_goods_store": ("5719", MCCCategory.RETAIL),
    "liquor_store": ("5921", MCCCategory.RETAIL),
    "pet_store": ("5995", MCCCategory.RETAIL),
    "shopping_mall": ("5300", MCCCategory.RETAIL),
    "supermarket": ("5411", MCCCategory.RETAIL),
    "florist": ("5992", MCCCategory.RETAIL),
    "gift_shop": ("5947", MCCCategory.RETAIL),
    "toy_store": ("5945", MCCCategory.RETAIL),
    "sporting_goods_store": ("5941", MCCCategory.RETAIL),
    "cosmetics_store": ("5977", MCCCategory.RETAIL),
    "perfumery": ("5977", MCCCategory.RETAIL),
    "stationery_store": ("5943", MCCCategory.RETAIL),
    "computer_store": ("5734", MCCCategory.RETAIL),
    "mobile_phone_shop": ("4812", MCCCategory.RETAIL),
    "camera_store": ("5946", MCCCategory.RETAIL),
    "music_store": ("5733", MCCCategory.RETAIL),
    "video_store": ("7841", MCCCategory.RETAIL),
    "boutique": ("5651", MCCCategory.RETAIL),
    # Food & Beverage
    "restaurant": ("5812", MCCCategory.FOOD),
    "cafe": ("5814", MCCCategory.FOOD),
    "bakery": ("5462", MCCCategory.FOOD),
    "bar": ("5813", MCCCategory.FOOD),
    "meal_delivery": ("5812", MCCCategory.FOOD),
    "meal_takeaway": ("5812", MCCCategory.FOOD),
    "food": ("5499", MCCCategory.FOOD),
    "grocery_or_supermarket": ("5411", MCCCategory.FOOD),
    "ice_cream_shop": ("5451", MCCCategory.FOOD),
    "coffee_shop": ("5814", MCCCategory.FOOD),
    "dessert_shop": ("5462", MCCCategory.FOOD),
    "food_court": ("5812", MCCCategory.FOOD),
    "fast_food_restaurant": ("5814", MCCCategory.FOOD),
    "pizza_restaurant": ("5812", MCCCategory.FOOD),
    "sushi_restaurant": ("5812", MCCCategory.FOOD),
    "steak_house": ("5812", MCCCategory.FOOD),
    "seafood_restaurant": ("5812", MCCCategory.FOOD),
    "vegetarian_restaurant": ("5812", MCCCategory.FOOD),
    "vegan_restaurant": ("5812", MCCCategory.FOOD),
    "buffet_restaurant": ("5812", MCCCategory.FOOD),
    # Services
    "hair_care": ("7230", MCCCategory.SERVICES),
    "beauty_salon": ("7230", MCCCategory.SERVICES),
    "spa": ("7298", MCCCategory.SERVICES),
    "laundry": ("7211", MCCCategory.SERVICES),
    "dry_cleaning": ("7216", MCCCategory.SERVICES),
    "car_wash": ("7542", MCCCategory.SERVICES),
    "car_repair": ("7538", MCCCategory.SERVICES),
    "pharmacy": ("5912", MCCCategory.SERVICES),
    "dentist": ("8021", MCCCategory.SERVICES),
    "doctor": ("8011", MCCCategory.SERVICES),
    "hospital": ("8062", MCCCategory.SERVICES),
    "veterinary_care": ("0742", MCCCategory.SERVICES),
    "optician": ("8043", MCCCategory.SERVICES),
    "hearing_aid_store": ("5975", MCCCategory.SERVICES),
    "medical_supply_store": ("5047", MCCCategory.SERVICES),
    "massage_therapist": ("7297", MCCCategory.SERVICES),
    "nail_salon": ("7230", MCCCategory.SERVICES),
    "tanning_salon": ("7297", MCCCategory.SERVICES),
    "tattoo_parlor": ("7297", MCCCategory.SERVICES),
    "barber_shop": ("7230", MCCCategory.SERVICES),
    "tailor": ("5697", MCCCategory.SERVICES),
    "shoe_repair": ("7251", MCCCategory.SERVICES),
    "key_shop": ("7699", MCCCategory.SERVICES),
    "locksmith": ("7699", MCCCategory.SERVICES),
    "moving_company": ("4214", MCCCategory.SERVICES),
    "storage": ("4215", MCCCategory.SERVICES),
    "plumber": ("1711", MCCCategory.SERVICES),
    "electrician": ("1731", MCCCategory.SERVICES),
    # Entertainment
    "movie_theater": ("7832", MCCCategory.ENTERTAINMENT),
    "amusement_park": ("7996", MCCCategory.ENTERTAINMENT),
    "aquarium": ("7991", MCCCategory.ENTERTAINMENT),
    "art_gallery": ("5971", MCCCategory.ENTERTAINMENT),
    "bowling_alley": ("7933", MCCCategory.ENTERTAINMENT),
    "casino": ("7993", MCCCategory.ENTERTAINMENT),
    "museum": ("7991", MCCCategory.ENTERTAINMENT),
    "night_club": ("5813", MCCCategory.ENTERTAINMENT),
    "park": ("7991", MCCCategory.ENTERTAINMENT),
    "stadium": ("7941", MCCCategory.ENTERTAINMENT),
    "zoo": ("7991", MCCCategory.ENTERTAINMENT),
    "theater": ("7922", MCCCategory.ENTERTAINMENT),
    "concert_hall": ("7922", MCCCategory.ENTERTAINMENT),
    "comedy_club": ("7922", MCCCategory.ENTERTAINMENT),
    "dance_studio": ("7911", MCCCategory.ENTERTAINMENT),
    "gym": ("7997", MCCCategory.ENTERTAINMENT),
    "fitness_center": ("7997", MCCCategory.ENTERTAINMENT),
    "yoga_studio": ("7997", MCCCategory.ENTERTAINMENT),
    "sports_club": ("7997", MCCCategory.ENTERTAINMENT),
    "golf_course": ("7992", MCCCategory.ENTERTAINMENT),
    "tennis_court": ("7992", MCCCategory.ENTERTAINMENT),
    "swimming_pool": ("7997", MCCCategory.ENTERTAINMENT),
    "arcade": ("7993", MCCCategory.ENTERTAINMENT),
    "billiards_hall": ("7933", MCCCategory.ENTERTAINMENT),
    "pool_hall": ("7933", MCCCategory.ENTERTAINMENT),
    "karaoke_bar": ("5813", MCCCategory.ENTERTAINMENT),
    # Travel
    "lodging": ("7011", MCCCategory.TRAVEL),
    "travel_agency": ("4722", MCCCategory.TRAVEL),
    "tourist_attraction": ("7991", MCCCategory.TRAVEL),
    "hostel": ("7011", MCCCategory.TRAVEL),
    "bed_and_breakfast": ("7011", MCCCategory.TRAVEL),
    "resort": ("7011", MCCCategory.TRAVEL),
    "motel": ("7011", MCCCategory.TRAVEL),
    "car_rental": ("7512", MCCCategory.TRAVEL),
    "bicycle_rental": ("7512", MCCCategory.TRAVEL),
    "boat_rental": ("7512", MCCCategory.TRAVEL),
    "tour_operator": ("4722", MCCCategory.TRAVEL),
    "tourist_information_center": ("4722", MCCCategory.TRAVEL),
    "airport": ("4582", MCCCategory.TRAVEL),
    "train_station": ("4111", MCCCategory.TRAVEL),
    "bus_station": ("4112", MCCCategory.TRAVEL),
    "ferry_terminal": ("4113", MCCCategory.TRAVEL),
    "parking": ("7523", MCCCategory.TRAVEL),
    "gas_station": ("5541", MCCCategory.TRAVEL),
    "car_dealer": ("5511", MCCCategory.TRAVEL),
    "motorcycle_dealer": ("5571", MCCCategory.TRAVEL),
    # Financial
    "bank": ("6012", MCCCategory.FINANCIAL),
    "atm": ("6011", MCCCategory.FINANCIAL),
    "insurance_agency": ("6300", MCCCategory.FINANCIAL),
    "accounting": ("8931", MCCCategory.FINANCIAL),
    "tax_preparation": ("8931", MCCCategory.FINANCIAL),
    "financial_advisor": ("6211", MCCCategory.FINANCIAL),
    "mortgage_broker": ("6211", MCCCategory.FINANCIAL),
    "credit_union": ("6012", MCCCategory.FINANCIAL),
    "currency_exchange": ("6051", MCCCategory.FINANCIAL),
    "pawn_shop": ("5933", MCCCategory.FINANCIAL),
    "check_cashing_service": ("6051", MCCCategory.FINANCIAL),
    "payday_loan_service": ("6012", MCCCategory.FINANCIAL),
    # Religious
    "church": ("8661", MCCCategory.RELIGIOUS),
    "mosque": ("8661", MCCCategory.RELIGIOUS),
    "synagogue": ("8661", MCCCategory.RELIGIOUS),
    "temple": ("8661", MCCCategory.RELIGIOUS),
    "religious_organization": ("8661", MCCCategory.RELIGIOUS),
    "religious_school": ("8211", MCCCategory.RELIGIOUS),
    "religious_bookstore": ("5942", MCCCategory.RELIGIOUS),
    "religious_goods_store": ("5973", MCCCategory.RELIGIOUS),
    # Arts & Crafts
    "art_school": ("8299", MCCCategory.ARTS),
    "art_supply_store": ("5971", MCCCategory.ARTS),
    "craft_store": ("5971", MCCCategory.ARTS),
    "fabric_store": ("5949", MCCCategory.ARTS),
    "pottery_store": ("5971", MCCCategory.ARTS),
    "photography_studio": ("7221", MCCCategory.ARTS),
    "musical_instrument_store": ("5733", MCCCategory.ARTS),
}


def get_mcc_from_google_place_type(place_type: str) -> Tuple[str, str]:
    """
    Get MCC code and category for a Google Places business type.

    Args:
        place_type: Google Places business type

    Returns:
        Tuple of (MCC code, category)
    """
    if place_type not in GOOGLE_TO_MCC_MAPPING:
        raise ValueError(f"Unknown business type: {place_type}")

    mcc_code, category = GOOGLE_TO_MCC_MAPPING[place_type]
    return mcc_code, category.value


def get_mcc_info(business_type: str) -> MCCInfo:
    """
    Get MCC information for a business type.

    Args:
        business_type: Business type

    Returns:
        MCCInfo object containing MCC code and category information
    """
    if business_type not in GOOGLE_TO_MCC_MAPPING:
        raise ValueError(f"Unknown business type: {business_type}")

    mcc_code, category = GOOGLE_TO_MCC_MAPPING[business_type]
    return MCCInfo(
        code=mcc_code,
        category=category.value,
        description=f"{business_type} business",
        examples=[business_type],
        mcc_category=category,
        google_place_types=[business_type],
    )


def get_all_codes() -> Dict[str, Tuple[str, str]]:
    """
    Get all MCC codes and their categories.

    Returns:
        Dictionary mapping business types to (MCC code, category) tuples
    """
    return {k: (v[0], v[1].value) for k, v in GOOGLE_TO_MCC_MAPPING.items()}


def validate_mcc_code(code: str) -> bool:
    """
    Validate an MCC code.

    Args:
        code: MCC code to validate

    Returns:
        True if valid, False otherwise
    """
    return code in {v[0] for v in GOOGLE_TO_MCC_MAPPING.values()}


def get_codes_by_category(category: MCCCategory) -> Dict[str, MCCInfo]:
    """
    Get all MCC codes for a specific category.

    Args:
        category: MCC category to filter by

    Returns:
        Dictionary mapping business types to MCCInfo objects
    """
    return {
        business_type: MCCInfo(
            code=code,
            category=cat.value,
            description=f"{business_type} business",
            examples=[business_type],
            mcc_category=cat,
            google_place_types=[business_type],
        )
        for business_type, (code, cat) in GOOGLE_TO_MCC_MAPPING.items()
        if cat == category
    }
