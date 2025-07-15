from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# 允许所有来源跨域（方便本地测试和 GPT 插件调用）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AnswerRequest(BaseModel):
    user_answer: str

class AnswerResponse(BaseModel):
    correct: bool
    message: str

@app.post("/check_answer", response_model=AnswerResponse)
def check_answer(data: AnswerRequest):
    correct_answer = "Tableware"
    if data.user_answer.strip().lower() == correct_answer.lower():
        return AnswerResponse(correct=True, message="✅ 正确！Tableware 是“餐具”的意思。")
    else:
        return AnswerResponse(correct=False, message="❌ 不正确。正确答案是 Tableware。")
