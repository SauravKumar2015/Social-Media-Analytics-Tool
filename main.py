import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
import tkinter as tk
from tkinter import filedialog

# Download NLTK stop words
import nltk
nltk.download('stopwords')
nltk.download('punkt')

# Load stop words
stop_words = set(stopwords.words('english'))

# Function to perform sentiment analysis
def analyze_sentiment(text):
    sid = SentimentIntensityAnalyzer()
    sentiment_score = sid.polarity_scores(text)
    return "Positive" if sentiment_score['compound'] >= 0 else "Negative"

# Function to extract and count keywords
def extract_keywords(text_data):
    all_words = [word.lower() for text in text_data for word in word_tokenize(text) if
                 len(word) > 2 and word.lower() not in stop_words]
    keyword_counter = Counter(all_words)
    return keyword_counter

# Function to process data and update GUI
def process_data():
    try:
        file_path = filedialog.askopenfilename(title="Select Social Media Data File", filetypes=[("CSV Files", "*.csv")])

        if not file_path:
            return

        # Update file path label
        file_path_label.config(text=file_path)

        # Enable the Analyse button
        analyse_button.config(state=tk.NORMAL)

    except pd.errors.EmptyDataError:
        print("Error: The selected file is empty or not a valid CSV file.")
    except Exception as e:
        print("An error occurred:", e)

def analyse_data():
    try:
        # Read the CSV file into a pandas DataFrame
        df = pd.read_csv(file_path_label.cget("text"))

        # Apply sentiment analysis to each post
        df['Sentiment'] = df['Comment'].apply(analyze_sentiment)

        # Group by user and calculate keywords sentiments for each user
        user_data = {}
        for user, data in df.groupby('User'):
            user_keywords = extract_keywords(data['Comment'])
            user_sentiments = {'Positive': [], 'Negative': []}
            for sentiment in ['Positive', 'Negative']:
                user_sentiments[sentiment] = [(word, count) for word, count in user_keywords.items() if analyze_sentiment(word) == sentiment]
            user_data[user] = {
                'Followers': data['Followers'].iloc[0],  # Assuming 'Followers' remains constant for each user
                'Likes': data['Likes'].sum(),
                'Shares': data['Shares'].sum(),
                'Caption': data['Caption'].iloc[0],  # Add caption data
                'Comment': data['Comment'].iloc[0],
                'Keywords': user_sentiments
            }

        # Update GUI with results
        user_info_text.delete('1.0', tk.END)
        for user, data in user_data.items():
            user_info_text.insert(tk.END, f"\nUser: \t\t{user}\n")
            user_info_text.insert(tk.END, f"\nFollowers: \t\t{data['Followers']}\nLikes: \t\t{data['Likes']}\nShares: \t\t{data['Shares']}\n")
            user_info_text.insert(tk.END, f"\nCaption: \t{data['Caption']}\n")  # Display caption
            user_info_text.insert(tk.END, f"\nComment: \t{data['Comment']}\n")
            user_info_text.insert(tk.END, "\nKeywords Sentiments:\n")
            user_info_text.insert(tk.END, "\nPositive:\n")
            for keyword, count in data['Keywords']['Positive'][:5]:
                user_info_text.insert(tk.END, f"\t{keyword}: {count}\n")
            user_info_text.insert(tk.END, "\nNegative:\n")
            if data['Keywords']['Negative']:
                for keyword, count in data['Keywords']['Negative'][:5]:
                    user_info_text.insert(tk.END, f"\t{keyword}: {count}\n")
            else:
                user_info_text.insert(tk.END, "\tNo negative sentiments found\n")

    except pd.errors.EmptyDataError:
        print("Error: The selected file is empty or not a valid CSV file.")
    except Exception as e:
        print("An error occurred:", e)

# Create the main application window
app = tk.Tk()
app.title("Social Media Analytics Tool")

# Set window size and position
app_width = 600
app_height = 600
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
x = (screen_width - app_width) // 2
y = (screen_height - app_height) // 2
app.geometry(f"{app_width}x{app_height}+{x}+{y}")

# Configure dark theme colors
app.configure(bg='#333333')

# Create and configure widgets with dark theme
instruction_label = tk.Label(app, text="Please choose a CSV file:", bg='#333333', fg='#FFFFFF', font=('Helvetica', 12))
browse_button = tk.Button(app, text="Browse", command=process_data, bg='#555555', fg='#FFFFFF', width=10)
file_path_label = tk.Label(app, text="", bg='#333333', fg='#FFFFFF', font=('Helvetica', 10))
result_label = tk.Label(app, text="Result of Data:", bg='#333333', fg='#FFFFFF', font=('Helvetica', 12))
user_info_text = tk.Text(app, bg='#333333', fg='#FFFFFF', font=('Helvetica', 12))
analyse_button = tk.Button(app, text="Analyse", command=analyse_data, bg='#555555', fg='#FFFFFF', state=tk.DISABLED)

# Place widgets in the window using grid layout
instruction_label.grid(row=0, column=0, pady=10, padx=(10, 5), sticky='w')
browse_button.grid(row=0, column=1, pady=10, padx=(5, 10), sticky='w')
file_path_label.grid(row=1, column=0, columnspan=2, pady=5, padx=10, sticky='w')
result_label.grid(row=2, column=0, columnspan=2, pady=5, padx=10, sticky='w')
user_info_text.grid(row=3, column=0, columnspan=2, pady=5, padx=10, sticky='nsew')
analyse_button.grid(row=4, column=0, columnspan=2, pady=10)

# Configure row to expand with window size
app.grid_rowconfigure(3, weight=1)

# Start the GUI event loop
app.mainloop()