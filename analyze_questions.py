'''
Author:     Manas Marathe
LinkedIn:   https://www.linkedin.com/in/manas-marathe-129942123/
Copyright (C) 2024 Manas Marathe
License:    GNU Affero General Public License
GitHub:     https://github.com/ManasMarathe/JobApplier

Question Analysis Script - Run this after the bot to identify and add missing questions
'''

import re
import os
from datetime import datetime

# Color codes for terminal output
class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def analyze_log_file():
    '''
    Analyzes the bot output log to find randomly answered questions
    '''
    log_file = "bot_output.log"
    
    if not os.path.exists(log_file):
        print(f"{Colors.FAIL}❌ Log file '{log_file}' not found!{Colors.ENDC}")
        print(f"{Colors.WARNING}Make sure the bot has run at least once.{Colors.ENDC}")
        return
    
    print(f"\n{Colors.HEADER}{'='*80}")
    print(f"📊 Question Analysis Report")
    print(f"{'='*80}{Colors.ENDC}\n")
    
    with open(log_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the "Questions randomly answered:" section
    pattern = r'Questions randomly answered:\s*\n\s*(.*?)\s*\n\n'
    matches = re.findall(pattern, content, re.DOTALL)
    
    if not matches:
        print(f"{Colors.OKGREEN}✅ Great! No randomly answered questions found.{Colors.ENDC}")
        print(f"{Colors.OKCYAN}All questions were answered using configured rules.{Colors.ENDC}\n")
        return
    
    # Parse the questions
    all_questions = set()
    for match in matches:
        questions = match.split(';')
        for q in questions:
            q = q.strip()
            if q:
                all_questions.add(q)
    
    if not all_questions:
        print(f"{Colors.OKGREEN}✅ No unanswered questions found!{Colors.ENDC}\n")
        return
    
    print(f"{Colors.WARNING}⚠️  Found {len(all_questions)} question(s) that were randomly answered:{Colors.ENDC}\n")
    
    # Categorize questions by type
    text_questions = []
    select_questions = []
    radio_questions = []
    
    for q in all_questions:
        if "'text'" in q:
            text_questions.append(q)
        elif "'select'" in q:
            select_questions.append(q)
        elif "'radio'" in q:
            radio_questions.append(q)
    
    # Display questions
    if text_questions:
        print(f"{Colors.OKBLUE}📝 Text Input Questions:{Colors.ENDC}")
        for i, q in enumerate(text_questions, 1):
            # Extract question text
            q_text = q.split("'")[0].strip().strip("(")
            print(f"   {i}. {q_text}")
        print()
    
    if select_questions:
        print(f"{Colors.OKCYAN}📋 Dropdown/Select Questions:{Colors.ENDC}")
        for i, q in enumerate(select_questions, 1):
            # Extract question text
            q_text = q.split("[")[0].strip().strip("(")
            print(f"   {i}. {q_text}")
        print()
    
    if radio_questions:
        print(f"{Colors.OKGREEN}🔘 Radio Button Questions:{Colors.ENDC}")
        for i, q in enumerate(radio_questions, 1):
            # Extract question text
            q_text = q.split("[")[0].strip().strip("(")
            print(f"   {i}. {q_text}")
        print()
    
    # Generate suggestions
    print(f"\n{Colors.HEADER}{'='*80}")
    print(f"💡 Suggested Actions")
    print(f"{'='*80}{Colors.ENDC}\n")
    
    print(f"{Colors.BOLD}1. Add these questions to config/custom_questions.py:{Colors.ENDC}\n")
    
    if text_questions:
        print(f"{Colors.OKBLUE}   # Add to CUSTOM_TEXT_QUESTIONS:{Colors.ENDC}")
        for q in text_questions:
            q_text = q.split("'")[0].strip().strip("(").lower()
            # Extract a good keyword
            keywords = [w for w in q_text.split() if len(w) > 3 and w not in ['your', 'what', 'when', 'where', 'which', 'this']]
            keyword = keywords[0] if keywords else q_text.split()[0]
            print(f'   "{keyword}": "YOUR_ANSWER_HERE",  # Question: {q_text}')
        print()
    
    if select_questions:
        print(f"{Colors.OKCYAN}   # Add to CUSTOM_SELECT_QUESTIONS:{Colors.ENDC}")
        for q in select_questions:
            q_text = q.split("[")[0].strip().strip("(").lower()
            keywords = [w for w in q_text.split() if len(w) > 3 and w not in ['your', 'what', 'when', 'where', 'which', 'this']]
            keyword = keywords[0] if keywords else q_text.split()[0]
            print(f'   "{keyword}": "YOUR_ANSWER_HERE",  # Question: {q_text}')
        print()
    
    if radio_questions:
        print(f"{Colors.OKGREEN}   # Add to CUSTOM_RADIO_QUESTIONS:{Colors.ENDC}")
        for q in radio_questions:
            q_text = q.split("[")[0].strip().strip("(").lower()
            keywords = [w for w in q_text.split() if len(w) > 3 and w not in ['your', 'what', 'when', 'where', 'which', 'this']]
            keyword = keywords[0] if keywords else q_text.split()[0]
            print(f'   "{keyword}": "YOUR_ANSWER_HERE",  # Question: {q_text}')
        print()
    
    print(f"{Colors.BOLD}2. After adding questions:{Colors.ENDC}")
    print(f"   - Edit {Colors.OKCYAN}config/custom_questions.py{Colors.ENDC}")
    print(f"   - Replace 'YOUR_ANSWER_HERE' with your actual answers")
    print(f"   - Run the bot again: {Colors.OKGREEN}python runAiBot.py{Colors.ENDC}")
    print(f"   - Run this analysis again: {Colors.OKGREEN}python analyze_questions.py{Colors.ENDC}\n")
    
    # Save suggestions to file
    suggestion_file = "logs/question_suggestions.txt"
    os.makedirs("logs", exist_ok=True)
    
    with open(suggestion_file, 'w', encoding='utf-8') as f:
        f.write(f"Question Analysis Report - {datetime.now()}\n")
        f.write("="*80 + "\n\n")
        f.write(f"Found {len(all_questions)} unanswered question(s)\n\n")
        
        if text_questions:
            f.write("TEXT INPUT QUESTIONS:\n")
            for q in text_questions:
                q_text = q.split("'")[0].strip().strip("(")
                f.write(f"- {q_text}\n")
            f.write("\n")
        
        if select_questions:
            f.write("DROPDOWN/SELECT QUESTIONS:\n")
            for q in select_questions:
                q_text = q.split("[")[0].strip().strip("(")
                f.write(f"- {q_text}\n")
            f.write("\n")
        
        if radio_questions:
            f.write("RADIO BUTTON QUESTIONS:\n")
            for q in radio_questions:
                q_text = q.split("[")[0].strip().strip("(")
                f.write(f"- {q_text}\n")
            f.write("\n")
    
    print(f"{Colors.OKGREEN}✅ Report saved to: {suggestion_file}{Colors.ENDC}\n")

def show_stats():
    '''
    Shows statistics from the last run
    '''
    log_file = "bot_output.log"
    
    if not os.path.exists(log_file):
        return
    
    with open(log_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract statistics
    easy_applied = re.search(r'Jobs Easy Applied:\s+(\d+)', content)
    external = re.search(r'External job links collected:\s+(\d+)', content)
    failed = re.search(r'Failed jobs:\s+(\d+)', content)
    skipped = re.search(r'Irrelevant jobs skipped:\s+(\d+)', content)
    
    if any([easy_applied, external, failed, skipped]):
        print(f"{Colors.HEADER}{'='*80}")
        print(f"📈 Last Run Statistics")
        print(f"{'='*80}{Colors.ENDC}\n")
        
        if easy_applied:
            print(f"   ✅ Easy Applied: {Colors.OKGREEN}{easy_applied.group(1)}{Colors.ENDC}")
        if external:
            print(f"   🔗 External Links: {Colors.OKCYAN}{external.group(1)}{Colors.ENDC}")
        if failed:
            print(f"   ❌ Failed: {Colors.FAIL}{failed.group(1)}{Colors.ENDC}")
        if skipped:
            print(f"   ⏭️  Skipped: {Colors.WARNING}{skipped.group(1)}{Colors.ENDC}")
        print()

if __name__ == "__main__":
    print(f"\n{Colors.BOLD}🤖 JobApplier Bot - Question Analyzer{Colors.ENDC}")
    show_stats()
    analyze_log_file()
    
    print(f"{Colors.HEADER}{'='*80}{Colors.ENDC}")
    print(f"{Colors.BOLD}💪 Keep improving with every run!{Colors.ENDC}\n")

