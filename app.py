import streamlit as st
from crew import create_crew



st.set_page_config(
    page_title="Origins Evaluator for your Idea",
    page_icon="🚀",
    layout="wide"
)

# Custom CSS styling
st.markdown("""
<style>
    .header { text-align: center; padding: 20px; background-color: #2E86C1; color: white; }
    .column { padding: 20px; border-radius: 10px; margin: 10px; background-color: #F8F9F9; }
    .agent-title { color: #2E86C1; font-weight: bold; }
    .separator { border-top: 2px solid #2E86C1; margin: 15px 0; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="header"><h1>🔍 Code Future Analyst</h1></div>', unsafe_allow_html=True)

user_query = st.text_area("Enter your code/idea:")
if st.button("Analyze") and user_query:
    with st.spinner("Processing..."):
        results = create_crew(user_query)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("🔐 Code Authenticity")
        st.markdown(results["code_analyst"])
    
    with col2:
        st.subheader("📈 Future Trends")
        st.markdown(results["trend_analyst"])
    
    with col3:
        st.subheader("🛠 Implementation Plan")
        st.markdown(results["implementation"])