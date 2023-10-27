import asyncio

from secrets import get_acp_pass
from playwright.sync_api import Page, expect

from playwright.sync_api import sync_playwright


def upload_to_acp(path_to_rtml: str):
    with sync_playwright() as p:
        # Open browser and go to ACP
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        acp_login = get_acp_pass()

        authenticated_url = f"http://{acp_login["username"]}:{acp_login["password"]}@10.0.0.71"

        page.goto(authenticated_url, timeout=0) #Don't timeout, our server is really slow. 

        # Naviagte to upload page
        scheduled_div = page.query_selector_all("text=Scheduled")[0]

        scheduled_div.click()
        page.query_selector("text=Upload RTML").click()

        # Upload RTML
        page.screenshot(path="upload0.png")
        input_element = page.wait_for_selector("text=Choose File", timeout=100000)
        input_element.set_input_files(f"{path_to_rtml}")

        page.screenshot(path="upload1.png")

        # Submit
        page.get_by_label("Enable immediately").click()
        page.screenshot(path="upload2.png")
        #page.wait_for_selector("text=Submit RTML").click()
        browser.close()


upload_to_acp(path_to_rtml="./rtml_pointings/GW_Followup_Pointings.rtml")
