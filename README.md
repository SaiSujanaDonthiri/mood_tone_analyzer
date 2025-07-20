# Mood Tone Analyzer Web App

A simple and interactive web application built using **Flask** and **TextBlob** that analyzes the sentiment of user-input text and displays the mood using emojis (😊 😢 😐). The app also tracks and displays mood trends in a clean interface.

---

## Features

- Analyze tone as Happy, Sad, or Neutral
- Emoji-based mood feedback
- Built with Flask and TextBlob
- Clean HTML/CSS frontend
- Simple and beginner-friendly

---

## How to Run

### 1. Clone or Download

```bash
git clone https://github.com/your-username/mood-tone-analyzer.git
cd mood-tone-analyzer
```

### 2. Install Required Libraries

```bash
pip install -r requirements.txt
python -m textblob.download_corpora
```

### 3. Start the App

```bash
python app.py
```

Visit: `http://127.0.0.1:5000`

---

## Example

**Input**:  
```text
I am so happy with how things are going!
```

**Output**:  
😊 Happy

---

## File Descriptions

| File/Folder     | Description                        |
|----------------|------------------------------------|
| `app.py`        | Flask backend with sentiment logic |
| `templates/`    | HTML frontend                      |
| `index.html`    | Web form + mood output             |
| `requirements.txt` | Required Python libraries       |
| `README.md`     | Project overview                   |

---

## Requirements

- Python 3.x
- Flask
- TextBlob

Install with:
```bash
pip install flask textblob
```

---

## Technologies Used

- Python
- Flask (Backend)
- TextBlob (Sentiment Analysis)
- HTML/CSS (Frontend)
- Chart.js *(optional, for dashboard features)*

---
## Author

Sai Sujana Donthiri

