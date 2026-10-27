# Phishing Email Detection Model — Mini Project

## Features
- Machine learning text classifier using TF-IDF + Logistic Regression
- Paste subject/body/URL text to classify an email as `Phishing` or `Safe`
- Training/evaluation tab with sample accuracy, classification report, and confusion matrix
- Included sample dataset
- Streamlit web interface

## Requirements
Python 3.9 or newer.

## Run on Windows
1. Extract the ZIP.
2. Open Command Prompt in this folder.
3. Create a virtual environment (recommended):
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```
4. Install packages:
   ```bash
   pip install -r requirements.txt
   ```
5. Start the app:
   ```bash
   streamlit run app.py
   ```
6. The browser will open the local app. If it does not, use the local URL shown in the terminal.

## Run on Linux/macOS
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## Dataset
`data/emails.csv` is a small hand-curated educational dataset. It is suitable for demonstrating the workflow only, not for claiming production-level accuracy.

## Important limitations
- Text-only model; it does not authenticate the sender or safely inspect links.
- The URL field is treated as text. URLs are never opened or fetched.
- Attackers can change wording, and legitimate messages can look suspicious.
- A `Safe` prediction is not proof that an email is safe.
- Replace the sample dataset with a larger, licensed, representative dataset before research or deployment.

## Ethical use
Use for awareness and defensive education. Do not use it to test live links by opening them or to collect other people's private emails without permission.
