from django.shortcuts import render

# Create your views here.


def index(request):
    questions = [
        {
            'id': i,
            'title': "Как взломать сайт МВД Бразилии? Я хочу...",
            'username': "Анатолий",
            'path': "question/" + str(i),
            'tag': "NeuralNetworks",
            'tag_path': "tag/" + "NeuralNetworks",
            'answer_count': 4
        } for i in range(10)
    ]
    return render(request, 'index.html', {'questions': questions})


def question(request, pk):
    question_info = [
        {
            'title': "Как сделать то...",
            'text': "Ну это... Ну то самое... ЭЭЭЭЭ... Да.",
            'tag': "NeuralNetworks",
            'tag_path': "tag/" + "NeuralNetworks",
            'username': "Анатолий"
        }
    ]
    answers = [
        {
           'username': "Алексей",
            'text': "Мда... " + str(i)
        } for i in range(5)
    ]
    return render(request, 'question.html', {'answers': answers, 'question': question_info})


def hot(request):
    questions = [
        {
            'id': i,
            'title': "Этот вопрос интереснее остальных",
            'path': "question/" + str(i),
            'tag': "hot",
            'tag_path': "tag/" + "hot",
            "answer_count": str(i) + " ответа",
        } for i in range(5)
    ]
    return render(request, 'index.html', {'questions': questions})


def ask(request):
    return render(request, 'ask.html')


def login(request):
    return render(request, 'signin.html')


def signup(request):
    return render(request, 'signup.html')


def tag(request, tn):
    questions = [
        {
            'id': i,
            'title': "Это вопрос с определённым тегом",
            'username': "Анатолий",
            'path': "question/" + str(i),
            'tag': tn,
            'tag_path': "tag/" + tn,
            'answer_count': 4
        } for i in range(10)
    ]
    return render(request, 'index.html', {'questions': questions})


def paginator(questions, page, per_page = 10): #questions - общее количество элементов, page - номер отображаемой страницы, per_page - сколько элементов на странице должно быть
    pag_questions = []
    for i in range(page * per_page, page * per_page + per_page):
        pag_questions.append(questions[i])
    return pag_questions
