import streamlit as st

st.set_page_config(page_title="week09_team03", layout="wide")

st.title("week09_team03")

with st.sidebar:
    st.header("설정")
    name = st.text_input("이름", "")

tab_home, tab_input, tab_result = st.tabs(["홈", "입력", "결과"])

with tab_home:
    st.subheader("홈")
    st.write(f"안녕하세요{', ' + name if name else ''}! 팀 프로젝트 메인 페이지입니다.")

with tab_input:
    st.subheader("입력")
    text = st.text_area("내용을 입력하세요")
    if st.button("저장"):
        st.session_state["text"] = text
        st.success("저장되었습니다.")

with tab_result:
    st.subheader("결과")
    saved = st.session_state.get("text")
    if saved:
        st.write(saved)
    else:
        st.info("입력 탭에서 내용을 저장하면 여기에 표시됩니다.")
