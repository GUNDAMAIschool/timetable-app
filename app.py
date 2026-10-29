import streamlit as st

st.set_page_config(page_title="時間割作成アプリ", page_icon="🕒")

st.title("🕒 時間割自動作成アプリ（テスト版）")
st.write("Streamlit Cloud上での動作確認テスト画面です。")

st.sidebar.header("設定項目")
teacher_count = st.sidebar.number_input("教員数", min_value=1, max_value=20, value=3)

if st.button("時間割を作成する"):
    st.success(f"ボタンが押されました！現在の設定教員数: {teacher_count}名")
    st.info("ここに今後、OR-ToolsとGemini AIの組み合わせ処理が入ります。")
