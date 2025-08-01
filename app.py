import streamlit as st
from io import StringIO

# Page Config
st.set_page_config(page_title="Prompt Generator", page_icon="✨", layout="centered")

# Hide Streamlit default style
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# Custom Title with Gradient
st.markdown("""
<h1 style='text-align: center; font-size: 3em; background: -webkit-linear-gradient(45deg, #ff6ec4, #7873f5); -webkit-background-clip: text; -webkit-text-fill-color: transparent;'>✨ Prompt Generator for Creators</h1>
""", unsafe_allow_html=True)

# Input Box
topic = st.text_input("📌 Enter your topic (e.g. AI, fitness, motivation):")

if topic:
    st.markdown("### 📝 Content Prompts")
    st.success(f"• Future predictions for {topic}")
    st.success(f"• How does {topic} work behind the scenes?")
    st.success(f"• Why is everyone suddenly talking about {topic}?")
    st.success(f"• Common myths about {topic} debunked")
    st.success(f"• What nobody tells you about {topic}")

    st.markdown("### 🔥 Hook Lines")
    st.info(f"• {topic} explained simply and clearly.")
    st.info(f"• Insider scoop: how {topic} actually works.")
    st.info(f"• Revolutionizing the world – one {topic} at a time.")
    st.info(f"• This is why {topic} matters more than ever.")
    st.info(f"• What happens if you ignore {topic}?")

    st.markdown("### 🧠 Hashtags")
    st.code(f"#ContentCreation #{topic.replace(' ', '')}Tips #GrowWith{topic.title()} #ViralPrompts", language="markdown")

    # Generate downloadable text
    output = f"""
📌 PROMPT GENERATOR OUTPUT

Topic: {topic}

📝 Content Prompts:
- Future predictions for {topic}
- How does {topic} work behind the scenes?
- Why is everyone suddenly talking about {topic}?
- Common myths about {topic} debunked
- What nobody tells you about {topic}

🔥 Hook Lines:
- {topic} explained simply and clearly.
- Insider scoop: how {topic} actually works.
- Revolutionizing the world – one {topic} at a time.
- This is why {topic} matters more than ever.
- What happens if you ignore {topic}?

🧠 Hashtags:
#ContentCreation #{topic.replace(' ', '')}Tips #GrowWith{topic.title()} #ViralPrompts
"""

    st.download_button(
        label="📥 Download as .txt",
        data=output,
        file_name="prompts.txt",
        mime="text/plain"
    )

# Footer / Credit
st.markdown("---")
st.markdown("<p style='text-align: center;'>Built with ❤️ by <a href='https://github.com/keshavdev01' target='_blank'>Keshav Sharma</a></p>", unsafe_allow_html=True)