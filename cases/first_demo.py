from playwright.sync_api import Page, expect
import re

def test(page:Page):
    page.goto("https://www.baidu.com")

    #判断页面title 是否包含百度
    expect(page).to_have_title(re.compile("百度一下"))

    #定位并输入搜索内容：Joyce
    input_text = page.locator("#kw")
    input_text.fill("Joyce")

    #定位并点击百度button
    btn = page.locator("text=百度一下")
    btn.click()

