#!/usr/bin/env python3
"""
Verification script to confirm the apply button fixes are present in the code
"""

import re

def verify_fixes():
    """Check if all the required fixes are present in runAiBot.py"""
    
    print("="*70)
    print("VERIFYING APPLY BUTTON FIXES IN runAiBot.py")
    print("="*70)
    
    with open("runAiBot.py", "r", encoding="utf-8") as f:
        content = f.read()
    
    fixes_found = {
        "Modal wait buffer (buffer(2))": False,
        "Modal retry logic (for attempt in range(3))": False,
        "Successfully found Easy Apply modal message": False,
        "Attempt N to find modal failed message": False,
        "StaleElementReferenceException handling": False,
        "Next button existence check before click": False,
        "Improved error handling": False
    }
    
    # Check for buffer(2) after click
    if re.search(r'buffer\(2\)\s*#.*modal.*time.*appear', content, re.IGNORECASE):
        fixes_found["Modal wait buffer (buffer(2))"] = True
    
    # Check for retry logic
    if re.search(r'for\s+attempt\s+in\s+range\(3\)', content):
        fixes_found["Modal retry logic (for attempt in range(3))"] = True
    
    # Check for success message
    if 'Successfully found Easy Apply modal!' in content:
        fixes_found["Successfully found Easy Apply modal message"] = True
    
    # Check for attempt failure message
    if re.search(r'Attempt\s+.*attempt.*to find modal failed', content):
        fixes_found["Attempt N to find modal failed message"] = True
    
    # Check for stale element handling
    if 'StaleElementReferenceException' in content:
        fixes_found["StaleElementReferenceException handling"] = True
    
    # Check for next button existence check
    if re.search(r'next_button\s*=\s*None.*if\s+next_button:', content, re.DOTALL):
        fixes_found["Next button existence check before click"] = True
    
    # Check for improved error handling
    if re.search(r'Failed to Easy apply.*Error details', content):
        fixes_found["Improved error handling"] = True
    
    print("\nFIX VERIFICATION RESULTS:\n")
    all_passed = True
    for fix_name, found in fixes_found.items():
        status = "[FOUND]" if found else "[MISSING]"
        print(f"  {status} {fix_name}")
        if not found:
            all_passed = False
    
    print("\n" + "="*70)
    if all_passed:
        print("[SUCCESS] ALL FIXES VERIFIED SUCCESSFULLY!")
        print("="*70)
        print("\nFix Summary:")
        print("1. Modal detection now waits 2 seconds after button click")
        print("2. Retry logic attempts to find modal up to 3 times")
        print("3. Success messages logged when modal is found")
        print("4. Stale element exceptions are properly handled")
        print("5. Next button existence is checked before clicking")
        print("6. Improved error messages for debugging")
        print("\nThe apply button fixes are ready for testing!")
    else:
        print("[FAILED] SOME FIXES ARE MISSING")
        print("="*70)
        print("Please check the fixes have been properly applied.")
    
    print("\n" + "="*70)
    return all_passed

if __name__ == "__main__":
    verify_fixes()
