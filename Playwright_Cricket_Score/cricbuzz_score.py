import re
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError

URL = "https://www.cricbuzz.com/cricket-match/live-scores"
SCREENSHOT_FILE = "score.png"

SCORE_RE = re.compile(r"\b(?:[A-Z]{2,5}\s*)?\d{1,3}[/-]\d{1,2}(?:\s*\([\d.]+\s*Ov\))?\b", re.I)
MATCH_NAME_RE = re.compile(r"\b[A-Z]{2,5}\s+vs\s+[A-Z]{2,5}\b", re.I)
LIVE_HINT_RE = re.compile(
    r"(need\s+\d+\s+runs?|trail\s+by\s+\d+\s+runs?|stumps|day\s+\d+|innings|target|required\s+\d+|live)",
    re.I,
)
RESULT_HINT_RE = re.compile(r"(won\s+by|beat|defeated|drew|abandoned|no result)", re.I)


def clean(text: str) -> str:
    return re.sub(r"\s+", " ", text or "").strip()


def extract_output_lines(page_text: str):
    lines = [clean(line) for line in page_text.splitlines() if clean(line)]

    candidates = []
    for idx, line in enumerate(lines):
        if not SCORE_RE.search(line):
            continue

        nearby = lines[idx: idx + 6]
        nearby_text = " | ".join(nearby)

        status_line = None
        for probe in nearby[1:]:
            if MATCH_NAME_RE.search(probe) or LIVE_HINT_RE.search(probe) or RESULT_HINT_RE.search(probe):
                status_line = probe
                break

        if status_line is None:
            for probe in lines:
                if probe != line and (MATCH_NAME_RE.search(probe) or LIVE_HINT_RE.search(probe) or RESULT_HINT_RE.search(probe)):
                    status_line = probe
                    break

        priority = 0
        if LIVE_HINT_RE.search(nearby_text):
            priority = 3
        elif MATCH_NAME_RE.search(nearby_text):
            priority = 2
        elif RESULT_HINT_RE.search(nearby_text):
            priority = 1

        candidates.append((priority, idx, line, status_line))

    if not candidates:
        return None, None

    candidates.sort(key=lambda item: (-item[0], item[1]))
    _, _, score_line, status_line = candidates[0]
    return score_line, status_line


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    try:
        page.goto(URL, wait_until="domcontentloaded", timeout=30000)
        page.wait_for_selector("body", timeout=30000)

        page_text = page.inner_text("body")
        score_line, status_line = extract_output_lines(page_text)

        page.screenshot(path=SCREENSHOT_FILE, full_page=True)

        if score_line:
            print(score_line)
            if status_line:
                print(status_line)
        else:
            print("No score found right now.")

        print(f"saved {SCREENSHOT_FILE}")

    except PlaywrightTimeoutError:
        page.screenshot(path=SCREENSHOT_FILE, full_page=True)
        print("No score found right now.")
        print(f"saved {SCREENSHOT_FILE}")
    finally:
        browser.close()