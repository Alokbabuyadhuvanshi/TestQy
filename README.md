
  # 🎯 TestQy - MCQ Generator

  A simple Django-based Quiz Application where users can select:
  - Number of Questions
  - Category (General Knowledge, Science, Sports, History, etc.)
  - Difficulty (Easy, Medium, Hard)

  The app fetches real-time multiple-choice questions (MCQs) from the **Open Trivia API**, lets users attempt the quiz, and shows detailed results,
  including correct and wrong answers after submission.



## 🚀 Live Demo
🔗 Try it here: **[Quiz App Live](https://alokbabu9410.pythonanywhere.com/)**

---

## 🛠️ Features

- Choose number of questions (10, 20, 30)
- Select category and difficulty
- Only **MCQ type** questions
- No negative marking for wrong answers
- See your **final score**
- Responsive and clean UI
- Deployed on **PythonAnywhere**

---

## 📦 Tech Stack

- **Backend:** Django
- **Frontend:** HTML, CSS, JavaScript
- **API:** [Open Trivia Database (opentdb.com)](https://opentdb.com/)
- **Hosting:** PythonAnywhere

---

## 🧩 How it Works

1. User selects quiz settings (number of questions, category, difficulty).
2. App sends a request to the Open Trivia API.
3. MCQs are displayed one by one.
4. After submitting, the app compares the selected answers to correct ones.
5. User sees:
   - Their score
6. Option to retry the quiz.

---

## 🔧 How to Run Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/TestQy.git
   cd TestQy
   ```

2. **Create a virtual environment and activate it**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install django requests
   ```

4. **Run the Django development server**
   ```bash
   python manage.py runserver
   ```

5. **Open your browser** and visit:  
   `http://127.0.0.1:8000/`

---

## 📁 Project Structure

```
TestQy/
│
├── TestQy/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── Quiz/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   │      ├── home.html
│   │      └── quiz.html
│   │       
│   └── static/
│         └── style.css
│      
│
└── manage.py

```

---

## 📸 Screenshots


| | Home-Page ![image](https://github.com/user-attachments/assets/f6d33659-041c-4376-9451-47009ca4c971)
| | Quiz-Page ![image](https://github.com/user-attachments/assets/01c95c20-9319-467b-a0e4-a3c4a13b41a5)
| | Score-Page ![image](https://github.com/user-attachments/assets/9ddebfd3-a6ad-47b0-a447-08b2be954bb9)

---

## 🙏 Acknowledgements

- [Open Trivia DB](https://opentdb.com/) for providing awesome quiz data.
- Deployed using [PythonAnywhere](https://www.pythonanywhere.com/).

---

## 👨‍💻 Developer

- **Developer:** Alok Babu  
📧 [alokbabuyadhuvanshi@gmail.com](mailto:alokbabuyadhuvanshi@gmail.com)  
🔗 [LinkedIn](https://linkedin.com/in/alok-babu) • [GitHub](https://github.com/Alokbabuyadhuvanshi)
- **Hosted at:** [alokbabu9410.pythonanywhere.com](https://alokbabu9410.pythonanywhere.com/)

---

# 🌟 If you like this project, don't forget to give it a ⭐!

---
