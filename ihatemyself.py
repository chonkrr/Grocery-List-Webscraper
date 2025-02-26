from playwright.sync_api import sync_playwright

def extract_urls():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--disable-http2"])  # Change to True if you don't want to see the browser
        page = browser.new_page()

        # Go to the provided search page URL
        search_url = "https://www.kingsoopers.com/search?query=eggs&searchType=default_search"
        page.goto(search_url)

        # Locate all <a> tags that contain the product links based on the href pattern
        elements = page.query_selector_all('a[href*="/p/"]')

        if elements and len(elements) > 1:
            # Skip the first element and get the next three links
            links = elements[1:4]
            for link in links:
                url = link.get_attribute('href')
                full_url = page.url.split('/search?')[0] + url  # Append the relative URL to the base URL
                print(full_url)
        else:
            print("Not enough elements found")

        browser.close()

extract_urls()
