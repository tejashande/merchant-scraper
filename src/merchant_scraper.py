class MerchantScraper:
    def map_business_type_to_mcc(self, business_type: str) -> str:
        """Map a business type to its corresponding MCC category."""
        business_type_to_mcc = {
            "restaurant": "Food & Beverage",
            "grocery_or_supermarket": "Retail",
            "retail": "Retail",
            "service": "Services",
            "entertainment": "Entertainment",
            "travel": "Travel",
            "automotive": "Automotive",
            "health": "Healthcare",
            "education": "Education",
            "other": "Other",
        }
        return business_type_to_mcc.get(business_type.lower(), "Other")
