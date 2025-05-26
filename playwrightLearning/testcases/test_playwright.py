
from playwright.sync_api import sync_playwright, expect, Browser
from playwright.sync_api import Page
from requests import options


def test_first_example(page):

    page.goto("https://way2automation.com")
    # page.set_viewport_size({"width": 1920, "height": 1080})

    title = page.title()
    print(title)
    assert "Way2Automation" in title
    page.wait_for_timeout(2000)
    page.goto("http://gmail.com")
    page.wait_for_timeout(2000)
    page.go_back()
    page.wait_for_timeout(2000)
    page.go_forward()
    page.wait_for_timeout(2000)
    page.reload()

def test_finding_elements(page):
    page.goto("https://gmail.com")
    #id, xpath, css, name, className, tahName, linkText, partialiLinkText
    # page.locator("//*[@id='identifierId']").fill("trainer@way2automation.com")
    page.get_by_label("Email or phone", exact=True).fill("trainer@way2automation.com")
    # page.get_by_role("button", name="Next").click()
    page.locator("button").filter(has_text="Next").click()
    page.get_by_label("Enter your password").fill("sdfsdfsf")
    page.locator("button").filter(has_text="Next").nth(1).click()
    page.wait_for_timeout(2000)
    error_message = page.get_by_text("Wrong").inner_text()
    print(error_message)
    assert "Wrong password" in error_message, "Test failed"

def test_handling_dropdown(page):
    page.goto("https://wikipedia.org")
    # page.wait_for_timeout(2000)
    # page.select_option("select", label="Eesti")
    page.select_option("select", value="hi")
    # page.wait_for_timeout(2000)

    options = page.locator("option").all()
    print(f"Total values are : {len(options)}")

    num = 0
    for option in options:
        text = option.inner_text()
        lang = option.get_attribute("lang")
        num += 1
        print(f"{num}. {lang}  :  {text}")


def test_handling_links(page):
    page.goto("https://wikipedia.org")
    block = page.locator("//*[@id='www-wikipedia-org']/footer/nav")
    links = block.locator("a").all()
    # links = page.locator("a").all()
    print(f"Total links: {len(links)}")
    num = 0
    for link in links:
        text = link.inner_text()
        url = link.get_attribute("href")
        num += 1
        print(f"{num}.{text}  :  {url}")

def test_checkboxes(page):
    page.goto("http://www.tizag.com/htmlT/htmlcheckboxes.php")

    block = page.locator("//html/body/table[3]/tbody/tr[1]/td[2]/table/tbody/tr/td/div[4]")
    checkboxes = block.locator("[name='sports']")
    checkboxes_count = checkboxes.count()
    print(checkboxes_count)

    for i in range(checkboxes_count):
        checkboxes.nth(i).click()

def test_assertions(page):
    page.goto("http://www.tizag.com/htmlT/htmlcheckboxes.php")

    expect(page).to_have_url("http://www.tizag.com/htmlT/htmlcheckboxes.php")
    print("URL Assertion passed")

    expect(page).not_to_have_url("error")
    print("No errors on the page hence passed")

    expect(page).to_have_title("HTML Tutorial - Checkboxes")
    print("Title is correct9")


def test_slider(page):
    page.goto("https://jqueryui.com/resources/demos/slider/default.html")

    slider = page.locator("//*[@id='slider']/span")

    bounding_box = slider.bounding_box()
    start_x = bounding_box["x"] + bounding_box["width"] / 2
    start_y = bounding_box["y"] + bounding_box["height"] / 2
    page.mouse.move(start_x, start_y)
    page.wait_for_timeout(3000)
    page.mouse.down()
    page.mouse.move(start_x + 400, start_y)
    page.mouse.up()
    page.wait_for_timeout(3000)

