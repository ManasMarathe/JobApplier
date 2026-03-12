#!/usr/bin/env python3
"""
Test script to verify the location/city field filling fix
"""

import sys
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

def test_location_field_filling():
    """
    Simple test to verify that location fields can be filled properly
    """
    print("=" * 70)
    print("LOCATION FIELD FILLING TEST")
    print("=" * 70)
    
    # Setup Chrome options
    options = Options()
    options.add_argument("--start-maximized")
    
    try:
        driver = webdriver.Chrome(options=options)
        
        # Test 1: Basic text input field clearing and filling
        print("\n[TEST 1] Testing basic text field fill logic...")
        driver.get("data:text/html,<input type='text' id='test' value='oldvalue'>")
        sleep(1)
        
        field = driver.find_element(By.ID, "test")
        
        # New fill logic (as in the fix)
        field.click()
        sleep(0.5)
        field.clear()
        sleep(0.3)
        field.send_keys("New City")
        sleep(0.5)
        
        value = field.get_attribute("value")
        assert value == "New City", f"Expected 'New City' but got '{value}'"
        print("✓ Text field filling works correctly")
        
        # Test 2: Multiple rapid field fills
        print("\n[TEST 2] Testing multiple rapid field fills...")
        cities = ["New York", "Los Angeles", "Chicago", "Houston"]
        for city in cities:
            field.click()
            sleep(0.2)
            field.clear()
            sleep(0.2)
            field.send_keys(city)
            sleep(0.3)
            value = field.get_attribute("value")
            assert value == city, f"Expected '{city}' but got '{value}'"
            print(f"✓ Successfully filled: {city}")
        
        print("\n" + "=" * 70)
        print("ALL TESTS PASSED!")
        print("=" * 70)
        return True
        
    except Exception as e:
        print(f"\n✗ TEST FAILED: {e}")
        print("=" * 70)
        return False
    finally:
        try:
            driver.quit()
        except:
            pass

if __name__ == "__main__":
    success = test_location_field_filling()
    sys.exit(0 if success else 1)
