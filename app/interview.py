import os
import json

from dotenv import load_dotenv
from groq import Groq


# ============================================================
# LOAD ENVIRONMENT
# ============================================================

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY is missing from .env")


client = Groq(api_key=api_key)


# ============================================================
# INTERVIEW PROMPT
# ============================================================

INTERVIEW_SYSTEM_PROMPT = """
You are an AI Interview Practice Assistant.

Your job is to conduct a professional mock interview.

The interview has three stages:

1. Ask interview questions.
2. Ask relevant follow-up questions based on the user's answer.
3. At the end, evaluate the user's performance.

Interview questions should be relevant to the selected role
and domain.

Be professional, encouraging, and clear.

Do not make the questions unnecessarily difficult.

During the interview:
- Ask only ONE question at a time.
- Wait for the user's answer.
- Ask a relevant follow-up question when appropriate.
- Do not give the final score until the interview is finished.

At the end, provide:

- Overall score out of 10
- Technical knowledge score
- Communication score
- Problem-solving score
- Strengths
- Areas for improvement
- Short final feedback
"""


# ============================================================
# GENERATE INTERVIEW QUESTION
# ============================================================

def generate_question(role, domain, previous_answer=None):

    if previous_answer:

        prompt = f"""
Role: {role}
Domain: {domain}

The candidate gave this answer:

{previous_answer}

Based on the candidate's answer, ask ONE relevant follow-up
interview question.

Do not evaluate the answer yet.
Only provide the next question.
"""

    else:

        prompt = f"""
Role: {role}
Domain: {domain}

Generate ONE interview question suitable for this role
and domain.

Only provide the interview question.
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "system",
                "content": INTERVIEW_SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content.strip()


# ============================================================
# EVALUATE INTERVIEW
# ============================================================

def evaluate_interview(role, domain, questions_answers):

    interview_text = ""

    for item in questions_answers:

        interview_text += f"""
Question:
{item['question']}

Candidate Answer:
{item['answer']}

"""

    prompt = f"""
Evaluate the following mock interview.

Role: {role}
Domain: {domain}

Interview:

{interview_text}

Provide the evaluation in this format:

Overall Score: X/10

Technical Knowledge: X/10

Communication: X/10

Problem Solving: X/10

Strengths:
- ...

Areas for Improvement:
- ...

Final Feedback:
...
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "system",
                "content": INTERVIEW_SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content.strip()


# ============================================================
# RUN MOCK INTERVIEW
# ============================================================

def run_interview():

    print("\n======================================")
    print("       AI INTERVIEW PRACTICE")
    print("======================================\n")

    role = input("Enter your role: ").strip()
    domain = input("Enter your domain: ").strip()

    print("\nStarting your mock interview...\n")

    questions_answers = []

    question = generate_question(role, domain)

    for i in range(5):

        print(f"\nQuestion {i + 1}:")
        print(question)

        answer = input("\nYour Answer: ").strip()

        if answer.lower() == "exit":
            print("\nInterview ended.")
            return

        questions_answers.append(
            {
                "question": question,
                "answer": answer
            }
        )

        if i < 4:
            question = generate_question(
                role,
                domain,
                previous_answer=answer
            )

    print("\n======================================")
    print("       INTERVIEW EVALUATION")
    print("======================================\n")

    evaluation = evaluate_interview(
        role,
        domain,
        questions_answers
    )

    print(evaluation)


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":
    run_interview()