import os
from playwright.sync_api import sync_playwright
import datetime
import calendar
# 从命令行读取参数
import argparse

def run(playwright, args):
    chromium = playwright.chromium # or "firefox" or "webkit".
    browser = chromium.launch(
        headless = True,
        # slow_mo = 200
    )
    page = browser.new_page()
    page.goto("http://eds.newtouch.cn/eds3/")

    page.on("dialog", handle_dialog)

    handle_login(page, args.name, args.password)

    # 获取当前年份和月份
    now = datetime.datetime.now()
    year = now.year
    month = now.month
    # 获取当月总天数
    total_days = calendar.monthrange(year, month)[1]
    # 遍历每一天的日期
    for day in range(1, total_days + 1):
        dateStr = datetime.date(year, month, day).strftime("%Y-%m-%d")
        page.goto("http://eds.newtouch.cn/eds3/worklog.aspx?LogDate=" + dateStr)
        table = page.locator("table#dgWorkLogList")
        if table.count() > 0:
            print(dateStr + " EDS done....")
        else: 
            page.locator("input#txtStartTime").fill("09:00")
            page.locator("input#txtEndTime").fill("12:00")
            page.locator("textarea#txtMemo").fill("开发")
            page.locator("input#btnSave").click()

            page.locator("input#txtStartTime").fill("13:00")
            page.locator("input#txtEndTime").fill("18:00")
            page.locator("textarea#txtMemo").fill("开发")
            page.locator("input#btnSave").click()
        
    # other actions...
    browser.close()

def handle_login(page, name, password):
    page.locator("input#UserId").fill(name)
    page.locator("input#UserPassword").fill(password)
    page.locator("button#btnSubmit").click()
    
def handle_dialog(dialog):
    print(f"dialog msg: {dialog.message}")
    if (dialog.message == "用户名或密码错误"):
        print("程序终止...请检查用户名密码是否正确")
        os._exit(1)
    else:
        dialog.accept()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", help="login user name", required=True)
    parser.add_argument("--password", help="login user password", required=True)
    parser.add_argument("--msg", help="EDS content message, such as '代码开发'", default="代码开发")
    args = parser.parse_args()

    with sync_playwright() as playwright:
        run(playwright, args)