import sys
from playwright.sync_api import sync_playwright
import datetime
import calendar
# 从命令行读取参数
import argparse

def run(playwright, args):
    chromium = playwright.chromium # or "firefox" or "webkit".
    browser = chromium.launch(
        headless = True,
        slow_mo = 200
    )
    page = browser.new_page()
    page.goto("http://eds.newtouch.cn/eds3/")

    handle_login(page, args.name, args.password)

    page.on("dialog", lambda dialog: handle_dialog(dialog, dateStr))
    
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
    page.on("dialog", lambda dialog: print("login action" + ": " + dialog.message))
    page.locator("input#UserId").fill(name)
    page.locator("input#UserPassword").fill(password)
    page.locator("button#btnSubmit").click()

def check_login_error(dialog):
    print("login action" + ": " + dialog.message)
    if (dialog.message == "用户名或密码错误"):
        sys.exit()
    
def handle_dialog(dialog, dateStr):
    print(dateStr + ": " + dialog.message)
    dialog.accept()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", help="login user name", required=True)
    parser.add_argument("--password", help="login user password", required=True)
    args = parser.parse_args()

    with sync_playwright() as playwright:
        run(playwright, args)