def test_resize(page):
    page.goto("https://jqueryui.com/resources/demos/resizable/default.html")

    slider_resize = page.locator("//*[@id='resizable']/div[3]")

    bounding_box_resize = slider_resize.bounding_box()
    start_x = bounding_box_resize["x"] + bounding_box_resize["width"] / 2
    start_y = bounding_box_resize["y"] + bounding_box_resize["height"] / 2
    page.mouse.move(start_x, start_y)
    page.wait_for_timeout(1000)
    page.mouse.down()
    page.mouse.move(start_x + 400, start_y + 400)
    page.mouse.up()
    page.wait_for_timeout(1000)

def test_drag_drop(page):
    page.goto("https://jqueryui.com/resources/demos/droppable/default.html")

    draggable = page.locator("#draggable")
    droppable = page.locator("#droppable")

    draggable_box = draggable.bounding_box()
    droppable_box = droppable.bounding_box()
    page.wait_for_timeout(2000)
    page.mouse.move(
        draggable_box["x"] + draggable_box["width"] / 2,
        droppable_box["y"] + droppable_box["height"] / 2
    )

    page.mouse.down()
    page.mouse.move(
        droppable_box["x"] + droppable_box["width"] / 2,
        droppable_box["y"] + droppable_box["height"] / 2
    )
    page.mouse.up()
    page.wait_for_timeout(2000)

def test_right_click(page):
    page.goto("https://deluxe-menu.com/popup-mode-sample.html")
    page.locator("//p[2]/img").click(button="right")
    page.wait_for_timeout(1000)

def test_alert(page):


    def dialog_handler(dialog):
        page.wait_for_timeout(2000)
        print(dialog.message())
        dialog.accept()

    page.on("dialog", dialog_handler)
    page.goto("https://mail.rediff.com/cgi-bin/login.cgi")
    page.locator("[type='submit']").click()

def test_tryit(page):
    page.goto("https://www.w3schools.com/html/tryit.asp?filename=tryhtml_form_submit", wait_until="domcontentloaded")

    frame = page.frame_locator("#iframeResult")

    frame.locator("#fname").clear()
    frame.locator("#fname").fill("Ivan")

    frame.locator("#lname").clear()
    frame.locator("#lname").fill("saff")

    frame.locator("[type='submit']").evaluate("(element) => {element.style.border = '3px solid red';}")
    # frame.locator("[type='submit']").click()

    frame.locator("[type='submit']").screenshot(path='screenshot/element.png')

    page.wait_for_timeout(2000)
    page.screenshot(path='screenshot/page.png')

def test_tabs_and_popups(page):
    page.goto("https://sso.teachable.com/secure/673/identity/sign_up/otp")

    # with page.expect_popup() as popup_info:
    page.locator("text=Privacy").nth(0).click()

    # popup = popup_info.value
    page.locator("//*[@id='header-sign-up-btn']").click()

def test_http_auth(page, browser: Browser):
    context = browser.new_context(
        http_credentials={"username":"admin",
                          "password":"admin"}
    )
    page = context.new_page()

    page.goto("https://the-internet.herokuapp.com/basic_auth")

    page.wait_for_timeout(2000)

def test_api_get():
    with sync_playwright() as p:
        request_context = p.request.new_context()
        response = request_context.get("http://localhost:8080/api/users/1")

        assert response.status == 200, f"Unexpected status code: {response.status}"
        print(f"status code {response.status}")
        print(f"response body: {response.text()}")

        json_respons = response.json()
        print(json_respons.get("firstName"))
        assert json_respons.get("firstName") == "Rahul", f"Expected 'Rahul' but got {json_respons.get('firstName')}"

def test_api_post():
    with sync_playwright() as p:
        request_context = p.request.new_context()
        respnose = request_context.post("http://localhost:8080/api/users", data={"email":"trump@way.com", "firstName":"Donald", "lastName":"trump"},
                             headers={"Content-Type":"application/json"})

        print(f"status code{respnose.status}")
        assert respnose.status == 201, f"Unexpected status code : {respnose.status}"
        print(f"Response body : {respnose.text()}")
