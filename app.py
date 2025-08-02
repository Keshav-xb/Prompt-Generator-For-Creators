import streamlit as st
from streamlit_option_menu import option_menu
import random

# --- Page Config ---
st.set_page_config(page_title="Prompt Generator for Creators", layout="wide")

# --- Sidebar Navigation ---
with st.sidebar:
    selected = option_menu(
        menu_title="🌐 Navigation",
        options=["Prompt Generator", "About", "Features", "Contact"],
        icons=["pen", "info-circle", "stars", "envelope"],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "10px", "background-color": "#0E1117"},
            "icon": {"color": "#ffffff", "font-size": "20px"},
            "nav-link": {
                "color": "#ffffff",
                "font-size": "16px",
                "text-align": "left",
                "margin": "5px 0",
                "--hover-color": "#1f77b4",
            },
            "nav-link-selected": {
                "background-color": "#1f77b4",
                "color": "white",
                "font-weight": "bold",
            },
        }
    )

# --- Prompt Generator Logic ---
def generate_prompt(topic, style):
    prompts = [
        f"Write a compelling Instagram caption about {topic}.",
        f"Create a unique YouTube video idea on {topic}.",
        f"Write a motivational quote involving {topic} in {style}.",
        f"Generate a tweet about '{topic}' using {style}.",
        f"Create a creative blog post title about {topic}.",
    ]
    return random.choice(prompts)

# --- Main Content Area ---
st.title("✨ AI Prompt Generator for Creators")

if selected == "Prompt Generator":
    topic = st.text_input("Enter your topic:")
    style = st.selectbox("Choose a style:", ["Casual", "Professional", "Funny", "Motivational"])

    if st.button("Generate Prompt"):
        if topic:
            prompt = generate_prompt(topic, style)
            st.success(prompt)
        else:
            st.warning("Please enter a topic first.")

elif selected == "About":
    st.subheader("About This App")
    st.write("This AI Prompt Generator helps content creators come up with new, high-quality ideas instantly.")

elif selected == "Features":
    st.subheader("Features")
    st.markdown("""
    - 🎯 Instant AI prompts for Instagram, YouTube, Twitter, and blogs  
    - 🧠 Smart content tailored to your style  
    - 💼 Ideal for creators, marketers, and entrepreneurs
    """)

elif selected == "Contact":
    st.subheader("Contact")
    st.markdown("""
    - 📧 Email: [keshavxkh@gmail.com](mailto:keshavxkh@gmail.com)  
    - 💼 LinkedIn: [Keshav Sharma](https://www.linkedin.com/in/keshav-sharma-b15270257)  
    - 💻 GitHub: [github.com/Keshav-xb](https://github.com/Keshav-xb)
    """)

# --- Footer ---
st.markdown(
    """
    <hr style="margin-top: 50px;">
    <div style='text-align: center; font-size: 14px;'>
        Made with ❤️ by <b>Keshav Sharma</b><br>
        <a href='mailto:keshavxkh@gmail.com'>📧 Email</a> |
        <a href='https://www.linkedin.com/in/keshav-sharma-b15270257'>💼 LinkedIn</a> |
        <a href='https://github.com/Keshav-xb'>💻 GitHub</a>
    </div>
    """,
    unsafe_allow_html=True
)
