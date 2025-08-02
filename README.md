#  Interactive AI CV / Conversational Portfolio

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Gradio](https://img.shields.io/badge/Gradio-FF7C00?style=for-the-badge&logo=gradio&logoColor=white)
![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-yellow?style=for-the-badge)

---

### 🔴 **[View Live Demo Here](https://huggingface.co/spaces/HamidOmarov/hamid-interactive-cv)** 🔴

---

### Project Overview

This project addresses the limitations of static, one-dimensional resumes by creating a dynamic, conversational AI assistant. It allows recruiters and hiring managers to interactively ask questions about my skills, projects, and professional journey, receiving instant, detailed answers. This portfolio piece is a live demonstration of my ability to build and deploy functional AI systems from concept to completion.

### Key Features
- **Natural Language Queries:** Ask questions in plain English.
- **Custom-Built Search Algorithm:** A hybrid, keyword-based search engine with a "Super Bonus" system for prioritizing specific projects.
- **Comprehensive Knowledge Base:** Trained on a collection of documents detailing my entire professional profile.
- **Live Deployment:** Fully functional and publicly accessible via Hugging Face Spaces.

### Demo GIF![AI Assistant](https://github.com/user-attachments/assets/1c085540-7fe7-4089-92e2-0f3fc9aeddd7)



### Tech Stack
- **Backend:** Python
- **UI Framework:** Gradio
- **Deployment Platform:** Hugging Face Spaces
- **Version Control:** Git / Git Bash

### How It Works
1.  **Knowledge Base:** The bot's "brain" is a collection of `.txt` files containing my story, work experience, project details, and a pre-compiled Q&A list.
2.  **Search Algorithm:** A custom Python script (`app.py`) reads all text files and splits them into logical paragraphs ("chunks"). When a question is asked, my hybrid search algorithm scores each chunk based on the keywords in the question, giving a "super bonus" to specific project names to ensure high accuracy.
3.  **Deployment:** The entire application is hosted on Hugging Face Spaces, with updates managed and deployed via Git.

### How to Run Locally
```bash
# 1. Clone the repository
git clone [https://github.com/HamidOmarov/AI-Conversational-Portfolio.git](https://github.com/HamidOmarov/AI-Conversational-Portfolio.git)

# 2. Navigate to the project directory
cd AI-Conversational-Portfolio

# 3. Install the required libraries
pip install -r requirements.txt

# 4. Run the application
python app.py
