# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Activate virtual environment (required before running anything)
source venv/bin/activate

# Run the bot
python runAiBot.py

# Run with auto-improvement cycle (run -> analyze -> suggest fixes)
python run_and_improve.py

# Analyze unanswered questions from last run
python analyze_questions.py

# Run the applied jobs history web UI (http://localhost:5000)
python app.py

# Test Gemini AI integration
python test_gemini.py
```

## Architecture

This is a fork of [Auto_job_applier_linkedIn](https://github.com/GodsScion/Auto_job_applier_linkedIn) configured for Manas Marathe. It uses Selenium/undetected-chromedriver to automate LinkedIn Easy Apply job applications.

### Entry Points
- `runAiBot.py` — main bot runner; drives the LinkedIn automation loop
- `run_and_improve.py` — wrapper that runs the bot then calls `analyze_questions.py` to surface unanswered questions
- `app.py` — Flask web UI that reads/updates `all excels/all_applied_applications_history.csv`

### Configuration (`config/`)
All user-specific configuration lives here. These files are in `.gitignore` and must never be committed with real credentials.
- `secrets.py` — LinkedIn credentials, AI provider selection (`llm_api`, `use_AI`, `llm_api_key`, `llm_model`, `llm_api_url`)
- `personals.py` — name, phone, address, etc.
- `questions.py` — pre-configured answers for common application questions; `default_resume_path`; `pause_before_submit`
- `search.py` — search terms, location, filters, `switch_number` (max jobs per run), `current_experience`
- `settings.py` — `stealth_mode`, `safe_mode`, `showAiErrorAlerts`, click intervals
- `custom_questions.py` — user-maintained dict of question keyword → answer, grows over time as the bot encounters new questions

### Modules (`modules/`)
- `helpers.py` — `print_lg`, `critical_error_log`, `convert_to_json` utilities used everywhere
- `open_chrome.py` — launches Chrome/undetected-chromedriver
- `clickers_and_finders.py` — Selenium helpers for finding and interacting with page elements
- `validator.py` — validates all config variables on startup
- `resumes/` — resume handling logic
- `ai/geminiConnections.py` — Gemini API client (`gemini_create_client`, `gemini_completion`, `gemini_extract_skills`, `gemini_answer_question`)
- `ai/deepseekConnections.py` — DeepSeek client via OpenAI-compatible API (same interface pattern)
- `ai/prompts.py` — prompt templates shared across AI providers (`extract_skills_prompt`, `ai_answer_prompt`, `deepseek_extract_skills_prompt`)

### AI Integration
AI is opt-in via `use_AI = True` in `config/secrets.py`. Both Gemini and DeepSeek providers share the same prompt templates from `modules/ai/prompts.py`. The AI is used to extract skills from job descriptions and answer unknown application questions.

### Output Files
- `all excels/all_applied_applications_history.csv` — every applied job
- `all excels/all_failed_applications_history.csv` — failed applications
- `logs/` — run logs
- `bot_output.log` — stdout log from last run

## Code Conventions

- Functions: lowercase snake_case, docstring in `''' ... '''` immediately after `def`, typed parameters and return types
- Local variables: camelCase; global/config variables: snake_case
- Contributions wrapped in `##> ------ Name : contact - Type ------` / `##<` attestation blocks
- Config variables must have inline comments explaining valid values and be validated in `modules/validator.py`
