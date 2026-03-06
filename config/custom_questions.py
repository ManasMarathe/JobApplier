'''
Author:     Manas Marathe
LinkedIn:   https://www.linkedin.com/in/manas-marathe-129942123/
Copyright (C) 2024 Manas Marathe
License:    GNU Affero General Public License
GitHub:     https://github.com/ManasMarathe/JobApplier
version:    24.12.29.12.30

Custom Question Mappings - Add your own question-answer pairs here
This file is loaded after the default question handlers, so you can override or add new patterns.
'''

# Text Input Questions Mapping
# Format: "keyword or phrase in question": "your answer"
CUSTOM_TEXT_QUESTIONS = {
    # Email variations
    "email": "manasvmarathe@gmail.com",
    "e-mail": "manasvmarathe@gmail.com",
    "email address": "manasvmarathe@gmail.com",
    "contact email": "manasvmarathe@gmail.com",
    
    # Phone number variations
    "phone": "9869031752",
    "mobile": "9869031752",
    "mobile number": "9869031752",
    "contact number": "9869031752",
    "telephone": "9869031752",
    
    # Work authorization
    "work authorization": "Yes",
    "authorized to work": "Yes",
    "legally authorized": "Yes",
    "right to work": "Yes",
    
    # Availability
    "notice period": "45",
    "availability": "45 days",
    "start date": "Within 45 days",
    "when can you start": "Within 45 days",
    "earliest start": "Within 45 days",
    
    # Salary expectations (in INR)
    "expected salary": "2900000",
    "salary expectation": "2900000",
    "desired compensation": "2900000",
    "expected ctc": "2900000",
    
    # Current salary
    "current salary": "1900000",
    "current ctc": "1900000",
    "present salary": "1900000",
    
    # Professional links
    "linkedin profile": "https://www.linkedin.com/in/manas-marathe-129942123/",
    "linkedin url": "https://www.linkedin.com/in/manas-marathe-129942123/",
    "portfolio": "https://manas-marathe.vercel.app/",
    "portfolio website": "https://manas-marathe.vercel.app/",
    "github": "https://github.com/ManasMarathe",
    "github profile": "https://github.com/ManasMarathe",
    
    # Education
    "university": "K.J Somai",  # TODO: Update with your actual university
    "degree": "Bachelor of Engineering",    # TODO: Update with your actual degree
    "graduation year": "2021",             # TODO: Update with your actual year
    
    # Referral
    "referral": "No",
    "referred by": "No",
    "employee referral": "No",
    
    # Additional custom questions - Add yours below:
    # "your question keyword": "your answer",
}

# Select Dropdown Questions Mapping
# Format: "keyword in question": "option to select"
CUSTOM_SELECT_QUESTIONS = {
    "email address": "manasmarathe1@gmail.com",  # LinkedIn still shows old email in dropdown
    "email": "manasmarathe1@gmail.com",  # Will select whichever is available
    "gender": "Male",
    "race": "Decline",
    "ethnicity": "Decline",
    "veteran status": "Decline",
    "disability": "Decline",
    "highest degree": "Bachelor",
    "education level": "Bachelor",
    
    # Work authorization dropdowns
    "work authorization": "Yes",
    "visa sponsorship": "No",
    "require sponsorship": "No",
    
    # Proficiency levels
    "english proficiency": "Professional",
    "java proficiency": "Expert",
    "spring boot proficiency": "Expert",
    
    # Add your custom select questions below:
    # "question keyword": "option to select",
}

# Radio Button Questions Mapping
# Format: "keyword in question": "option to select"
CUSTOM_RADIO_QUESTIONS = {
    "citizenship": "Non-citizen allowed to work for any employer",
    "work eligibility": "Non-citizen allowed to work for any employer",
    "veteran": "Decline",
    "disability": "Decline",
    "sponsorship": "No",
    
    # Add your custom radio questions below:
    # "question keyword": "option to select",
}

# Textarea Questions Mapping (for longer answers)
# Format: "keyword in question": "your detailed answer"
CUSTOM_TEXTAREA_QUESTIONS = {
    "cover letter": """Dear Hiring Manager,

I am writing to express my interest in this position. With 2+ years of experience in Java development, 
Spring Boot, and Microservices architecture, I am confident in my ability to contribute effectively to your team.

My experience includes designing and implementing scalable backend systems, working with RESTful APIs, 
and collaborating with cross-functional teams to deliver high-quality software solutions.

I am excited about the opportunity to bring my technical skills and passion for software development to your organization.

Thank you for considering my application.

Best regards,
Manas Marathe""",
    
    "why do you want to work here": """I am excited about this opportunity because it aligns perfectly with my career goals 
and technical expertise. I am particularly drawn to your company's innovative approach and commitment to excellence. 
I believe my skills in Java, Spring Boot, and Microservices would allow me to make meaningful contributions to your team.""",
    
    "tell us about yourself": """I am a Software Engineer with 2+ years of experience specializing in Java backend development. 
I have hands-on expertise in Spring Boot, Microservices architecture, and building scalable RESTful APIs. 
I am passionate about writing clean, efficient code and continuously learning new technologies.""",
    
    # Add your custom textarea questions below:
    # "question keyword": "your detailed answer",
}

# Question keywords that should trigger AI assistance
# These are complex questions that are better handled by AI
AI_PREFERRED_QUESTIONS = [
    "describe a time when",
    "tell me about a project",
    "biggest challenge",
    "how would you handle",
    "what would you do if",
    "technical problem",
    "conflict with",
    "leadership experience",
    "greatest strength",
    "greatest weakness",
]

# Add notes for questions you want to remember
QUESTION_NOTES = """
=== QUESTIONS TO ADD AFTER NEXT RUN ===

Instructions:
1. After each bot run, check the logs for "randomly answered questions"
2. Add those questions here with the correct answers
3. Test the bot again to verify

Example:
- Question: "How many years of Python experience?"
- Add to CUSTOM_TEXT_QUESTIONS: "python experience": "1"

=== PENDING QUESTIONS ===
(Add questions from logs here after each run)

"""
