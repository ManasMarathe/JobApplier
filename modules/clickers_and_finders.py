'''
Author:     Manas Marathe
LinkedIn:   https://www.linkedin.com/in/manas-marathe-129942123/

Copyright (C) 2024 Manas Marathe

License:    GNU Affero General Public License
            https://www.gnu.org/licenses/agpl-3.0.en.html
            
GitHub:     https://github.com/ManasMarathe/JobApplier

version:    24.12.29.12.30
'''

from config.settings import click_gap, smooth_scroll
from modules.helpers import buffer, print_lg, sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains

# Click Functions
def wait_span_click(driver: WebDriver, text: str, time: float=5.0, click: bool=True, scroll: bool=True, scrollTop: bool=False) -> WebElement | bool:
    '''
    Finds the span element with the given `text`.
    - Returns `WebElement` if found, else `False` if not found.
    - Clicks on it if `click = True`.
    - Will spend a max of `time` seconds in searching for each element.
    - Will scroll to the element if `scroll = True`.
    - Will scroll to the top if `scrollTop = True`.
    '''
    if text:
        try:
            button = WebDriverWait(driver,time).until(EC.presence_of_element_located((By.XPATH, './/span[normalize-space(.)="'+text+'"]')))
            if scroll:  scroll_to_view(driver, button, scrollTop)
            if click:
                button.click()
                buffer(click_gap)
            return button
        except Exception as e:
            print_lg("Click Failed! Didn't find '"+text+"'")
            # print_lg(e)
            return False

def multi_sel(driver: WebDriver, texts: list, time: float=5.0) -> None:
    '''
    - For each text in the `texts`, tries to find and click `span` element with that text.
    - Will spend a max of `time` seconds in searching for each element.
    '''
    for text in texts:
        ##> ------ Dheeraj Deshwal : dheeraj20194@iiitd.ac.in/dheerajdeshwal9811@gmail.com - Bug fix ------
        wait_span_click(driver, text, time, False)
        ##<
        try:
            button = WebDriverWait(driver,time).until(EC.presence_of_element_located((By.XPATH, './/span[normalize-space(.)="'+text+'"]')))
            scroll_to_view(driver, button)
            button.click()
            buffer(click_gap)
        except Exception as e:
            print_lg("Click Failed! Didn't find '"+text+"'")
            # print_lg(e)

def multi_sel_noWait(driver: WebDriver, texts: list, actions: ActionChains = None) -> None:
    '''
    - For each text in the `texts`, tries to find and click `span` element with that class.
    - If `actions` is provided, bot tries to search and Add the `text` to this filters list section.
    - Won't wait to search for each element, assumes that element is rendered.
    '''
    for text in texts:
        try:
            button = driver.find_element(By.XPATH, './/span[normalize-space(.)="'+text+'"]')
            scroll_to_view(driver, button)
            button.click()
            buffer(click_gap)
        except Exception as e:
            if actions: company_search_click(driver,actions,text)
            else:   print_lg("Click Failed! Didn't find '"+text+"'")
            # print_lg(e)

def boolean_button_click(driver: WebDriver, actions: ActionChains, text: str) -> None:
    '''
    Tries to click on the boolean switch/toggle with the given label `text` (e.g. "Easy Apply").
    Tries multiple selectors to cope with LinkedIn UI changes.
    '''
    xpath_strategies = [
        # Original: h3 label inside fieldset
        './/h3[normalize-space()="' + text + '"]/ancestor::fieldset//input[@role="switch"]',
        # Any element with exact text, then ancestor fieldset
        './/*[normalize-space(.)="' + text + '"]/ancestor::fieldset//input[@role="switch"]',
        # Fieldset that contains the label text anywhere
        './/fieldset[.//*[normalize-space(.)="' + text + '"]]//input[@role="switch"]',
        # Label or span with text, then any ancestor that contains a switch
        './/*[normalize-space(.)="' + text + '"]/ancestor::*[.//input[@role="switch"]]//input[@role="switch"]',
        # Switch whose preceding sibling or ancestor contains the text (for flex/div layouts)
        './/input[@role="switch"][ancestor::*[.//*[normalize-space(.)="' + text + '"]]]',
    ]
    for xpath in xpath_strategies:
        try:
            button = driver.find_element(By.XPATH, xpath)
            scroll_to_view(driver, button)
            actions.move_to_element(button).click().perform()
            buffer(click_gap)
            return
        except Exception:
            continue
    print_lg("Click Failed! Didn't find '" + text + "'")

# Find functions
def find_by_class(driver: WebDriver, class_name: str, time: float=5.0) -> WebElement | Exception:
    '''
    Waits for a max of `time` seconds for element to be found, and returns `WebElement` if found, else `Exception` if not found.
    '''
    return WebDriverWait(driver, time).until(EC.presence_of_element_located((By.CLASS_NAME, class_name)))

