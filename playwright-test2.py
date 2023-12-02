from playwright.sync_api import Playwright, sync_playwright, expect
from datetime import datetime

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://3-shake.com/")
    page.wait_for_timeout(5000)
    current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    screenshot_filename = f"screenshot_top_{current_datetime}.png"
    page.screenshot(path=screenshot_filename)
    page.wait_for_timeout(5000)
    page.get_by_role("banner").get_by_role("link", name="About Us").click()
    page.wait_for_timeout(5000)
    current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    screenshot_filename = f"screenshot_about_{current_datetime}.png"
    page.screenshot(path=screenshot_filename)
    page.wait_for_timeout(5000)
    page.get_by_role("banner").get_by_role("link", name="Services").click()
    page.wait_for_timeout(5000)
    current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    screenshot_filename = f"screenshot_sec-services_{current_datetime}.png"
    page.screenshot(path=screenshot_filename)
    page.wait_for_timeout(5000)
    page.get_by_role("banner").get_by_role("link", name="News").click()
    page.wait_for_timeout(5000)
    current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    screenshot_filename = f"screenshot_news_{current_datetime}.png"
    page.screenshot(path=screenshot_filename)
    page.wait_for_timeout(5000)
    page.get_by_role("banner").get_by_role("link", name="Recruit").click()
    page.wait_for_timeout(5000)
    current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    screenshot_filename = f"screenshot_recruit_{current_datetime}.png"
    page.screenshot(path=screenshot_filename)
    page.wait_for_timeout(5000)

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
