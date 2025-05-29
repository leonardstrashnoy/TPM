import streamlit as st
import random

st.set_page_config(page_title="AI Hiring Ethics Game", layout="centered")

st.title("🤖 AI Hiring Ethics Game")
st.markdown("""
Welcome to the AI Hiring Ethics Game. You're an HR executive at a tech company deploying AI to screen candidates. 
Recent audits show bias in the system. Your decisions will shape the company's future.
""")

# Stage 1: Perception (Superposition)
st.header("Stage 1: Perception")
st.write("Hold multiple perspectives before making a judgment.")

perspectives = {
    "Executives": "Efficiency and cost reduction are top priorities.",
    "Advocacy Groups": "Bias in AI hiring algorithms harms diversity.",
    "Employees": "Fear that AI undermines human judgment in hiring."
}

for role, view in perspectives.items():
    st.checkbox(f"{role}: {view}")

# Stage 2: Information Processing (Entanglement)
st.header("Stage 2: Information Processing")
st.write("Analyze reports and stakeholder feedback. Choices will affect future outcomes.")

bias_metric = 0.23  # Simulated metric: 23% more likely to reject underrepresented candidates
st.metric("Bias Metric", f"{bias_metric*100:.1f}%")

priority = st.selectbox("What do you prioritize?", [
    "Profitability",
    "Diversity and Inclusion",
    "Regulatory Compliance"
])

# Stage 3: Ethical Pathway
st.header("Stage 3: Ethical Reasoning")
pathway = st.radio("Choose an ethical pathway:", [
    "Utilitarianism",
    "Deontology",
    "Ethical Egoism",
    "Virtue Ethics",
    "Relativism",
    "Ethics of Care"
])

# Stage 4: Decision Collapse
st.header("Stage 4: Decision")
decision = st.radio("What is your decision?", [
    "Modify the AI",
    "Keep the AI as is",
    "Use Hybrid Human-AI system"
])

# Stage 5: Probabilistic Outcome
st.header("Outcome")
if st.button("See Outcome"):
    outcomes = {
        "Modify the AI": ["Fairness improved", "Operational delay", "Praise from advocacy groups"],
        "Keep the AI as is": ["Profit boosted", "Public backlash", "Potential lawsuits"],
        "Use Hybrid Human-AI system": ["Balance achieved", "Moderate costs", "Stakeholder support"]
    }
    result = random.sample(outcomes[decision], 2)
    st.success(f"Outcome: {result[0]}, {result[1]}")

# Feedback Loop
st.header("🔁 Feedback Loop")
if st.button("Revisit your Decision"):
    st.experimental_rerun()

# Deployment Notes
st.sidebar.title("Deployment Guide")
st.sidebar.markdown("""
### To Deploy on Streamlit Cloud:
1. Upload this `app.py` to a GitHub repo.
2. Add a `requirements.txt` file with:
```
streamlit
```
3. Go to [streamlit.io/cloud](https://streamlit.io/cloud), connect your GitHub, and deploy.
""")
