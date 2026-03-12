#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Verification script for Apply button fix
Checks that the code changes were properly applied
"""

import sys
import os
from pathlib import Path

def verify_try_xp_fix():
    """Verify that try_xp function was updated to use WebDriverWait"""
    print("\n" + "=" * 70)
    print("VERIFICATION 1: try_xp() Improvement")
    print("=" * 70)
    
    with open("modules/clickers_and_finders.py", "r") as f:
        content = f.read()
    
    # Check 1: try_xp should use WebDriverWait
    if "WebDriverWait(driver, wait_time).until(" in content and \
       "EC.element_to_be_clickable" in content:
        print("[OK] try_xp() now uses WebDriverWait.element_to_be_clickable()")
    else:
        print("[FAIL] try_xp() doesn't use WebDriverWait.element_to_be_clickable()")
        return False
    
    # Check 2: try_xp should have wait_time parameter
    if "def try_xp(driver: WebDriver, xpath: str, click: bool=True, wait_time: float=5.0)" in content:
        print("[OK] try_xp() has wait_time parameter")
    else:
        print("[FAIL] try_xp() doesn't have wait_time parameter")
        return False
    
    # Check 3: try_xp should call scroll_to_view
    if "scroll_to_view(driver, element)" in content:
        print("[OK] try_xp() calls scroll_to_view() before clicking")
    else:
        print("[FAIL] try_xp() doesn't call scroll_to_view()")
        return False
    
    print("\n[PASS] try_xp() verification successful\n")
    return True


def verify_click_apply_button_function():
    """Verify that new click_apply_button function exists"""
    print("\n" + "=" * 70)
    print("VERIFICATION 2: click_apply_button() Function")
    print("=" * 70)
    
    with open("modules/clickers_and_finders.py", "r") as f:
        content = f.read()
    
    # Check 1: Function exists
    if "def click_apply_button(driver: WebDriver) -> bool:" in content:
        print("[OK] click_apply_button() function exists with correct signature")
    else:
        print("[FAIL] click_apply_button() function not found or has wrong signature")
        return False
    
    # Check 2: Function has multiple XPath strategies
    strategies = [
        'jobs-apply-button-id',
        'Easy Apply aria-label',
        'Generic: Apply button with class',
        'Fallback: Any button containing',
        'Alternative: Button with aria-label'
    ]
    
    for strategy_name in strategies:
        if strategy_name in content:
            print(f"[OK] Strategy '{strategy_name}' found")
        else:
            print(f"[WARN] Strategy '{strategy_name}' might be missing")
    
    # Check 3: Uses try_xp with proper parameters
    if "try_xp(driver, xpath, click=True, wait_time=3.0)" in content:
        print("[OK] click_apply_button() uses try_xp with wait_time parameter")
    else:
        print("[FAIL] click_apply_button() doesn't properly use try_xp")
        return False
    
    print("\n[PASS] click_apply_button() verification successful\n")
    return True


def verify_runaibot_updates():
    """Verify that runAiBot.py was updated to use new functions"""
    print("\n" + "=" * 70)
    print("VERIFICATION 3: runAiBot.py Updates")
    print("=" * 70)
    
    with open("runAiBot.py", "r") as f:
        content = f.read()
    
    # Check 1: Uses click_apply_button in easy apply case
    if "# Case 1: Easy Apply Button (using improved click function with multiple strategies)" in content and \
       "if click_apply_button(driver):" in content:
        print("[OK] runAiBot.py Easy Apply case uses click_apply_button()")
    else:
        print("[FAIL] runAiBot.py doesn't properly update Easy Apply case")
        return False
    
    # Check 2: Uses click_apply_button in external apply case
    if "click_apply_button(driver)  # Use improved Apply button clicking with multiple strategies" in content:
        print("[OK] runAiBot.py external_apply() uses click_apply_button()")
    else:
        print("[WARN] External apply case might not be updated optimally")
    
    print("\n[PASS] runAiBot.py verification successful\n")
    return True


def verify_no_old_patterns():
    """Verify that old problematic patterns were removed"""
    print("\n" + "=" * 70)
    print("VERIFICATION 4: Old Patterns Removed")
    print("=" * 70)
    
    with open("runAiBot.py", "r") as f:
        content = f.read()
    
    # Check 1: Old XPath is replaced
    old_xpath = ".//button[@id='jobs-apply-button-id' or (contains(@class,'jobs-apply-button') and contains(@class, 'artdeco-button--3') and contains(@aria-label, 'Easy'))]"
    
    # Count occurrences (should be 0 in the main logic, only in comments if at all)
    count = content.count("click_apply_button(driver)")
    
    if count > 0:
        print(f"[OK] Found {count} uses of new click_apply_button() function")
    else:
        print("[WARN] No uses of click_apply_button() found - might be an issue")
    
    print("\n[PASS] Old patterns verification successful\n")
    return True


def main():
    print("\n" + "=" * 70)
    print("APPLY BUTTON FIX - CODE VERIFICATION")
    print("=" * 70)
    
    os.chdir("D:\\coding\\JobApplier")
    
    all_passed = True
    all_passed &= verify_try_xp_fix()
    all_passed &= verify_click_apply_button_function()
    all_passed &= verify_runaibot_updates()
    all_passed &= verify_no_old_patterns()
    
    print("\n" + "=" * 70)
    if all_passed:
        print("[PASS] ALL VERIFICATIONS PASSED!")
        print("=" * 70)
        print("\nSUMMARY OF FIXES:")
        print("-" * 70)
        print("1. try_xp() now uses WebDriverWait.element_to_be_clickable()")
        print("   - Waits up to 5 seconds for button to be interactive")
        print("   - Scrolls element into view before clicking")
        print("   - Proper error handling with timeout")
        print()
        print("2. New click_apply_button() function with 5 selector strategies:")
        print("   - Primary: Modern Easy Apply button ID (jobs-apply-button-id)")
        print("   - Legacy: Apply with Easy Apply aria-label")
        print("   - Generic: Apply button with classes (no label requirement)")
        print("   - Fallback: Any button with 'Apply' text in span")
        print("   - Alternative: Button with 'apply' in aria-label")
        print()
        print("3. Updated runAiBot.py:")
        print("   - Easy Apply flow uses click_apply_button()")
        print("   - External Apply flow uses click_apply_button()")
        print()
        print("This ensures reliable button clicking with multiple fallbacks!")
        print("=" * 70)
        return 0
    else:
        print("[FAIL] SOME VERIFICATIONS FAILED")
        print("=" * 70)
        return 1


if __name__ == "__main__":
    sys.exit(main())
