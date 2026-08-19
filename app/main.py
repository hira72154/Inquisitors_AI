from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from app.chatbot import ask_chatbot
from app.interview import generate_question, evaluate_interview


# ============================================================
# FASTAPI APP
# ============================================================

app = FastAPI(
    title="Inquisitors Society AI",
    description="AI Chatbot and Interview Practice API",
    version="1.0.0"
)


# ============================================================
# CORS
# ============================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://hira72154.github.io",
        "http://127.0.0.1:3000",
        "http://localhost:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ============================================================
# REQUEST MODELS
# ============================================================

class ChatRequest(BaseModel):
    message: str


class InterviewQuestionRequest(BaseModel):
    role: str
    domain: str
    previous_answer: str | None = None


class InterviewEvaluationRequest(BaseModel):
    role: str
    domain: str
    questions_answers: list


# ============================================================
# HOME
# ============================================================

@app.get("/")
def home():
    return {
        "message": "Inquisitors Society AI is running!",
        "features": [
            "Chatbot",
            "Interview Practice"
        ]
    }


# ============================================================
# HEALTH CHECK
# ============================================================

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "Inquisitors Society AI"
    }


# ============================================================
# CHATBOT
# ============================================================

@app.post("/chat")
def chat(request: ChatRequest):

    answer = ask_chatbot(request.message)

    return {
        "message": request.message,
        "response": answer
    }


# ============================================================
# INTERVIEW QUESTION
# ============================================================

@app.post("/interview/question")
def interview_question(request: InterviewQuestionRequest):

    question = generate_question(
        role=request.role,
        domain=request.domain,
        previous_answer=request.previous_answer
    )

    return {
        "role": request.role,
        "domain": request.domain,
        "question": question
    }


# ============================================================
# INTERVIEW EVALUATION
# ============================================================

@app.post("/interview/evaluate")
def interview_evaluate(request: InterviewEvaluationRequest):

    evaluation = evaluate_interview(
        role=request.role,
        domain=request.domain,
        questions_answers=request.questions_answers
    )

    # --------------------------------------------------------
    # If evaluate_interview() returns a dictionary,
    # return its fields directly so the frontend can read:
    #
    # data.overall_score
    # data.technical_score
    # data.communication_score
    # data.problem_solving_score
    # data.final_feedback
    # --------------------------------------------------------

    if isinstance(evaluation, dict):

        return evaluation

    # --------------------------------------------------------
    # Fallback if evaluation is returned as plain text
    # --------------------------------------------------------

    return {
        "overall_score": 0,
        "technical_score": 0,
        "communication_score": 0,
        "problem_solving_score": 0,
        "strengths": [],
        "areas_for_improvement": [],
        "final_feedback": str(evaluation)
    }