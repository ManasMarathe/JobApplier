# ⚡ Quick Start Guide - Auto-Improving JobApplier Bot

## 🚀 Three Ways to Run

### 1️⃣ Auto-Improvement Mode (Recommended for Learning)
```bash
cd /Users/manas.marathe/personalProjects/JobApplier
source venv/bin/activate
python run_and_improve.py
```
✨ **Best for:** First-time setup, adding new questions, continuous improvement

---

### 2️⃣ Standard Mode (For Regular Use)
```bash
cd /Users/manas.marathe/personalProjects/JobApplier
source venv/bin/activate
python runAiBot.py
```
✨ **Best for:** After you've configured most questions, regular job hunting

---

### 3️⃣ Analysis Only (After a Run)
```bash
python analyze_questions.py
```
✨ **Best for:** Checking what questions need to be added

---

## 📝 After Each Run

### 1. Check for New Questions
```bash
python analyze_questions.py
```

### 2. Add Answers to Custom Questions
Edit `config/custom_questions.py`:
```python
CUSTOM_TEXT_QUESTIONS = {
    "question keyword": "your answer",
}
```

### 3. Run Again!
The bot gets smarter each time! 🧠

---

## 🎯 Key Files

| File | Purpose | When to Edit |
|------|---------|-------------|
| `config/custom_questions.py` | Your question-answer mappings | After each run |
| `config/personals.py` | Your personal info (name, phone, etc.) | Initial setup |
| `config/search.py` | Job search preferences | When changing search criteria |
| `config/questions.py` | General application settings | Rarely |
| `logs/question_suggestions.txt` | Auto-generated suggestions | Read-only (reference) |

---

## 🔄 Improvement Cycle

```
Run Bot → Analyze Questions → Add to Custom File → Run Again → Improve!
```

**Goal:** Each run should have fewer "randomly answered" questions!

---

## ⚙️ Important Settings

### In `config/search.py`:
```python
switch_number = 30           # Number of jobs to apply per search term
pause_after_filters = False  # Set False for auto-run
search_location = "India"    # Your job search location
current_experience = 2       # Your years of experience
```

### In `config/questions.py`:
```python
pause_before_submit = True         # Verify before submitting
pause_at_failed_question = False   # Auto-skip unknown questions
overwrite_previous_answers = False # Keep filled answers
```

---

## 🐛 Quick Fixes

### Issue: Bot stops after few jobs
**Fix:** Set `pause_after_filters = False` in `config/search.py`

### Issue: Questions still randomly answered
**Fix:** Add more specific keywords in `config/custom_questions.py`

### Issue: Browser crash
**Fix:** 
1. Update Chrome to latest version
2. Set `safe_mode = True` in `config/settings.py`
3. Close extra Chrome windows (keep under 10 tabs)

---

## 📊 Measuring Success

After each run, check:
- ✅ **Easy Applied** count (higher is better)
- ⚠️ **Randomly Answered** questions (lower is better)  
- ❌ **Failed** applications (lower is better)

**Target:** 90%+ success rate with custom questions configured!

---

## 💡 Pro Tips

1. **Start with 5-10 job applications** (`switch_number = 5`) to test
2. **Run analysis after EVERY bot run** to catch new questions
3. **Use specific keywords** in custom questions (not generic terms)
4. **Keep improving** - your bot learns from each run!

---

## 📚 Full Documentation

- **Auto-Improvement Guide:** `AUTO_IMPROVEMENT_GUIDE.md`
- **Setup Instructions:** `SETUP_INSTRUCTIONS.md`
- **Original README:** `README.md`

---

## 🎉 First Time Running?

### Step 1: Update your info
```bash
# Edit these files:
config/personals.py      # Add your email, phone, address
config/search.py         # Set job preferences
```

### Step 2: Run in auto-improvement mode
```bash
python run_and_improve.py
```

### Step 3: Follow the prompts
The script will guide you through the process!

---

## 🆘 Need Help?

**Check logs:**
```bash
cat bot_output.log | grep "randomly answered"
cat logs/question_suggestions.txt
```

**Verify config:**
```bash
python -c "from config.custom_questions import *"
```

---

**Remember:** Each run makes your bot smarter! 🚀

Happy job hunting! 💼