# Scroll functions
def scroll_to_view(driver: WebDriver, element: WebElement, top: bool = False, smooth_scroll: bool = smooth_scroll) -> None:
    '''
    Scrolls the `element` to view.
    - `smooth_scroll` will scroll with smooth behavior.
    - `top` will scroll to the `element` to top of the view.
    '''
    if top:
        return driver.execute_script('arguments[0].scrollIntoView();', element)
    behavior = "smooth" if smooth_scroll else "instant"
    return driver.execute_script('arguments[0].scrollIntoView({block: "center", behavior: "'+behavior+'" });', element)

# Enter input text functions
def text_input_by_ID(driver: WebDriver, id: str, value: str, time: float=5.0) -> None | Exception:
    '''
    Enters `value` into the input field with the given `id` if found, else throws NotFoundException.
    - `time` is the max time to wait for the element to be found.
    '''
    username_field = WebDriverWait(driver, time).until(EC.presence_of_element_located((By.ID, id)))
    username_field.send_keys(Keys.CONTROL + "a")
    username_field.send_keys(value)

def try_xp(driver: WebDriver, xpath: str, click: bool=True, wait_time: float=5.0) -> WebElement | bool:
    '''
    Tries to find and optionally click an element using XPath.
    - Waits up to `wait_time` seconds for the element to be present and clickable.
    - Returns the element if found (and not clicking), True if clicked, False if not found.
    '''
    try:
        if click:
            # Wait for element to be clickable before clicking
            element = WebDriverWait(driver, wait_time).until(
                EC.element_to_be_clickable((By.XPATH, xpath))
            )
            scroll_to_view(driver, element)
            element.click()
            return True
        else:
            # Just wait for presence
            element = WebDriverWait(driver, wait_time).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            return element
    except Exception as e:
        return False

def click_apply_button(driver: WebDriver) -> bool:
    '''
    Clicks the Apply button on LinkedIn job posting.
    Tries multiple XPath strategies to handle LinkedIn UI variations and Easy Apply vs External Apply buttons.
    Returns True if clicked, False if not found.
    '''
    apply_button_xpaths = [
        # Primary: Modern Easy Apply button with ID
        ".//button[@id='jobs-apply-button-id']",
        
        # Legacy: Apply button with Easy Apply aria-label
        ".//button[contains(@class,'jobs-apply-button') and contains(@class, 'artdeco-button--3') and contains(@aria-label, 'Easy')]",
        
        # Generic: Apply button with class (without Easy label requirement)
        ".//button[contains(@class,'jobs-apply-button') and contains(@class, 'artdeco-button--3')]",
        
        # Fallback: Any button containing 'Apply' text in a span
        ".//button[.//span[contains(normalize-space(.), 'Apply')]][@aria-label or @class]",
        
        # Alternative: Button with aria-label containing 'apply'
        ".//button[contains(@aria-label, 'apply') or contains(@aria-label, 'Apply')]",
    ]
    
    for xpath in apply_button_xpaths:
        if try_xp(driver, xpath, click=True, wait_time=3.0):
            print_lg(f"Successfully clicked Apply button using XPath: {xpath}")
            buffer(click_gap)
            return True
    
    print_lg("Failed to find and click Apply button with any selector")
    return False

def try_linkText(driver: WebDriver, linkText: str) -> WebElement | bool:
    try:    return driver.find_element(By.LINK_TEXT, linkText)
    except:  return False

def try_find_by_classes(driver: WebDriver, classes: list[str]) -> WebElement | ValueError:
    for cla in classes:
        try:    return driver.find_element(By.CLASS_NAME, cla)
        except: pass
    raise ValueError("Failed to find an element with given classes")

def company_search_click(driver: WebDriver, actions: ActionChains, companyName: str) -> None:
    '''
    Tries to search and Add the company to company filters list.
    '''
    wait_span_click(driver,"Add a company",1)
    search = driver.find_element(By.XPATH,"(.//input[@placeholder='Add a company'])[1]")
    search.send_keys(Keys.CONTROL + "a")
    search.send_keys(companyName)
    buffer(3)
    actions.send_keys(Keys.DOWN).perform()
    actions.send_keys(Keys.ENTER).perform()
    print_lg(f'Tried searching and adding "{companyName}"')

def text_input(actions: ActionChains, textInputEle: WebElement | bool, value: str, textFieldName: str = "Text") -> None | Exception:
    if textInputEle:
        sleep(1)
        # actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
        textInputEle.clear()
        textInputEle.send_keys(value.strip())
        sleep(2)
        actions.send_keys(Keys.ENTER).perform()
    else:
        print_lg(f'{textFieldName} input was not given!')