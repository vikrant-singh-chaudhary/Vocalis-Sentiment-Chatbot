import tkinter as tk
from tkinter import scrolledtext, ttk
from ttkthemes import ThemedTk 

from sentiment_engine import (
    get_sentiment_label,
    analyze_overall_sentiment,
    summarize_sentiment_trend
)

class VocalisChatbotGUI:
    def __init__(self, master):
        self.master = master
        master.set_theme("clam") 
    
        master.title("Vocalis: The Sentiment Chatbot")
        master.geometry("700x550")
        master.resizable(True, True) 
            
        self.user_messages = [] 
        self.full_exchange = [] 
        self.sentiment_labels = []

        style = ttk.Style()
        style.configure("Chat.TFrame", background="#F5F5F7") 
        
        chat_frame = ttk.Frame(master, padding="10", style="Chat.TFrame")
        chat_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        self.chat_display = scrolledtext.ScrolledText(chat_frame, wrap=tk.WORD,  width=80, height=20,  font=("Helvetica Neue", 10), bg="white", relief=tk.FLAT, padx=10, pady=10)
        self.chat_display.pack(fill=tk.BOTH, expand=True)
        self.chat_display.config(state=tk.DISABLED) 

        input_frame = ttk.Frame(master, padding="5 10 5 5")
        input_frame.pack(pady=0, padx=10, fill=tk.X)

        self.msg_input = ttk.Entry(input_frame, font=("Helvetica Neue", 10))
        self.msg_input.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
        self.msg_input.bind("<Return>", lambda event: self.send_message()) 
     
        send_button = ttk.Button(input_frame, text="Send", command=self.send_message)
        send_button.pack(side=tk.LEFT)
        
        analyze_button = ttk.Button(input_frame, text="Analyze & Report", command=self.show_analysis, style='Accent.TButton')
        analyze_button.pack(side=tk.LEFT, padx=5)
        
        self.display_message("Vocalis", "Hello! I'm Vocalis, ready to chat and analyze your mood.", "Chatbot")

    def display_message(self, speaker, message, tag):
        """Adds a message to the chat display with a custom tag/color."""
        self.chat_display.config(state=tk.NORMAL)
        
        if tag == "User":
            prefix = "You: "
            color = "#1D74F2"
        elif tag == "Chatbot":
            prefix = "Vocalis: "
            color = "#4CAF50" 
        else:
            prefix = ""
            color = "black"

        self.chat_display.insert(tk.END, prefix + message + "\n")
        self.chat_display.tag_config(tag, foreground=color)
        start = self.chat_display.index("end-1c linestart")
        end = self.chat_display.index("end-1c linestart + 9c")
        self.chat_display.tag_add(tag, start, end)
        self.chat_display.yview(tk.END)
        self.chat_display.config(state=tk.DISABLED)

    def send_message(self):
        """Handles user input, calls the external sentiment engine, and updates display."""
        msg = self.msg_input.get().strip()
        self.msg_input.delete(0, tk.END) 
        
        if not msg:
            return

        self.display_message("You", msg, "User")
        
        sentiment = get_sentiment_label(msg) 
    
        if sentiment == "Positive":
            chatbot_response = f"That's fantastic! (Sentiment: {sentiment})"
        elif sentiment == "Negative":
            chatbot_response = f"I sincerely apologize for that. (Sentiment: {sentiment})"
        else:
            chatbot_response = f"I see. Tell me more. (Sentiment: {sentiment})"
                   
        self.display_message("Vocalis", chatbot_response, "Chatbot")

        self.user_messages.append(msg)
        self.sentiment_labels.append(sentiment)
        self.full_exchange.append({
            'user_input': msg,
            'sentiment': sentiment,
            'chatbot_response': chatbot_response
        })
        
    def show_analysis(self):
        """Opens a new window to display the final Tier 1 and Tier 2 analysis."""
        if not self.user_messages:
            self.display_message("Vocalis", "No conversation history to analyze.", "Chatbot")
            return

        overall_sentiment = analyze_overall_sentiment(self.user_messages)
        trend_summary = summarize_sentiment_trend(self.sentiment_labels)
    
        self.msg_input.config(state=tk.DISABLED)
        
        analysis_window = tk.Toplevel(self.master)
        analysis_window.title("Sentiment Analysis Report")
        analysis_window.geometry("550x450")
        
     
        analysis_text = scrolledtext.ScrolledText(analysis_window, wrap=tk.WORD, 
                                                  font=("SF Mono", 10), bg="#F0F0F0",relief=tk.FLAT)
        analysis_text.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        analysis_text.insert(tk.END, "VOCALIS FINAL REPORT\n\n")
               
        analysis_text.insert(tk.END, "OVERALL CONVERSATION SENTIMENT\n", "header")
        analysis_text.insert(tk.END, f"Result:{overall_sentiment}\n\n", "bold_result")

        analysis_text.insert(tk.END, "SENTIMENT TREND SUMMARY\n", "header")
        analysis_text.insert(tk.END, f"{trend_summary}\n\n")
               
        analysis_text.insert(tk.END, "STATEMENT-LEVEL SENTIMENT\n", "header")
        
        for i, ex in enumerate(self.full_exchange):
            sentiment_tag = "neg" if ex['sentiment'] == "Negative" else "pos" if ex['sentiment'] == "Positive" else "neut"
            
            analysis_text.insert(tk.END, f"[{i+1}] User: \"{ex['user_input']}\"\n")
            analysis_text.insert(tk.END, f"    -> Sentiment: {ex['sentiment']}\n\n", sentiment_tag)

        analysis_text.tag_config("neg", foreground="#FF3B30", font=("SF Mono", 10, "bold")) 
        analysis_text.tag_config("pos", foreground="#34C759", font=("SF Mono", 10, "bold")) 
        analysis_text.tag_config("neut", foreground="gray")
        analysis_text.tag_config("header", font=("SF Mono", 10, "underline"))
        analysis_text.tag_config("bold_result", font=("SF Mono", 12, "bold"))

        analysis_text.config(state=tk.DISABLED)

if __name__ == "__main__":
    
    root = ThemedTk() 
    app = VocalisChatbotGUI(root)
    root.mainloop()