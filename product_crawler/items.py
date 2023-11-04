import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, Join, MapCompose, Compose
import re

class AmazonProduct(scrapy.Item):
    product_id = scrapy.Field()
    product_title = scrapy.Field()
    product_price = scrapy.Field()
    list_price = scrapy.Field()
    currency_id = scrapy.Field()
    listing_url = scrapy.Field()
    manufacturer = scrapy.Field()
    upc = scrapy.Field()
    model_name = scrapy.Field()
    product_dimensions = scrapy.Field()
    customer_ratings = scrapy.Field()
    average_rating = scrapy.Field()
    image_url = scrapy.Field()
    title_desc = scrapy.Field()
    product_weight = scrapy.Field()
    marketplace_id = scrapy.Field()
    seller_url = scrapy.Field()
    seller_name = scrapy.Field()


def handle_data(value):
    if value is None:
        return ""
    value = value.strip().replace('\u200e', '')
    return value

def handle_none(value):
    if value is None:
        return ""
    return value
       
def remove_ratings(value):
    if value is None:
        return ""
    cleaned_text = re.sub(r'\brating\b|\bratings\b', '', value, flags=re.IGNORECASE)
    return ' '.join(cleaned_text.split())

def clean_url(url):
    ref_index = url.find("ref=")
    if ref_index != -1:
        return url[:ref_index]
    else:
        return url
    
def clean_img(url):
    cleaned_url = re.sub(r'(\.[^\.]+)\.jpg$', r'.jpg', url)
    return cleaned_url

def split_title(text):
    segments = re.split(r'[|,]', text)
    return segments[0]

def split_desc(text):
    segments = re.split(r'[|,]', text)
    return segments[1:]

def remove_commas(text):
    return text.replace(",", "")

def clean_dimensions(dimensions):
    cleaned_dimensions = dimensions.replace("inches", "").replace('"', "").replace("W", "").replace("H", "").strip()
    return cleaned_dimensions

def clean_weight(value):
    clean_weight = value.replace("pounds", "lbs").replace("Pounds", "lbs").replace("ounces", "oz").replace("Ounces", "oz").strip()
    return clean_weight

def remove_symbol(value):
    if value is None:
        return ""
    value.split("$")[-1]
    return value

    
def combine_or_deduplicate_upc(values):
    """
    Function to combine or deduplicate UPCs based on conditions.

    Arguments:
    - values: List of UPC values extracted by the selectors.

    Returns:
    - A single combined or deduplicated UPC value as a string.
    """
    if len(values) == 0:
        return None  # No UPCs found

    # Remove any None or empty values
    cleaned_values = [value for value in values if value is not None and value.strip() != '']

    if len(cleaned_values) == 0:
        return None  # No valid UPCs found

    unique_values = set(cleaned_values)  # Deduplicate

    if len(unique_values) == 1:
        return next(iter(unique_values))  # Return the single unique UPC
    else:
        return "-".join(sorted(unique_values))  # Combine different UPCs, sorted
    
    

class AmazonProductLoader(ItemLoader):
    
    default_output_processor = TakeFirst()
    
    product_title_in = MapCompose(str.strip, split_title)
    title_desc_in = MapCompose(split_desc, str.strip)
    product_price_in = MapCompose(lambda x: x.split("$")[-1])
    list_price_in = MapCompose(lambda x: x.split("$")[-1])
    listing_url_in = MapCompose(clean_url)
    manufacturer_in = MapCompose(handle_data)
    upc_in = MapCompose(handle_data)
    model_name_in = MapCompose(handle_data, remove_commas)
    product_dimensions_in = MapCompose(handle_data, clean_dimensions)
    customer_ratings_in = MapCompose(remove_ratings)
    average_ratings_in = MapCompose(handle_none)
    image_url_in = MapCompose(clean_img)
    product_weight_in = MapCompose(handle_data, clean_weight)
    

