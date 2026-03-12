#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test script to verify the Apply button clicking fix
Focuses on testing the click_apply_button() function and try_xp() improvements
"""

import sys
import os
from time import sleep
from pathlib import Path

# Force UTF-8 encoding for output
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Import the fixed functions
from modules.clickers_and_finders import try_xp, click_apply_button
from modules.helpers import print_lg, buffer, sleep as bot_sleep

def test_try_xp_with_wait():
    """
    Test that try_xp() now waits for clickability instead of immediately finding
    """
    print("\n" + "=" * 70)
    print("TEST 1: try_xp() with Clickability Wait")
    print("=" * 70)
    
    options = Options()
    options.add_argument("--start-maximized")
    
    try:
        driver = webdriver.Chrome(options=options)
        
        # Create a test page with a button that becomes clickable after a delay
        html = """
        <html>
        <body>
            <button id="delayed-button" style="opacity: 0; pointer-events: none;">Click Me</button>
            <script>
                setTimeout(() => {
                    let btn = document.getElementById('delayed-button');
                    btn.style.opacity = '1';
                    btn.style.pointerEvents = 'auto';
                    btn.textContent = 'Ready to Click';
                }, 2000);
            </script>
        </body>
        </html>
        """
        
        driver.get(f"data:text/html,{html}")
        print("✓ Loaded test page with delayed button")
        
        # Test 1a: try_xp with click=False (should find element even if not clickable)
        print("\n[TEST 1a] try_xp with click=False...")
        element = try_xp(driver, ".//button[@id='delayed-button']", click=False, wait_time=1.0)
        assert element != False, "Should have found the element"
        print("✓ try_xp successfully found element before it became clickable")
        
        # Test 1b: try_xp with click=True (should wait for clickability)
        print("\n[TEST 1b] try_xp with click=True (should wait for button to be clickable)...")
        driver.get(f"data:text/html,{html}")
        
        import time
        start = time.time()
        result = try_xp(driver, ".//button[@id='delayed-button']", click=True, wait_time=5.0)
        elapsed = time.time() - start
        
        assert result == True, "Should have clicked the button"
        assert elapsed >= 2.0, f"Should have waited at least 2 seconds, but only waited {elapsed:.1f}s"
        print(f"✓ try_xp successfully clicked button after waiting {elapsed:.1f}s")
        
        # Test 1c: try_xp timeout on non-existent element
        print("\n[TEST 1c] try_xp timeout on non-existent element...")
        import time
        start = time.time()
        result = try_xp(driver, ".//button[@id='nonexistent']", click=True, wait_time=1.0)
        elapsed = time.time() - start
        
        assert result == False, "Should return False for non-existent element"
        assert elapsed >= 0.9, f"Should have waited at least 1 second, but only waited {elapsed:.1f}s"
        print(f"✓ try_xp correctly timed out after {elapsed:.1f}s")
        
        print("\n✅ TEST 1 PASSED: try_xp() correctly waits for clickability\n")
        
        driver.quit()
        return True
        
    except AssertionError as e:
        print(f"\n❌ TEST 1 FAILED: {e}\n")
        try:
            driver.quit()
        except:
            pass
        return False
    except Exception as e:
        print(f"\n❌ TEST 1 ERROR: {e}\n")
        try:
            driver.quit()
        except:
            pass
        return False


def test_click_apply_button_selectors():
    """
    Test that click_apply_button() tries multiple selectors and finds the button
    """
    print("\n" + "=" * 70)
    print("TEST 2: click_apply_button() Multiple Selector Strategies")
    print("=" * 70)
    
    options = Options()
    options.add_argument("--start-maximized")
    
    try:
        driver = webdriver.Chrome(options=options)
        
        # Test 2a: Button with ID selector (primary strategy)
        print("\n[TEST 2a] Testing primary ID selector strategy...")
        html = """
        <html>
        <body>
            <button id="jobs-apply-button-id">Apply</button>
        </body>
        </html>
        """
        driver.get(f"data:text/html,{html}")
        
        click_counter = [0]
        
        # Inject click tracking
        driver.execute_script("""
            let btn = document.getElementById('jobs-apply-button-id');
            btn.addEventListener('click', () => {
                window.clickCounter = (window.clickCounter || 0) + 1;
            });
        """)
        
        result = click_apply_button(driver)
        click_count = driver.execute_script("return window.clickCounter || 0;")
        
        assert result == True, "Should have clicked the button"
        assert click_count == 1, f"Button should have been clicked once, but was clicked {click_count} times"
        print("✓ Successfully clicked button with ID selector")
        
        # Test 2b: Button with legacy selector
        print("\n[TEST 2b] Testing legacy Easy Apply selector strategy...")
        html = """
        <html>
        <body>
            <button class="jobs-apply-button artdeco-button--3" aria-label="Easy Apply">Apply</button>
        </body>
        </html>
        """
        driver.get(f"data:text/html,{html}")
        
        driver.execute_script("""
            let btn = document.querySelector('button[class*="jobs-apply-button"]');
            if (btn) {
                btn.addEventListener('click', () => {
                    window.clickCounter = (window.clickCounter || 0) + 1;
                });
            }
        """)
        
        result = click_apply_button(driver)
        click_count = driver.execute_script("return window.clickCounter || 0;")
        
        assert result == True, "Should have clicked the button"
        assert click_count == 1, f"Button should have been clicked once, but was clicked {click_count} times"
        print("✓ Successfully clicked button with legacy selector")
        
        # Test 2c: Button with fallback selector
        print("\n[TEST 2c] Testing fallback selector strategy...")
        html = """
        <html>
        <body>
            <button class="some-other-class" aria-label="apply">Apply Now</button>
        </body>
        </html>
        """
        driver.get(f"data:text/html,{html}")
        
        driver.execute_script("""
            let btn = document.querySelector('button[aria-label*="apply"]');
            if (btn) {
                btn.addEventListener('click', () => {
                    window.clickCounter = (window.clickCounter || 0) + 1;
                });
            }
        """)
        
        result = click_apply_button(driver)
        click_count = driver.execute_script("return window.clickCounter || 0;")
        
        assert result == True, "Should have clicked the button"
        assert click_count == 1, f"Button should have been clicked once, but was clicked {click_count} times"
        print("✓ Successfully clicked button with fallback selector")
        
        print("\n✅ TEST 2 PASSED: click_apply_button() handles multiple selector strategies\n")
        
        driver.quit()
        return True
        
    except AssertionError as e:
        print(f"\n❌ TEST 2 FAILED: {e}\n")
        try:
            driver.quit()
        except:
            pass
        return False
    except Exception as e:
        print(f"\n❌ TEST 2 ERROR: {e}\n")
        try:
            driver.quit()
        except:
            pass
        return False


def test_visibility_before_click():
    """
    Test that buttons are scrolled into view before clicking
    """
    print("\n" + "=" * 70)
    print("TEST 3: Visibility Check Before Clicking")
    print("=" * 70)
    
    options = Options()
    options.add_argument("--start-maximized")
    
    try:
        driver = webdriver.Chrome(options=options)
        
        html = """
        <html>
        <body>
            <div style="height: 1000px; background: lightgray;">Scroll down to see button</div>
            <button id="jobs-apply-button-id" style="margin-top: 1000px;">Apply</button>
        </body>
        </html>
        """
        driver.get(f"data:text/html,{html}")
        print("✓ Loaded test page with button below viewport")
        
        # Check initial scroll position
        initial_scroll = driver.execute_script("return window.scrollY;")
        print(f"  Initial scroll position: {initial_scroll}")
        
        # Click the button (should scroll it into view first)
        driver.execute_script("""
            let btn = document.getElementById('jobs-apply-button-id');
            btn.addEventListener('click', () => {
                window.clickCounter = (window.clickCounter || 0) + 1;
            });
        """)
        
        result = click_apply_button(driver)
        click_count = driver.execute_script("return window.clickCounter || 0;")
        
        # Check that button was clicked
        assert result == True, "Should have clicked the button"
        assert click_count == 1, f"Button should have been clicked once, but was clicked {click_count} times"
        
        # Check that page scrolled
        final_scroll = driver.execute_script("return window.scrollY;")
        print(f"  Final scroll position: {final_scroll}")
        
        assert final_scroll > initial_scroll, f"Page should have scrolled down, but scroll didn't change"
        print("✓ Page scrolled to bring button into view before clicking")
        
        print("\n✅ TEST 3 PASSED: Buttons are scrolled into view before clicking\n")
        
        driver.quit()
        return True
        
    except AssertionError as e:
        print(f"\n❌ TEST 3 FAILED: {e}\n")
        try:
            driver.quit()
        except:
            pass
        return False
    except Exception as e:
        print(f"\n❌ TEST 3 ERROR: {e}\n")
        try:
            driver.quit()
        except:
            pass
        return False


if __name__ == "__main__":
    print("\n" + "=" * 70)
    print("APPLY BUTTON FIX TEST SUITE")
    print("=" * 70)
    
    all_passed = True
    
    # Run tests
    all_passed &= test_try_xp_with_wait()
    all_passed &= test_click_apply_button_selectors()
    all_passed &= test_visibility_before_click()
    
    # Summary
    print("\n" + "=" * 70)
    if all_passed:
        print("✅ ALL TESTS PASSED!")
        print("=" * 70)
        sys.exit(0)
    else:
        print("❌ SOME TESTS FAILED")
        print("=" * 70)
        sys.exit(1)
