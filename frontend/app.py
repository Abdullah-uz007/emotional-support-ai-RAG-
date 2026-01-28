st.markdown("---")
st.caption("Built by Abdullah Khan • RAG-powered Emotional AI")


import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/chat"

st.set_page_config(
    page_title="Emotional Support AI",
    page_icon="🧠",
    layout="centered"
)

st.title("🧠 Emotional Support AI")
st.caption("RAG-powered • Emotion-aware • Privacy-focused")

user_input = st.text_area(
    "How are you feeling today?",
    placeholder="I feel anxious and overwhelmed..."
)

if st.button("Talk to AI"):
    if user_input.strip():
        with st.spinner("Thinking..."):
            try:
                res = requests.post(API_URL, json={"message": user_input}) #####3#####

                if res.status_code != 200:
                    st.error("Backend error. Check FastAPI logs.")
                else:
                    try:
                        data = res.json()
                        st.markdown(f"### Detected Emotion: **{data['emotion']}**")
                        st.markdown("---")
                        st.write(data["response"])
                    except Exception:
                        st.error("Backend did not return valid JSON.")
                        st.code(res.text)

            except Exception as e:
                st.error("Could not connect to backend.")
                st.code(str(e))

    else:
        st.warning("Please write something first.")
