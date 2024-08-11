#4th branch!


# ~ ~ ~ ~

from bs4 import BeautifulSoup
import requests

def get_amazon_product_price(url):
    # Send a GET request to the Amazon product page
    response = requests.get(url)
    print("status code is ", response.status_code)
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the span element with the class 'aok-offscreen'
        price_whole = soup.find('span', {'class': 'a-price-whole'})
        price_dec = soup.find('span', {'class': 'a-price-decimal'})
        #print(price_whole)
        # Check if the price element was found
        if price_whole and price_dec:
            # Extract the text content within the span element
            price_w = price_whole.text.strip()
            price_d = price_dec.text.strip()
            print("price is: ",price_w + price_d)
            return price_w + price_d
        else:
            return 'Price not found'
    else:
        return 'Failed to retrieve data'

# Example usage
amazon_url = 'https://www.amazon.com/dp/B0113UZJE2'
product_price = get_amazon_product_price(amazon_url)
print('Product Price:', product_price)
