import streamlit as st
from io import StringIO

# Title
st.title("🎯 Prompt Generator for Creators")

# User input
topic = st.text_input("📌 Enter your topic (e.g. AI, fitness, motivation, finance):")

# If topic is entered, generate content
if topic:
    st.markdown("### 📝 Content Prompts")
    st.write(f"• Future predictions for {topic}")
    st.write(f"• How does {topic} work behind the scenes?")
    st.write(f"• Why is everyone suddenly talking about {topic}?")
    st.write(f"• Common myths about {topic} debunked")
    st.write(f"• What nobody tells you about {topic}")

    st.markdown("### 🔥 Hook Lines")
    st.write(f"• {topic} explained simply and clearly.")
    st.write(f"• Insider scoop: how {topic} actually works.")
    st.write(f"• Revolutionizing the world – one {topic} at a time.")
    st.write(f"• This is why {topic} matters more than ever.")
    st.write(f"• What happens if you ignore {topic}?")

    st.markdown("### 🧠 Hashtags")
    st.write(f"#ContentCreation #{topic.replace(' ', '')}Tips #GrowWith{topic.title()} #ViralPrompts")

    # Format all content into a downloadable text
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

    # Download button
    st.download_button(
        label="📩 Download Prompts as .txt",
        data=output,
        file_name="prompts.txt",
        mime="text/plain"
    )

# Footer
st.markdown("---")
st.markdown("Made with ❤️ by [Keshav Sharma](https://github.com/keshavdev01)")