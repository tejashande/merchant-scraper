from setuptools import setup, find_packages

setup(
    name="merchant_scraper",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "googlemaps==4.10.0",
        "openpyxl==3.1.2",
        "python-dateutil==2.8.2",
    ],
) 