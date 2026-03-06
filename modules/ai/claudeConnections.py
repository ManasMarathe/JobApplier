'''
Author:     Manas Marathe
LinkedIn:   https://www.linkedin.com/in/manas-marathe-129942123/
Copyright (C) 2024 Manas Marathe
License:    GNU Affero General Public License
GitHub:     https://github.com/ManasMarathe/JobApplier
version:    24.12.29.12.30
'''

from config.secrets import llm_api_key, llm_model
from modules.helpers import print_lg, critical_error_log
from modules.ai.prompts import ai_answer_prompt
from typing import Literal

import anthropic


def claude_create_client() -> anthropic.Anthropic | None:
    '''
    Create and return an Anthropic Claude client.
    * Returns an `anthropic.Anthropic` client, or None on failure
    '''
    try:
        print_lg("Creating Anthropic Claude client...")
        client = anthropic.Anthropic(api_key=llm_api_key)
        print_lg("---- SUCCESSFULLY CREATED CLAUDE CLIENT! ----")
        print_lg(f"Using Model: {llm_model}")
        print_lg("---------------------------------------------")
        return client
    except Exception as e:
        critical_error_log("Error occurred while creating Claude client.", e)
        return None


def claude_answer_question(
    client: anthropic.Anthropic,
    question: str,
    options: list[str] | None = None,
    question_type: Literal['text', 'textarea', 'single_select', 'multiple_select'] = 'text',
    job_description: str = None,
    about_company: str = None,
    user_information_all: str = None,
) -> str | None:
    '''
    Answer a form question using the Anthropic Claude API.
    * Takes in `client` of type `anthropic.Anthropic`
    * Takes in `question` of type `str` - The question to answer
    * Takes in `options` of type `list[str] | None` - Options for select questions
    * Takes in `question_type` of type `str` - One of "text", "textarea", "single_select", "multiple_select"
    * Takes in `job_description` of type `str | None` - Job description for context
    * Takes in `about_company` of type `str | None` - Company info for context
    * Takes in `user_information_all` of type `str | None` - Resume/user info for context
    * Returns answer string, or None on failure
    '''
    print_lg("-- ANSWERING QUESTION using Claude")
    try:
        prompt = ai_answer_prompt.format(user_information_all or "N/A", question)
        if options:
            prompt += f"\nChoose from these options only: {options}"
        if job_description and job_description != "Unknown":
            prompt += f"\nJob Description:\n{job_description}"
        if about_company and about_company != "Unknown":
            prompt += f"\nAbout the Company:\n{about_company}"

        response = client.messages.create(
            model=llm_model,
            max_tokens=512,
            messages=[{"role": "user", "content": prompt}]
        )
        result = response.content[0].text.strip()
        print_lg(f"Claude answered: {result}")
        return result
    except Exception as e:
        print_lg(f"Claude answer failed: {e}")
        return None
