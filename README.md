# 🧠 Trivia-Quiz

A graphical True/False Trivia Quiz app using Python and Tkinter, powered by the Open Trivia Database API.

---

## ✨ Features

- Interactive GUI made with Tkinter
- Fetches live True/False trivia questions from Open Trivia DB
- Real-time score tracking
- Visual feedback for correct and incorrect answers
- Automatically moves to the next question
- Quiz ends with a final score display

---
## 🧾 Requirements
Python 3.x

requests module (install with pip install requests)

Tkinter (usually preinstalled with Python)

---
## 💡 Customization & API Tips

This app uses the [Open Trivia DB API](https://opentdb.com/api_config.php) to fetch quiz questions. You can fully customize the quiz by editing the `parameters` in `data.py`:

```python
parameters = {
    "amount": 10,        # Number of questions
    "type": "boolean"    # "boolean" for True/False, or "multiple" for multiple-choice
}
```
Additionally,
- Add filters: Use "category" and "difficulty" parameters for more specific questions.

---
