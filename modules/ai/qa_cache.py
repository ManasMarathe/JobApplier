'''
Author:     Manas Marathe
LinkedIn:   https://www.linkedin.com/in/manas-marathe-129942123/
Copyright (C) 2024 Manas Marathe
License:    GNU Affero General Public License
GitHub:     https://github.com/ManasMarathe/JobApplier
version:    24.12.29.12.30
'''

import json
import os

from modules.helpers import print_lg

QA_CACHE_PATH = "all excels/ai_qa_cache.json"


def _normalize(question: str) -> str:
    '''Normalize a question string for consistent cache key lookup.'''
    return question.lower().strip()


def load_cache() -> dict:
    '''Load the QA cache from disk. Returns empty dict if file doesn't exist or is corrupt.'''
    if not os.path.exists(QA_CACHE_PATH):
        return {}
    try:
        with open(QA_CACHE_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print_lg(f'Failed to load QA cache: {e}')
        return {}


def lookup_cache(question: str, question_type: str) -> str | None:
    '''
    Look up a question in the QA cache.
    * Takes in `question` of type `str` - The question label
    * Takes in `question_type` of type `str` - The question type
    * Returns cached answer string, or None if not found
    '''
    cache = load_cache()
    key = _normalize(question)
    entry = cache.get(key)
    if entry and entry.get("question_type") == question_type:
        count = entry.get("count", 1)
        print_lg(f'QA Cache hit ({count}x) for "{question}": "{entry["answer"]}"')
        return entry["answer"]
    return None


def save_to_cache(question: str, question_type: str, answer: str) -> None:
    '''
    Save an AI-answered question to the QA cache.
    * Takes in `question` of type `str` - The question label
    * Takes in `question_type` of type `str` - The question type
    * Takes in `answer` of type `str` - The answer to cache
    '''
    cache = load_cache()
    key = _normalize(question)
    if key in cache:
        cache[key]["count"] = cache[key].get("count", 1) + 1
        cache[key]["answer"] = answer  # Update with latest answer
    else:
        cache[key] = {
            "answer": answer,
            "question_type": question_type,
            "original_question": question,
            "count": 1
        }
    try:
        os.makedirs(os.path.dirname(QA_CACHE_PATH), exist_ok=True)
        with open(QA_CACHE_PATH, 'w', encoding='utf-8') as f:
            json.dump(cache, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print_lg(f'Failed to save to QA cache: {e}')
