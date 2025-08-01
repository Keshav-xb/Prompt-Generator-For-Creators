import streamlit as st
from streamlit_option_menu import option_menu
import random

# --- Page Config ---
st.set_page_config(page_title="Prompt Generator for Creators", layout="wide")

# --- Sidebar Navigation ---
with st.sidebar:
    selected = option_menu(
        menu_title="🌐 Navigation",
        options=["Prompt Generator", "About", "Features", "Use Cases", "GitHub"],
        icons=["pen", "info-circle", "gear", "lightbulb", "github"],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "5px", "background-color": "#111"},
            "icon": {"color": "#ffffff", "font-size": "20px"},
            "nav-link": {
                "color": "#eee",
                "font-size": "16px",
                "text-align": "left",
                "margin": "2px",
            },
            "nav-link-selected": {"background-color": "#4c8bf5"},
        },
    )

# --- Prompt Generator Logic ---
def generate_prompt(topic, style):
    prompts = [
        f"Write a compelling Instagram caption about '{topic}' in a {style} tone.",
        f"Create a unique YouTube video idea centered around '{topic}'.",
        f"Write a motivational quote involving '{topic}' in a {style} voice.",
        f"Generate a tweet about '{topic}' using a {style} style and emojis.",
        f"Create a creative blog post title about '{topic}' in a {style} format.",
    ]
    return random.choice(prompts)

# --- Page Routing ---
if selected == "Prompt Generator":
    st.title("🧠 Prompt Generator for Creators")
    st.subheader("Unleash your creativity with AI-generated content prompts!")

    topic = st.text_input("Enter your topic or niche (e.g., travel, fitness, tech):")
    style = st.selectbox("Choose a tone/style:", ["Creative", "Professional", "Casual", "Motivational", "Funny"])

    if st.button("🎯 Generate Prompt"):
        if topic:
            prompt = generate_prompt(topic, style)
            st.success("Here's your AI-generated prompt:")
            st.markdown(f"**👉 {prompt}**")
        else:
            st.warning("Please enter a topic before generating.")

elif selected == "About":
    st.title("📄 About")
    st.markdown("""
    **Prompt Generator for Creators** is a simple yet powerful tool built using Python and Streamlit, designed to help content creators generate unique prompts for social media, blogs, videos, and more.  
    This project was crafted by **Keshav Sharma**, a passionate AI builder and developer from India.  
    """)

elif selected == "Features":
    st.title("⚙️ Features")
    st.markdown("""
    - ✨ One-click prompt generation  
    - 💬 Style and tone customization  
    - 🧠 AI-generated creativity booster  
    - 📄 Exportable prompt output (coming soon)  
    - 🚀 Mobile-friendly & super fast  
    """)

elif selected == "Use Cases":
    st.title("🧠 Use Cases")
    st.markdown("""
    - Content creation for Instagram, YouTube, LinkedIn  
    - Caption ideas for reels, shorts, and blog intros  
    - Email subject line inspiration  
    - Product tagline generation  
    - Motivational quotes and tweet crafting  
    """)

elif selected == "GitHub":
    st.title("🔗 GitHub")
    st.markdown("[👉 Visit My GitHub Repo](https://github.com/Keshav-xb)", unsafe_allow_html=True)

# --- Footer ---
st.markdown("""
<hr style="border: none; border-top: 1px solid #555;" />

<div style="text-align: center; font-size: 14px; color: #999;">
    <p><strong>Prompt Generator for Creators</strong> – Built with ❤️ by Keshav Sharma</p>
    <p>© 2025 Keshav-xb · 
    <a href="https://github.com/Keshav-xb" target="_blank">GitHub</a> · 
    <a href="mailto:keshavxkh@gmail.com" target="_blank">Email</a> · 
    <a href="https://www.linkedin.com/in/keshav-sharma-b15270257" target="_blank">LinkedIn</a></p>
</div>
""", unsafe_allow_html=True)