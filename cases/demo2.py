import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.baidu.com/")
    page.locator("#kw").click()
    page.locator("#kw").fill("joyce")
    page.get_by_role("button", name="百度一下").click()

    # ---------------------
   # context.close()
   ## browser.close()


with sync_playwright() as playwright:
    run(playwright)