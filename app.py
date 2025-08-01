import streamlit as st
import random

st.set_page_config(page_title="Prompt Generator", page_icon="✍️", layout="centered")

st.title("🧠 Prompt Generator for Content Creators")
st.write("Generate high-quality prompts, hook lines, and hashtags based on your topic.")

topic = st.text_input("🔍 Enter your topic:", "")

prompt_templates = [
    "5 powerful lessons about {} you should know",
    "How to master {} even if you're just starting",
    "What nobody tells you about {}",
    "Why {} could change your life in 2025",
    "I tried {} for 30 days — here's what I learned"
]

hook_templates = [
    "You're not lazy — you're distracted.",
    "This one shift will 10x your {} strategy.",
    "Everyone is talking about {}, but no one is showing this.",
    "The secret behind viral {} content is simpler than you think."
]

hashtag_templates = [
    "#{}Tips #DailyInspo #{}Talks #LearnWithMe #GrowDaily",
    "#CreatorMindset #{}Growth #Motivation #HustleHard #RealContent"
]

if st.button("⚡ Generate Content"):
    if topic.strip() == "":
        st.warning("Please enter a topic to generate prompts.")
    else:
        st.subheader("🎯 Content Prompts")
        for _ in range(3):
            st.write("➤ " + random.choice(prompt_templates).format(topic))

        st.subheader("📢 Hook Lines")
        for _ in range(2):
            st.write("➤ " + random.choice(hook_templates).format(topic))

        st.subheader("📱 Hashtags")
        st.write(random.choice(hashtag_templates).format(topic, topic))