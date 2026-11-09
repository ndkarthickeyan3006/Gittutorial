
from playwright.sync_api import sync_playwright, TimeoutError
import re

# Start Playwright
with sync_playwright() as p:

    # Open Chrome browser
    browser = p.chromium.launch(headless=False)

    # Create a new page
    page = browser.new_page()

    # Open Cricbuzz website
    page.goto("https://www.cricbuzz.com/")

    print("Opening Cricbuzz website...")

    try:
        # Find cricket score elements using text pattern
        score_locator = page.get_by_text(
            re.compile(r"\b\d{1,3}-\d{1,2}")
        )

        # Wait until a score appears
        score_locator.first.wait_for(
            state="visible",
            timeout=30000
        )

        # Get all visible page text
        page_text = page.locator("body").inner_text()

        # Extract cricket scores using regular expression
        scores = re.findall(
            r"\b\d{1,3}-\d{1,2}(?:\s*\(\d+(?:\.\d+)?\))?",
            page_text
        )

        # Print scores in terminal
        print("\nLive Cricket Scores:")

        if scores:
            for score in scores:
                print(score)
        else:
            print("No cricket scores found.")

    except TimeoutError:
        print("No live score found within 30 seconds.")

    # Take screenshot
    page.screenshot(path="score.png", full_page=True)

    print("\nScreenshot saved as score.png")

    # Close browser
    browser.close()
