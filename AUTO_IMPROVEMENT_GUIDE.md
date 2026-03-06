# 🚀 Auto-Improvement System Guide

## Overview

Your JobApplier bot now has a **self-improvement system** that learns from each run and gets better over time! 

### What's New?

1. **Custom Questions File** - Easy-to-edit question mappings
2. **Question Analyzer** - Identifies unanswered questions automatically
3. **Auto-Improvement Mode** - Complete workflow from run → analyze → improve
4. **Smart Question Matching** - Checks custom questions before default logic

---

## 📁 New Files

### 1. `config/custom_questions.py`
Your personalized question-answer mappings. The bot checks this file **first** before using default logic.

**Contains:**
- `CUSTOM_TEXT_QUESTIONS` - For text input fields
- `CUSTOM_SELECT_QUESTIONS` - For dropdown menus
- `CUSTOM_RADIO_QUESTIONS` - For radio buttons
- `CUSTOM_TEXTAREA_QUESTIONS` - For long-form answers (cover letters, etc.)

### 2. `analyze_questions.py`
Analyzes bot logs to find questions that were randomly answered.

**Features:**
- Categorizes questions by type (text, select, radio)
- Suggests exact code to add to `custom_questions.py`
- Saves report to `logs/question_suggestions.txt`

### 3. `run_and_improve.py`
Complete auto-improvement workflow script.

**Workflow:**
1. Runs the bot
2. Automatically analyzes questions
3. Shows interactive menu for improvements
4. Lets you edit questions and re-run

---

## 🎯 How to Use

### Method 1: Quick Run (Same as Before)
```bash
cd /Users/manas.marathe/personalProjects/JobApplier
source venv/bin/activate
python runAiBot.py
```

### Method 2: Auto-Improvement Mode (Recommended!)
```bash
cd /Users/manas.marathe/personalProjects/JobApplier
source venv/bin/activate
python run_and_improve.py
```

This will:
- ✅ Run the bot
- ✅ Analyze results automatically
- ✅ Show you exactly what questions to add
- ✅ Give you options to edit and re-run

### Method 3: Manual Analysis (After a Run)
```bash
python analyze_questions.py
```

---

## 📝 Adding Custom Questions

### Step 1: Run the Bot
```bash
python runAiBot.py
```

### Step 2: Check for Unanswered Questions
```bash
python analyze_questions.py
```

You'll see output like:
```
📊 Question Analysis Report
====================================

⚠️  Found 3 question(s) that were randomly answered:

📝 Text Input Questions:
   1. How many years of Python experience?
   
📋 Dropdown/Select Questions:
   1. What is your highest degree?

💡 Suggested Actions
====================================

1. Add to CUSTOM_TEXT_QUESTIONS:
   "python": "1",  # Question: how many years of python experience?

2. Add to CUSTOM_SELECT_QUESTIONS:
   "degree": "Bachelor",  # Question: what is your highest degree?
```

### Step 3: Edit `config/custom_questions.py`

Open the file and add your answers:

```python
CUSTOM_TEXT_QUESTIONS = {
    # ... existing questions ...
    
    # New questions (add at the bottom)
    "python": "1",
    "python experience": "1 year",
}

CUSTOM_SELECT_QUESTIONS = {
    # ... existing questions ...
    
    # New questions
    "degree": "Bachelor of Engineering",
    "highest degree": "Bachelor",
}
```

### Step 4: Run Again!
```bash
python runAiBot.py
```

The bot will now use your custom answers! 🎉

---

## 💡 Pro Tips

### 1. Use Keywords
The bot matches questions using **keywords**. Use the most specific part of the question:

✅ Good:
```python
"python experience": "2 years"
"javascript experience": "1 year"
```

❌ Too Generic:
```python
"experience": "2 years"  # Will match ANY experience question!
```

### 2. Check What the Bot Found
Your custom answers are logged:
```
Found custom answer for "How many years of Python experience?" using keyword "python experience"
```

### 3. Handle Variations
Add multiple entries for similar questions:
```python
CUSTOM_TEXT_QUESTIONS = {
    "notice period": "45",
    "notice": "45 days",
    "when can you start": "Within 45 days",
    "availability": "45 days",
}
```

### 4. Use AI for Complex Questions
Some questions are too complex for simple mapping. Add them to `AI_PREFERRED_QUESTIONS`:
```python
AI_PREFERRED_QUESTIONS = [
    "describe a time when",
    "tell me about your biggest challenge",
    # Add more here
]
```

Then enable AI in `config/secrets.py`:
```python
use_AI = True
ai_provider = "gemini"  # or "openai" or "deepseek"
```

