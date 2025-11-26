# Vocalis: The Sentiment-Tracking Chatbot

Hey Liaplus.ai , I'am vikrant Singh  This is my project for the sentiment analysis assignment—I named the chatbot Vocalis. The goal was to build a chatbot that not only chats but also figures out how the user is feeling throughout the conversation.

I focused on making the code super clean by separating the core logic from the user interface (GUI).

## Assignment Goals Check-Off
Tier 1 : Fully Complete,The project successfully calculates the Overall Conversation Sentiment for the entire chat history.

Tier 2 : Fully Complete,The project performs Statement-Level Analysis for each message,This analysis is presented in a detailed, structured report.

The code is professionally separated into two distinct files: sentiment_engine.py (Logic) and vocalis_gui.py (GUI).

This separation makes the code clean, modular, and easy to maintain.

##  How to Run Vocalis

It’s a Python project, super easy to run just type in terminal **python vocalis_gui.py**

### Prerequisites

You'll need these installed:
1.  **Python 3.x**
2.  **NLTK** (The Natural Language Toolkit)
3.  **ttkthemes** (For the clean iOS-like GUI style)

### Step-by-Step Instructions

1.  **Install Libraries:**
    bash
    pip install nltk ttkthemes
    
2.  **Get the Files:** Make sure both `sentiment_engine.py` and `vocalis_gui.py` are in the same folder.
3.  **Run the Chatbot:** You only need to run the GUI file!
    bash
    python vocalis_gui.py
    
4.  **Chat & Analyze!** Type your messages and click **"Analyze & Report"** to see the full emotional breakdown in a separate window.

## My Sentiment Logic Explained

I used a powerful hybrid model to make sure the sentiment analysis is both accurate and responsive to critical feedback.

### Tech Used

* **Algorithm:** **VADER** (from NLTK). It's designed to understand conversational text, like slang and emoticons!

### The Two-Part Analysis

1.  **The Overrider (Custom Keywords):** My code first checks for a strong list of negative phrases (like "not satisfied," "worst"). If the user types any of these, it immediately flags the message as **Negative**, overriding the VADER score.
2.  **The Core (VADER Score):** Otherwise, it uses VADER's `compound` score: scores above `0.05` are **Positive**, below `-0.05` are **Negative**, and everything in between is **Neutral**.

##  Bonus Features & Highlights

* **Professional Structure:** Logic in `sentiment_engine.py` and GUI in `vocalis_gui.py`. This means I can change the GUI without breaking the analysis engine!
* **iOS-Inspired GUI:** I used the `ttkthemes` library to give the interface a clean, flat, modern look, similar to a macOS/iOS application.
* **Mood Tracker:** The final report includes a function that tracks the sequence of moods and tells you if the user's emotion **improved** or **deteriorated** during the chat!

I hope you like it! Let me know if you have any feedback.
