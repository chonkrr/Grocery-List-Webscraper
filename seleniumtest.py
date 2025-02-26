from playwright.sync_api import sync_playwright

url = "https://www.kingsoopers.com/p/eggland-s-best-cage-free-large-white-eggs-24-count/0071514151453"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, args=["--disable-http2"])  # Use HTTP/1.1
    page = browser.new_page()
    page.goto(url, timeout=60000)  # Load page with a timeout

    aisle_info = page.locator("span[data-testid='product-details-location']").text_content()

    if aisle_info:
        print("Aisle Information:", aisle_info.strip())
    else:
        print("Aisle information not found.")

    browser.close()

