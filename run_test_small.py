"""
Test script to verify the apply button fixes with a smaller job set
Run this to test 2-3 job applications instead of 30 per search
"""
import sys
sys.path.insert(0, '.')

# Temporarily modify config for testing
import config.search as search
print("=" * 70)
print("TESTING MODE: Reducing job applications to 3 per search for testing")
print("=" * 70)
original_switch_number = search.switch_number
search.switch_number = 3  # Only try 3 jobs per search

# Only test with 1-2 search terms
original_search_terms = search.search_terms
search.search_terms = search.search_terms[:2]  # Only use first 2 search terms

print(f"\nSearch terms: {search.search_terms}")
print(f"Jobs per search: {search.switch_number}")
print(f"Total test applications: {len(search.search_terms) * search.switch_number} approx\n")

# Now import and run the main bot
from runAiBot import run

print("Starting bot with reduced test parameters...")
print("-" * 70)

try:
    run(1)
except KeyboardInterrupt:
    print("\n\nTest interrupted by user")
except Exception as e:
    print(f"\n\nTest failed with error: {e}")
    import traceback
    traceback.print_exc()

print("\n" + "=" * 70)
print("TEST COMPLETE")
print("=" * 70)
print("\nCheck the logs for:")
print("✓ 'Successfully found Easy Apply modal!'")
print("✓ Job applications recorded in 'all excels/all_applied_applications_history.csv'")
print("✗ Error messages in 'Failed to Easy apply!'")
