from playwright.sync_api import sync_playwright

def get_product_urls(playwright, search_terms):
    browser = playwright.chromium.launch(headless=False, args=["--disable-http2"])
    page = browser.new_page()
    base_url = "https://www.kingsoopers.com"
    urls = []

    for term in search_terms:
        search_url = f"{base_url}/search?query={term}&searchType=default_search"
        page.goto(search_url, wait_until='load')
        elements = page.query_selector_all('a[href*="/p/"]')
        
        if elements:
            # Take the first relevant result
            url = elements[0].get_attribute('href')
            if url:
                full_url = base_url + url
                urls.append((term, full_url))
    
    return browser, page, urls

def get_aisle_locations(page, product_urls):
    aisle_info = {}

    for term, url in product_urls:
        page.goto(url, wait_until='load')
        try:
            page.wait_for_selector("span[data-testid='product-details-location']", timeout=5000)
            text = page.locator("span[data-testid='product-details-location']").text_content()
            aisle_info[term] = text.strip() if text else "Not found"
        except:
            aisle_info[term] = "Not found or Timeout"
    
    return aisle_info

def main():
    with open("grocerylist.txt", "r") as f:
        products = [line.strip() for line in f if line.strip()]

    with sync_playwright() as p:
        browser, page, product_urls = get_product_urls(p, products)
        aisle_data = get_aisle_locations(page, product_urls)
        browser.close()

    for product, aisle in aisle_data.items():
        print(f"{product}: {aisle}")

if __name__ == "__main__":
    main()
