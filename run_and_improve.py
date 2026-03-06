#!/usr/bin/env python3
'''
Author:     Manas Marathe
LinkedIn:   https://www.linkedin.com/in/manas-marathe-129942123/
Copyright (C) 2024 Manas Marathe
License:    GNU Affero General Public License
GitHub:     https://github.com/ManasMarathe/JobApplier

Auto-Improvement Wrapper - Runs bot and analyzes results automatically
'''

import subprocess
import sys
import os

def run_bot():
    '''Run the main job application bot'''
    print("\n" + "="*80)
    print("🤖 Starting LinkedIn Job Applier Bot...")
    print("="*80 + "\n")
    
    try:
        # Run the bot
        result = subprocess.run([sys.executable, "runAiBot.py"], 
                              capture_output=False, 
                              text=True)
        return result.returncode == 0
    except KeyboardInterrupt:
        print("\n\n⚠️  Bot stopped by user.")
        return False
    except Exception as e:
        print(f"\n❌ Error running bot: {e}")
        return False

def analyze_questions():
    '''Analyze questions after bot run'''
    print("\n" + "="*80)
    print("📊 Analyzing Questions...")
    print("="*80 + "\n")
    
    try:
        subprocess.run([sys.executable, "analyze_questions.py"])
    except Exception as e:
        print(f"\n❌ Error analyzing questions: {e}")

def show_menu():
    '''Show improvement menu'''
    print("\n" + "="*80)
    print("🎯 What would you like to do next?")
    print("="*80)
    print("\n1. Run bot again (to test improvements)")
    print("2. Edit custom questions (config/custom_questions.py)")
    print("3. View question suggestions (logs/question_suggestions.txt)")
    print("4. Exit")
    
    while True:
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == "1":
            return "run_again"
        elif choice == "2":
            return "edit"
        elif choice == "3":
            return "view"
        elif choice == "4":
            return "exit"
        else:
            print("Invalid choice. Please enter 1-4.")

def main():
    '''Main execution flow'''
    print("""
    ╔═══════════════════════════════════════════════════════════════╗
    ║                                                               ║
    ║         🤖 LinkedIn Job Applier - Auto-Improvement Mode       ║
    ║                                                               ║
    ║   This script will:                                          ║
    ║   1. Run the job application bot                             ║
    ║   2. Analyze unanswered questions                            ║
    ║   3. Suggest improvements                                    ║
    ║   4. Help you add new questions                              ║
    ║                                                               ║
    ╚═══════════════════════════════════════════════════════════════╝
    """)
    
    input("Press Enter to start...")
    
    # Run the bot
    success = run_bot()
    
    # Always analyze, even if bot had issues
    analyze_questions()
    
    # Show menu for next steps
    while True:
        action = show_menu()
        
        if action == "run_again":
            print("\n🔄 Restarting bot...\n")
            success = run_bot()
            analyze_questions()
        
        elif action == "edit":
            config_file = "config/custom_questions.py"
            print(f"\n📝 Opening {config_file}...")
            print("Add your question-answer pairs, save, and run the bot again.\n")
            
            # Try to open in default editor
            if sys.platform == "darwin":  # macOS
                os.system(f"open {config_file}")
            elif sys.platform == "linux":
                os.system(f"xdg-open {config_file}")
            elif sys.platform == "win32":
                os.system(f"start {config_file}")
            else:
                print(f"Please manually edit: {config_file}")
        
        elif action == "view":
            suggestion_file = "logs/question_suggestions.txt"
            if os.path.exists(suggestion_file):
                print(f"\n📄 Opening {suggestion_file}...\n")
                with open(suggestion_file, 'r', encoding='utf-8') as f:
                    print(f.read())
            else:
                print(f"\n⚠️  No suggestions file found at {suggestion_file}")
                print("Run the bot first to generate suggestions.\n")
        
        elif action == "exit":
            print("\n👋 Thank you for using JobApplier Bot!")
            print("💪 Keep improving with every run!\n")
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye!")
        sys.exit(0)

