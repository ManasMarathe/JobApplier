# LinkedIn AI Auto Job Applier

A Selenium-based bot that automates LinkedIn Easy Apply job applications. It searches for jobs matching your criteria, auto-answers application questions, selects your resume, and submits — capable of applying to 100+ jobs in under an hour.

---

## Setup

### Prerequisites
- Python 3.10+
- Google Chrome (latest)

### Install

```bash
git clone https://github.com/ManasMarathe/JobApplier.git
cd JobApplier
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Configure

All config files live in the `config/` folder:

| File | What to set |
|------|-------------|
| `personals.py` | Name, phone, address |
| `questions.py` | Pre-filled answers for common questions, resume path, pause settings |
| `search.py` | Search terms, location, filters, experience level, jobs-per-run limit |
| `secrets.py` | LinkedIn credentials (optional), AI provider and API key |
| `settings.py` | Stealth mode, safe mode, click intervals, headless mode |
| `custom_questions.py` | Your own keyword → answer pairs, grows with each run |

Place your resume at `all resumes/default/resume.pdf`.

---

## Running

```bash
source venv/bin/activate

# Run the bot
python runAiBot.py

# Run with auto-improvement (applies, then analyzes unanswered questions)
python run_and_improve.py

# Analyze what questions the bot couldn't answer
python analyze_questions.py

# View applied jobs history in browser (http://localhost:5000)
python app.py
```

---

## Features

- Auto login (via saved browser profile or configured credentials)
- Keyword-based job search with filters: location, experience level, date posted, remote/hybrid, salary
- Skips blacklisted companies and jobs with unwanted keywords
- Skips jobs above your configured experience level
- Answers text, textarea, radio, select, checkbox, and address type questions
- Uploads your default resume
- Optional pause before submission for review
- Saves full application history to `all excels/all_applied_applications_history.csv`
- Logs failed applications separately for debugging
- Runs through multiple filter/sort combinations in each cycle
- Headless / background mode
- Stealth mode via undetected-chromedriver
- Randomized click intervals to mimic human behavior
- Web UI to browse applied jobs and external application links

### AI Features (optional)

Enable by setting `use_AI = True` in `config/secrets.py`. Supports **Gemini** and **DeepSeek**:
- Extracts required skills from job descriptions
- Answers unknown application questions using your profile context

---

## Auto-Improvement Cycle

The bot gets smarter over time:

1. Run `python run_and_improve.py`
2. Bot applies to jobs and logs any questions it couldn't answer
3. Run `python analyze_questions.py` to see what to add
4. Add entries to `config/custom_questions.py`
5. Repeat — each run covers more questions automatically

---

## Output Files

| Path | Contents |
|------|----------|
| `all excels/all_applied_applications_history.csv` | All successfully applied jobs |
| `all excels/all_failed_applications_history.csv` | Applications that failed |
| `logs/` | Per-run log files |
| `bot_output.log` | Latest run stdout |

---

## Disclaimer

This program is for personal/educational use only. Use it in compliance with LinkedIn's Terms of Service. The author bears no responsibility for misuse, account restrictions, or any consequences arising from use of this tool.

---

## Contact

- **LinkedIn**: https://www.linkedin.com/in/manas-marathe-129942123/
- **Portfolio**: https://manas-marathe.vercel.app/
