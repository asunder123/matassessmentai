import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Define the questions for each maturity level
questions = {
    "Latent": [
        "Is there a lack of dedicated time for discussing RAI during AI development?",
        "Are RAI concerns addressed only after deployment?",
        "Is there a reactive approach to RAI issues?",
        "Is RAI not considered a priority in AI projects?",
        "Is there minimal awareness of RAI within the AI team?"
    ],
    "Emerging": [
        "Is RAI considered at some point during the AI lifecycle?",
        "Are there initial steps towards implementing RAI practices?",
        "Is there a basic understanding of RAI importance among team members?",
        "Are RAI practices implemented inconsistently?",
        "Is RAI training provided to some team members?"
    ],
    "Developing": [
        "Are UX disciplines involved when considering RAI early in the process?",
        "Is there a proactive approach to integrating RAI?",
        "Are RAI best practices being developed?",
        "Is there a structured plan for RAI implementation?",
        "Are RAI considerations part of the regular workflow?"
    ],
    "Realizing": [
        "Is RAI integrated from the start of AI model development?",
        "Does UX work begin before AI model development with RAI in mind?",
        "Are RAI practices well-documented and followed?",
        "Is there a clear alignment between RAI goals and project objectives?",
        "Are RAI metrics actively monitored and used for decision-making?"
    ],
    "Leading": [
        "Is RAI considered during the ideation stages before product development?",
        "Does prior UX work inform the product idea with RAI considerations?",
        "Are predictive RAI measures in place to anticipate issues?",
        "Is RAI embedded in the organization's culture?",
        "Is there continuous improvement and innovation in RAI practices?"
    ]
}

# Initialize scores
scores = {level: [0] * len(questions[level]) for level in questions}

# Streamlit app
def main():
    st.title("AI Maturity Level Assessment")

    # Collect user responses for each maturity level
    for level, qs in questions.items():
        st.subheader(level)
        for i, question in enumerate(qs):
            response = st.radio(f"{question}", ["No", "Yes"], key=f"{level}_{i}")
            scores[level][i] = 1 if response == "Yes" else 0

    # Calculate total score for each level
    total_scores = {level: sum(scores[level]) for level in scores}

    # Display radar chart
    st.header("Maturity Levels Radar Chart")
    st.pyplot(plot_radar_chart(total_scores))

def plot_radar_chart(total_scores):
    labels = list(total_scores.keys())
    data = list(total_scores.values())
    num_vars = len(labels)

    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    angles += angles[:1]  # Repeat the first value to close the circle

    data += data[:1]  # Repeat the first score to close the loop

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    ax.fill(angles, data, color='blue', alpha=0.25)
    ax.plot(angles, data, color='blue', linewidth=2)  # Draw the outline of our data
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)

    return fig

if __name__ == "__main__":
    main()
