# JobApplier - Setup Instructions

## 🎉 Setup Complete!

Your LinkedIn Auto Job Applier has been successfully configured and is ready to use!

---

## ✅ What Has Been Set Up

### 1. **Configuration Files Created**
- ✅ `config/personals.py` - Your personal information
- ✅ `config/secrets.py` - LinkedIn credentials and AI settings
- ✅ `config/questions.py` - Job application answers (already configured with your info)
- ✅ `config/search.py` - Job search preferences (configured for Java/Backend roles)
- ✅ `config/settings.py` - Bot behavior settings

### 2. **Resume**
- ✅ Your resume copied to `all resumes/default/resume.pdf`

### 3. **Python Environment**
- ✅ Virtual environment created at `venv/`
- ✅ All dependencies installed successfully

### 4. **Git Repository**
- ✅ Git initialized with `main` branch
- ✅ Connected to: https://github.com/ManasMarathe/JobApplier
- ✅ All code pushed to GitHub
- ✅ Author information updated to **Manas Marathe**

### 5. **Job Search Configuration**
Your bot is configured to search for:
- Java Developer
- Backend Engineer
- Software Engineer
- Spring Boot Developer
- Microservices Engineer
- Full Stack Java Developer

**Filters Applied:**
- Location: United States
- Experience Level: Entry level, Associate, Mid-Senior level
- Job Type: Full-time
- Work Mode: Remote, Hybrid
- Easy Apply Only: Yes
- Date Posted: Past week

---

## 🚀 How to Run

### Step 1: Activate Virtual Environment
```bash
cd /Users/manas.marathe/personalProjects/JobApplier
source venv/bin/activate
```

### Step 2: Run the Bot
```bash
python runAiBot.py
```

### Step 3: Run the History UI (Optional)
To view applied jobs in a web interface:
```bash
python app.py
```
Then open your browser to: http://localhost:5000

---

## ⚙️ Important Configuration Details

### Your Current Settings:

**Personal Info** (`config/personals.py`):
- Name: Manas Marathe
- Phone: +1234567890 ⚠️ **UPDATE THIS!**
- Country: United States

**Job Application** (`config/questions.py`):
- Years of Experience: 2
- Visa Sponsorship: No
- Website: https://manas-marathe.vercel.app/
- LinkedIn: https://www.linkedin.com/in/manas-marathe-129942123/
- Citizenship: Non-citizen allowed to work for any employer
- Desired Salary: 2,700,000 (INR?)
- Current CTC: 1,700,000 (INR?)
- Notice Period: 45 days

**LinkedIn Login** (`config/secrets.py`):
- Currently set to use saved browser login
- AI Features: Disabled (set `use_AI = True` if you want AI assistance)

---

## ⚠️ Things You Need to Update

1. **Phone Number**: Update in `config/personals.py` (currently placeholder)
2. **Salary Values**: Verify the salary amounts in `config/questions.py` are correct
3. **LinkedIn Credentials** (Optional): If you want to auto-login:
   - Edit `config/secrets.py`
   - Replace `"keep_this_as_default"` with your actual credentials

---

## 📝 Before First Run

### Required:
1. ✅ Install Google Chrome (latest version)
2. ⚠️ Update your phone number in `config/personals.py`
3. ✅ Make sure you have a LinkedIn account

### Optional:
1. Configure AI features in `config/secrets.py` for better question answering
2. Adjust job search filters in `config/search.py`
3. Update salary expectations if needed

---

## 🎯 How It Works

1. **Opens Chrome** with your profile (or logs in to LinkedIn)
2. **Searches for jobs** based on your configured search terms
3. **Filters jobs** based on your experience and preferences
4. **Applies to jobs** automatically using Easy Apply
5. **Answers questions** using your configured answers
6. **Saves history** in `all excels/all_applied_applications_history.csv`

---

## 🔧 Troubleshooting

### Bot won't start?
```bash
# Make sure virtual environment is activated
source venv/bin/activate

# Try running with stealth mode
# Edit config/settings.py and set: stealth_mode = True
```

### Chrome issues?
- Make sure Chrome is updated to the latest version
- Try setting `safe_mode = True` in `config/settings.py`

### LinkedIn login issues?
- Set your credentials in `config/secrets.py`, OR
- Make sure you're logged into LinkedIn in your default Chrome profile

---

## 📊 Viewing Results

After running the bot, you can check:
- **Applied Jobs**: `all excels/all_applied_applications_history.csv`
- **Failed Applications**: `all excels/all_failed_applications_history.csv`
- **Logs**: `logs/` folder

Or run the web UI:
```bash
python app.py
```

---

## 🔒 Security Notes

- `config/secrets.py` and `config/personals.py` are in `.gitignore`
- **Never commit** these files with real credentials
- Your data stays local on your machine

---

## 📱 Next Steps

1. **Update your phone number** in `config/personals.py`
2. **Review all settings** in the config files
3. **Test with a small run** - set `switch_number = 5` in `config/search.py` to apply to only 5 jobs first
4. **Run the bot**: `python runAiBot.py`
5. **Monitor the process** - the bot will pause before submitting (configurable)

---

## 📚 Additional Resources

- Original Project: https://github.com/ManasMarathe/JobApplier
- Your Repository: https://github.com/ManasMarathe/JobApplier

---

**Good luck with your job search! 🎉**

*Configured by Manas Marathe*
*Last Updated: November 4, 2025*

