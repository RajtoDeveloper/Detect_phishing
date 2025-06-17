# Detect_phishing
This tool analyzes URLs using a Logistic Regression model trained on 10,000+ phishing/good links. It flags suspicious sites, blocks threats automatically, and logs them to a MySQL database—all in a lightweight Streamlit interface.

## 📌 Overview
A machine learning-based system that detects phishing URLs with *92%+ accuracy*, featuring:
- Real-time URL classification
- Malicious URL blocking system
- Database logging of suspicious sites

## 🎯 Purpose
Protect users from phishing attacks by automatically identifying malicious URLs before they cause harm.

## 🔧 How It Works
1. *URL Analysis*:
   - Tokenizes URL into features (domain, paths, parameters)
   - Uses TF-IDF vectorization to convert to numerical features
2. *Machine Learning*:
   - Logistic Regression classifier trained on 10,000+ URLs
   - Makes real-time predictions (good/bad)
3. *Protection System*:
   - Blocks detected phishing URLs
   - Maintains database of malicious sites

## 🛠 Technical Stack
| Component       | Technology Used |
|----------------|----------------|
| *Frontend*   | Streamlit (Python) |
| *Backend*    | Python 3.7+ |
| *ML Model*   | Scikit-learn (Logistic Regression) |
| *Database*   | MySQL |
| *Vectorizer* | TF-IDF with custom tokenizer |

## ✨ Key Features
- 🚨 Real-time phishing detection
- 📊 Visual URL threat dashboard
- 🔒 Automatic URL blocking
- 📝 Historical threat logging
- 📱 Responsive web interface
