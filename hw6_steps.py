from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


BUTTON_LINK = (By.CSS_SELECTOR, 'a[href="https://www.amazon.com/gp/feature.html?docId=1000625601"]')
AMAZON_APP_IMG = (By.CSS_SELECTOR, "[alt='The Amazon app']")

@given('Open Amazon T&C page')
def open_page(context):
    context.driver.get(f'https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')

@when('Store original windows')
def store(context):
    context.original_windows = context.driver.window_handles
    context.original_window = context.driver.current_window_handle
    print(context.original_windows)
    print(context.original_window)

@when('Click on  link')
def click_on_butn(context):
    button_link = context.driver.find_element(*BUTTON_LINK)
    button_link.click()

@when('Switch to window')
def switch_windows(context):
    context.driver.wait.until(EC.new_window_is_opened)
    context.new_windows = context.driver.window_handles
    print(context.new_windows)
    for window in context.original_windows:
        context.new_windows.remove(window)
    print(context.new_windows)
    context.driver.switch_to_window(context.new_windows[0])

@then('page is opened')
def check_app_page(context):
    context.driver.find_element(*AMAZON_APP_IMG)

@then('close new window and switch back to original')
def switch_back(context):
    context.driver.close()
    context.driver.switch_to_window(context.original_window)















