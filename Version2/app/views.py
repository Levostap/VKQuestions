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
        } for i in range(5)
    ]
    return render(request, 'index.html', {'questions': questions})


def tag(request, tn):
    pass