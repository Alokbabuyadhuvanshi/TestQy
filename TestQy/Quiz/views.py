import random
from django.shortcuts import redirect, render
import html
import requests


def home(request):
    return render(request,'home.html')

def start_quiz(request):
    if request.method == "POST":
        amount = int(request.POST.get('amount',10))
        category = request.POST.get('category')
        difficulty = request.POST.get("difficulty")

        url = f"https://opentdb.com/api.php?amount={amount}" 
        
        if category:
            url += f"&category={category}"
        if difficulty:
            url += f"&difficulty={difficulty}"
        url += "&type=multiple"
        
        response = requests.get(url)
        data = response.json()

        questions = []
        if data['response_code'] == 0:
            for item in data['results']:
                question = {
                    'question': html.unescape(item['question']),
                    'correct_answer': html.unescape(item['correct_answer']),
                    'options': [html.unescape(option) for option in item['incorrect_answers']] + [html.unescape(item['correct_answer'])]
                }
                random.shuffle(question['options'])
                questions.append(question)
                
        else:
            return render(request, 'home.html', {'error': 'Could not fetch questions. Please try again.'})
        return render(request, 'quiz.html', {'questions': questions})
    return redirect('home')

def submit_quiz(request):
    if request.method == "POST":
        correct_answers = request.POST.getlist('correct_answer')
        selected_answers =[]

        for key,value in request.POST.items():
            if key.startswith('question_'):
                selected_answers.append(value)
        
        score = 0
        for correct, selected in zip(correct_answers, selected_answers):
            if correct == selected:
                score +=1

        return render(request, "score.html",{'score':score, 'total':len(correct_answers)})
    
    return redirect('home')



