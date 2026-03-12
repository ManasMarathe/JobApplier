'''
Quick test script to diagnose Apply button clicking issues
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import json
from datetime import datetime

def analyze_buttons(driver):
    """Analyze all buttons on the current page"""
    print("\n" + "="*80)
    print("BUTTON ANALYSIS")
    print("="*80)
    
    buttons = driver.find_elements(By.TAG_NAME, "button")
    print(f"\nTotal buttons found: {len(buttons)}")
    
    # Look for apply buttons specifically
    apply_buttons = [
        btn for btn in buttons 
        if 'apply' in (btn.get_attribute('aria-label') or '').lower() or
           'apply' in btn.text.lower()
    ]
    
    print(f"Apply-related buttons found: {len(apply_buttons)}")
    
    for idx, btn in enumerate(apply_buttons):
        print(f"\n--- Apply Button {idx+1} ---")
        print(f"  Text: {btn.text[:60]}")
        print(f"  ID: {btn.get_attribute('id')}")
        print(f"  Class: {btn.get_attribute('class')[:100]}")
        print(f"  aria-label: {btn.get_attribute('aria-label')}")
        print(f"  aria-disabled: {btn.get_attribute('aria-disabled')}")
        print(f"  Visible: {btn.is_displayed()}")
        print(f"  Enabled: {btn.is_enabled()}")
        
        try:
            btn_rect = btn.rect
            print(f"  Position: x={btn_rect['x']}, y={btn_rect['y']}")
            print(f"  Size: {btn_rect['width']}x{btn_rect['height']}")
        except:
            print(f"  Position: [Could not get rect]")
    
    # Test each selector
    print(f"\n\n" + "="*80)
    print("TESTING SELECTORS")
    print("="*80)
    
    selectors = [
        (".//button[@id='jobs-apply-button-id']", "ID-based selector"),
        (".//button[contains(@class,'jobs-apply-button') and contains(@class, 'artdeco-button--3') and contains(@aria-label, 'Easy')]", "Legacy with Easy label"),
        (".//button[contains(@class,'jobs-apply-button') and contains(@class, 'artdeco-button--3')]", "Generic with classes"),
        (".//button[.//span[contains(normalize-space(.), 'Apply')]][@aria-label or @class]", "Span-based"),
        (".//button[contains(@aria-label, 'apply') or contains(@aria-label, 'Apply')]", "aria-label"),
        (".//button[contains(., 'Apply')]", "Text contains Apply"),
        ("//button[@aria-label and contains(translate(@aria-label, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'apply')]", "Case-insensitive aria"),
    ]
    
    for xpath, desc in selectors:
        try:
            elem = driver.find_element(By.XPATH, xpath)
            print(f"\n✓ FOUND with: {desc}")
            print(f"  XPath: {xpath[:80]}...")
            print(f"  Text: {elem.text[:60]}")
            print(f"  aria-label: {elem.get_attribute('aria-label')}")
        except NoSuchElementException:
            print(f"\n✗ NOT FOUND: {desc}")

def main():
    print("Apply Button Diagnostic Script")
    print("1. You must have Chrome running with the JobApplier profile")
    print("2. Navigate to a LinkedIn job page with an Apply button")
    print("3. This script will analyze the buttons and test selectors")
    print("\nPress Enter when ready...")
    input()
    
    # Try to connect to existing Chrome
    options = webdriver.ChromeOptions()
    options.add_argument("--user-data-dir=chrome_profile")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    try:
        driver = webdriver.Chrome(options=options)
        driver.get("https://www.linkedin.com/jobs/search/?keywords=Java%20Developer&location=India")
        
        wait = WebDriverWait(driver, 10)
        
        # Wait for job listings to load
        wait.until(EC.presence_of_all_elements_located((By.XPATH, "//li[@data-occludable-job-id]")))
        
        # Click first job
        first_job = driver.find_element(By.XPATH, "//li[@data-occludable-job-id]")
        first_job.click()
        
        # Wait for job details to load
        wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(@class, 'jobs-details-main-content')]")))
        
        # Now analyze buttons
        analyze_buttons(driver)
        
        input("\nPress Enter to close...")
        driver.quit()
        
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
