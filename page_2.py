import streamlit as st

if "messages" not in st.session_state :
    st.session_state.messages = []

st.title("우리 회사 챗봇")

prompt = st.chat_input("무엇이든 물어보세요")
if prompt:
    st.session_state.messages.append({"role" : "user", "content" : prompt})
    st.session_state.messages.append({"role" : "ai", "content" : "만나서 반갑습니다."})

for message in st.session_state.messages :
    with st.chat_message(message['role']) :
        st.write(message['content'])