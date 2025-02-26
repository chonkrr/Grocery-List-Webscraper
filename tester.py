from playwright.sync_api import sync_playwright

def get_product_url():
    with sync_playwright() as p:
        # Launch the browser in headless mode
        browser = p.chromium.launch(headless=False, args=["--disable-http2"])  # Use HTTP/1.1
        page = browser.new_page()

        # Go to the page (you can keep the timeout higher to ensure it loads properly)
        page.goto("https://www.kingsoopers.com/search?query=eggs&searchType=default_search", timeout=60000)

        # Wait for at least one product link to appear
        page.wait_for_selector("a[aria-label][href]", timeout=30000)  # Wait for anchor tags with both aria-label and href

        # Extract the first product URL
        product_link = page.locator('a[aria-label][href]').first  # Use .first to get the first match
        url = product_link.get_attribute('href')  # Get href attribute

        # Print and return the first product URL
        print(url)

        browser.close()  # Close the browser
        return url  # Return the single product URL

# Get the first product URL
url = get_product_url()
print(url)
