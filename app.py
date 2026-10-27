import streamlit as st
import pandas as pd
import joblib
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "emails.csv"
MODEL_PATH = BASE_DIR / "phishing_model.joblib"

st.set_page_config(page_title="Phishing Email Detection", page_icon="🛡️", layout="wide")
st.title("🛡️ Phishing Email Detection Model")
st.caption("Educational ML mini project — check suspicious email text before interacting with it.")
st.warning("This is a learning demo, not a guarantee of safety. Never open suspicious links or attachments to test them.")

@st.cache_resource
def load_or_train_model():
    if MODEL_PATH.exists():
        return joblib.load(MODEL_PATH)
    df = pd.read_csv(DATA_PATH)
    pipeline = Pipeline([
        ("tfidf", TfidfVectorizer(lowercase=True, stop_words="english", ngram_range=(1, 2), max_features=12000)),
        ("classifier", LogisticRegression(max_iter=1000, class_weight="balanced", random_state=42))
    ])
    pipeline.fit(df["text"].astype(str), df["label"].astype(str))
    joblib.dump(pipeline, MODEL_PATH)
    return pipeline

try:
    model = load_or_train_model()
except Exception as e:
    st.error(f"Could not load/train model: {e}")
    st.stop()

with st.sidebar:
    st.header("About")
    st.write("Model: TF-IDF + Logistic Regression")
    st.write("Training data: included educational sample dataset")
    st.write("Labels: Phishing / Safe")
    st.write("Use only as a first-pass indicator.")

tab1, tab2, tab3 = st.tabs(["🔎 Check an Email", "📊 Model Evaluation", "📚 How It Works"])

with tab1:
    st.subheader("Paste email content")
    subject = st.text_input("Email subject (optional)", placeholder="e.g. Urgent account verification")
    body = st.text_area("Email body", height=220, placeholder="Paste the email text here. Do not click its links.")
    urls = st.text_input("URLs shown in the email (optional)", placeholder="Paste URL text only; do not open it")
    if st.button("Analyze Email", type="primary"):
        combined = f"Subject: {subject}\nBody: {body}\nURL text: {urls}".strip()
        if len(combined) < 10:
            st.info("Please enter a subject, email body, or URL text to analyze.")
        else:
            prediction = model.predict([combined])[0]
            probabilities = model.predict_proba([combined])[0]
            classes = list(model.classes_)
            score = float(probabilities[classes.index(prediction)]) * 100
            if prediction.lower() == "phishing":
                st.error(f"⚠️ Prediction: PHISHING (model confidence: {score:.1f}%)")
                st.write("Recommended action: do not click links, open attachments, reply, or provide credentials. Verify using a known official channel.")
            else:
                st.success(f"✅ Prediction: SAFE-LIKE (model confidence: {score:.1f}%)")
                st.write("Important: this prediction does not prove the email is safe. Check sender address, domain, links, and unexpected requests manually.")
            with st.expander("Text features noticed by the model"):
                words = ["urgent", "verify", "password", "account", "login", "click", "bank", "suspended", "prize", "invoice", "attachment", "security"]
                found = [w for w in words if w in combined.lower()]
                st.write("Common risk-related terms found:", ", ".join(found) if found else "No terms from this small illustrative list.")
                st.write("This list is an explanation aid only; the ML model uses TF-IDF text features.")

with tab2:
    st.subheader("Evaluate on held-out sample data")
    df = pd.read_csv(DATA_PATH)
    X_train, X_test, y_train, y_test = train_test_split(
        df["text"].astype(str), df["label"].astype(str), test_size=0.25,
        random_state=42, stratify=df["label"].astype(str)
    )
    eval_model = Pipeline([
        ("tfidf", TfidfVectorizer(lowercase=True, stop_words="english", ngram_range=(1, 2), max_features=12000)),
        ("classifier", LogisticRegression(max_iter=1000, class_weight="balanced", random_state=42))
    ])
    eval_model.fit(X_train, y_train)
    preds = eval_model.predict(X_test)
    accuracy = accuracy_score(y_test, preds)
    st.metric("Sample test accuracy", f"{accuracy * 100:.1f}%")
    st.caption("This score is from a small, hand-curated teaching dataset and is not representative of real-world performance.")
    labels = ["Phishing", "Safe"]
    cm = confusion_matrix(y_test, preds, labels=labels)
    fig, ax = plt.subplots()
    ax.imshow(cm)
    ax.set_xticks(range(len(labels)), labels=labels)
    ax.set_yticks(range(len(labels)), labels=labels)
    ax.set_xlabel("Predicted label")
    ax.set_ylabel("True label")
    ax.set_title("Confusion Matrix")
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            ax.text(j, i, str(cm[i, j]), ha="center", va="center")
    st.pyplot(fig)
    st.text("Classification report:\n" + classification_report(y_test, preds, zero_division=0))

with tab3:
    st.subheader("Project workflow")
    st.markdown("""
    1. **Dataset:** labelled email examples are stored in `data/emails.csv`.
    2. **Preprocessing:** TF-IDF converts email text into numerical features.
    3. **Training:** Logistic Regression learns patterns associated with the labels.
    4. **Prediction:** the trained pipeline classifies new text as `Phishing` or `Safe`.
    5. **Evaluation:** a held-out split is used to show accuracy and a confusion matrix.
    """)
    st.info("Real phishing detection should also use sender authentication, domain reputation, URL analysis, attachment sandboxing, and larger validated datasets. This mini project intentionally does not open or fetch URLs.")

st.divider()
st.caption("Mini project for educational use. A false negative is possible: treat unexpected requests for money, passwords, OTPs, or sensitive data with caution.")
