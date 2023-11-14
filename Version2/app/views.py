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

def paginate(request, objects_list, default_limit=10, pages_count=None):
    try:
        limit = int(request.GET.get('limit', default_limit))
    except ValueError:
        limit = default_limit
    if limit > 100:
        limit = default_limit
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404

    paginator = Paginator(objects_list, limit)
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    if not pages_count:
        page_range = paginator.page_range
    else:
        start = page.number - pages_count
        if start < 0:
            start = 0
        page_range = paginator.page_range[start: page.number + int(pages_count / 2)]
    return page, page_range