---

## 📊 Understanding the Analysis Report

### Statistics Section
```
📈 Last Run Statistics
====================================
   ✅ Easy Applied: 5
   🔗 External Links: 2
   ❌ Failed: 1
   ⏭️  Skipped: 3
```

### Question Types

**Text Input** - Simple one-line answers
```
Examples: phone number, years of experience, salary
```

**Select/Dropdown** - Choose from a list
```
Examples: gender, degree level, country
```

**Radio Button** - Choose one option
```
Examples: citizenship status, veteran status
```

**Textarea** - Long-form answers
```
Examples: cover letter, tell us about yourself
```

---

## 🔄 Continuous Improvement Cycle

```
┌─────────────────────────────────────────────┐
│ 1. Run Bot (python runAiBot.py)           │
└──────────────┬──────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────┐
│ 2. Bot encounters unknown questions        │
│    → Answers randomly (logs them)          │
└──────────────┬──────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────┐
│ 3. Analyze (python analyze_questions.py)   │
│    → Identifies questions                   │
│    → Suggests code to add                   │
└──────────────┬──────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────┐
│ 4. Edit config/custom_questions.py         │
│    → Add question-answer pairs              │
└──────────────┬──────────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────────┐
│ 5. Run Bot Again                           │
│    → Bot uses new answers                   │
│    → Success rate improves! 📈              │
└──────────────┬──────────────────────────────┘
               │
               └─────────────────► Repeat!
```

---

## 🐛 Troubleshooting

### Bot Still Randomly Answering Known Questions

**Check 1:** Is the keyword specific enough?
```python
# Too generic - matches everything
"experience": "2"

# Better - specific
"java experience": "2"
```

**Check 2:** Is the question in the right section?
- Text inputs → `CUSTOM_TEXT_QUESTIONS`
- Dropdowns → `CUSTOM_SELECT_QUESTIONS`
- Radio buttons → `CUSTOM_RADIO_QUESTIONS`

**Check 3:** Check the logs for the exact question text:
```bash
grep "randomly answered" bot_output.log
```

### Custom Questions Not Loading

**Solution:** Check for syntax errors
```bash
python -c "from config.custom_questions import *"
```

If you see errors, fix the syntax in `config/custom_questions.py`

### Analysis Shows No Questions

**This is good!** It means all questions were answered correctly. 🎉

---

## 📈 Tracking Your Progress

After several runs, you should see:
- ✅ Fewer randomly answered questions
- ✅ Higher success rate
- ✅ More applications completed
- ✅ Fewer failed applications

Keep the improvement cycle going! 💪

---

## 🎓 Examples

### Example 1: Adding Experience Questions

**Bot Log Shows:**
```
Questions randomly answered:
  ('How many years of Python experience?', 'text')
```

**Add to custom_questions.py:**
```python
CUSTOM_TEXT_QUESTIONS = {
    # ... existing ...
    "python experience": "2",
}
```

### Example 2: Adding Dropdown Questions

**Bot Log Shows:**
```
Questions randomly answered:
  ('Preferred work location [ "Remote", "Hybrid", "On-site" ]', 'select')
```

**Add to custom_questions.py:**
```python
CUSTOM_SELECT_QUESTIONS = {
    # ... existing ...
    "preferred work location": "Remote",
    "work location preference": "Remote",
}
```

### Example 3: Complex Cover Letter

**Bot Log Shows:**
```
Questions randomly answered:
  ('Why do you want to work at our company?', 'textarea')
```

**Add to custom_questions.py:**
```python
CUSTOM_TEXTAREA_QUESTIONS = {
    # ... existing ...
    "why do you want to work": """I am excited about this opportunity because 
    it aligns with my career goals and technical expertise. I am particularly 
    drawn to your company's innovative approach and commitment to excellence.""",
}
```

---

## 🎯 Goals

**Short-term (First 3 runs):**
- Add 5-10 common questions
- Reduce random answers by 50%

**Medium-term (After 10 runs):**
- Have answers for 90% of questions
- Minimal manual intervention needed

**Long-term:**
- Fully automated application process
- High success rate
- Bot handles almost all questions

---

## 📞 Need Help?

If you encounter questions that are:
- Too complex for simple mappings
- Job-specific
- Require contextual understanding

Consider:
1. Enabling AI assistance (`use_AI = True`)
2. Using `pause_at_failed_question = True` for manual review
3. Adding specific industry/role questions to custom mappings

---

**Remember:** Every run makes your bot smarter! 🧠

Keep the improvement cycle going and you'll have a fully optimized job application bot in no time! 🚀

