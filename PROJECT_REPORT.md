# Project Report: Phishing Email Detection Model

## 1. Abstract
Phishing is a social-engineering attack in which an attacker attempts to trick a recipient into revealing credentials, financial details, or other sensitive information. This mini project demonstrates a machine-learning approach that classifies email text as `Phishing` or `Safe`. It uses TF-IDF for text feature extraction and Logistic Regression for classification. A Streamlit interface lets a user paste an email and view a prediction. A separate evaluation page displays sample accuracy, a confusion matrix, and a classification report.

## 2. Problem Statement
Users may find it difficult to recognize suspicious emails, especially messages that create urgency or request account verification. A simple educational tool can demonstrate how text classification may help flag potentially suspicious messages.

## 3. Objectives
- Prepare a labelled sample dataset of phishing and legitimate email examples.
- Convert email text into numerical features using TF-IDF.
- Train a Logistic Regression classifier.
- Predict whether supplied email text resembles phishing or safe examples.
- Display evaluation metrics and a confusion matrix.

## 4. Existing System
Users often rely on manual inspection or built-in email filters. Manual checks may miss warning signs, while a basic text-only model cannot inspect every technical signal.

## 5. Proposed System
The proposed application accepts an email subject, body, and optional URL text. It combines the text, applies the trained ML pipeline, and presents a predicted label and model confidence. The evaluation tab trains on a split of the included dataset and displays standard metrics.

## 6. Modules
1. Dataset module — loads labelled examples from CSV.
2. Text preprocessing module — uses TF-IDF vectorization.
3. Model training module — trains Logistic Regression.
4. Email analysis module — predicts the label for pasted text.
5. Evaluation module — calculates accuracy and classification report, and plots a confusion matrix.
6. User interface module — provides the Streamlit web interface.

## 7. System Workflow
Start → Load labelled email dataset → Clean/convert text using TF-IDF → Train classifier → User pastes email text → Model predicts Phishing/Safe → Display prediction → Evaluate model with test split → End.

## 8. Technology Stack
- Python 3.9+
- Scikit-learn
- Pandas
- Streamlit
- Matplotlib
- Joblib

## 9. Expected Outcome
The application demonstrates a complete ML classification workflow and provides a preliminary phishing-like text indicator, plus basic evaluation metrics.

## 10. Limitations
The bundled dataset is small and hand-curated, so the displayed score is not a reliable estimate of real-world performance. The model is text-only and does not verify sender identity, DNS records, domain reputation, URL redirects, or attachments. It can make false positives and false negatives. `Safe` must never be interpreted as guaranteed safe.

## 11. Future Enhancements
- Train and test on a larger, representative, licensed dataset.
- Add safe URL lexical analysis without opening the URL.
- Include sender/domain authentication indicators from authorized email headers.
- Use cross-validation and per-class precision/recall tracking.
- Integrate with a controlled mail-security workflow after privacy and security review.

## 12. Conclusion
This mini project introduces text classification for cybersecurity awareness. It combines TF-IDF, Logistic Regression, a simple user interface, and model evaluation to demonstrate how ML can assist—but not replace—careful phishing analysis.

## 13. Ethical Use
Use only for defensive learning. Do not upload confidential emails or personal data to an untrusted service. Never click suspicious links or open attachments to test them.
