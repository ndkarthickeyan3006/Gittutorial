from playwright.sync_api import sync_playwright

url = "https://www.accuweather.com/en/in/hosur-sarjapur-road-layout/3352280/hourly-weather-forecast/3352280"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto(url, wait_until="domcontentloaded", timeout=60000)
    print(page.title())


 #Navigation
    page.goto("https://www.accuweather.com/en/in/hosur-sarjapur-road-layout/3352280/hourly-weather-forecast/3352280")
    page.screenshot(path="accuweather.png")

    #click
    page.click("Hourly")
    page.screenshot(path="full_forecast.png")

    #typing
    page.fill("input[name=q]", "Playwright")
    page.press("input[name=q]", "Enter")
    page.screenshot(path="search_results.png")

    #waiting for elements
    page.wait_for_selector("text=Playwright: Fast and reliable end-to-end testing for modern ...")
    page.screenshot(path="search_results_loaded.png")

    #Extracting the data
    title = page.title()
    print(f"Page title: {title}")
    browser.close()