"""
Data models for the merchant scraper.
"""

from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Merchant:
    """Data class to store merchant information."""

    name: str
    address: str
    latitude: float
    longitude: float
    business_types: List[str]
    mcc_code: str
    mcc_category: str
    place_id: str
    rating: float
    user_ratings_total: int
    price_level: int
    is_open: bool
    phone: Optional[str] = None
    website: Optional[str] = None
