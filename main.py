# from dotenv import load_dotenv

# load_dotenv()
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI

import streamlit as st

# Chat Model 초기화
chat_model = ChatOpenAI(model="gpt-4", temperature=1.07, max_tokens=1024)

system_message = "지금은 2023년이고 너는 미래 2033년에 살고있어. 인터넷 신문사 '지피터스 타임즈' 3년차 기자 '구라임'이야. 자극적이고 재미있는 기사를 많이 써. 가끔 비난도 해. "


st.title("AI 예언가 🔮")
st.write("당신의 10년 뒤 모습을 알려드립니다.")

# 사용자 입력 받기
name = st.text_input("이름")
age = st.text_input("현재 나이")
MBTI = st.text_input("MBTI")
sex = st.text_input("성별")
field = st.text_input("전공이나 관심사")
dream = st.text_input("미래의 나에게 꼭 바라는 것")

if st.button("🪄 미래 알아보기"):
    with st.spinner("주문을 외우는 중 ... 60~100초"):
        # 예측 요청
        human_message = f"다음 나의 정보를 이용해서 니가 살고있는 2033년에서 나에 대한 자극적인 기사를 500자 이내로 작성해줘. 실제 신문기사처럼. \n- 이름: {name}\n- 현재 나이: {age}\n- MBTI: {MBTI}\n- 성별: {sex}\n- 전공이나 관심사: {field}\n- 미래의 나에게 꼭 바라는것: {dream}"

        response = chat_model.predict(system_message + human_message)

        # 응답 출력
        st.write(response)
