# 🧠 Social Media Analytics Tool

A **Python-based Social Media Analytics Tool** that performs **Sentiment Analysis** and **Keyword Extraction** on social media comments using **NLTK** and presents insights through an interactive **Tkinter GUI**.

---

## 🚀 Features
- 📂 Load CSV files containing social media data.
- 🧩 Perform **sentiment analysis** on comments (`Positive` / `Negative`).
- 🔍 Extract and count **keywords** (excluding stop words).
- 📊 Group results by **user** and display:
  - Followers count  
  - Total Likes  
  - Total Shares  
  - Caption and Comment  
  - Top Positive and Negative Keywords
- 🌙 **Dark-themed GUI** built using Tkinter.

---

## 🧰 Technologies Used
- **Python 3.x**
- **NLTK (Natural Language Toolkit)**
- **Tkinter (GUI Framework)**
- **Pandas**

---

## 📦 Installation

### 1️⃣ Clone or Download the Repository
```bash
git clone https://github.com/yourusername/social-media-analytics-tool.git

```
### 2️⃣ Install Required Libraries
```command
pip install pandas nltk

```
### 3️⃣ Download NLTK Data (first-time only)
```
nltk.download('stopwords')
nltk.download('punkt')
OR
python -m nltk.downloader stopwords punkt

```
🖥️ How to Run
```
Open the project folder in your IDE (VS Code, PyCharm, etc.)
python main.py

Use the Browse button in the GUI to select your CSV file.

Click Analyse to see sentiment and keyword analytics.

```
🧑‍💻 Author & License Section
```
## 👨‍💻 Author
**Saurav**  
📍 Python Developer | Data Enthusiast

```
## 📜 License
```
This project is open-source and available under the **MIT License**.

```
## 🖼️ Example Screenshots
```
### Application Window
![App Interface]  (screenshots/App_Interface.png)

### Analysis Result
![Result Output]  (screenshots/result_example.png)

