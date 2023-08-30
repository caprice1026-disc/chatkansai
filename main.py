import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.schema import (SystemMessage, HumanMessage, AIMessage)


def main():
    llm = ChatOpenAI(temperature=0)

    st.set_page_config(
        page_title="ChatGPT的な何か",
        page_icon="🤗"
    )
    st.header("ChatGPT的な何か")

    # チャット履歴の初期化
    if "messages" not in st.session_state:
        st.session_state.messages = [
            SystemMessage(content="関西弁でしゃべってください。")
        ]

    # ユーザーの入力を監視
    container = st.container()
    with container:
        with st.form(key="my_form"):
            user_input = st.text_input("聞きたいことを入力してや！")
            submit_button = st.form_submit_button(label="送信")
            if submit_button:
                st.session_state.messages.append(HumanMessage(content=user_input))
                with st.spinner("考えてるで..."):
                        response = llm(st.session_state.messages)
                st.session_state.messages.append(AIMessage(content=response.content))
                user_input = ""

    # チャット履歴の表示
    messages = st.session_state.get('messages', [])
    for message in messages:
        if isinstance(message, AIMessage):
            with st.chat_message('assistant'):
                st.markdown(message.content)
        elif isinstance(message, HumanMessage):
            with st.chat_message('user'):
                st.markdown(message.content)
        else:  # isinstance(message, SystemMessage):
            st.write(f"System message: {message.content}")


if __name__ == '__main__':
    main()