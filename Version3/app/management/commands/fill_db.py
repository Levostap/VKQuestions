from django.core.management.base import BaseCommand
from app.models import Profile, Question, Tag, Answer, QuestionLike, AnswerLike
import random

class Command(BaseCommand):
    def handle(self, *args, **options):
        # Создание пользователей
        for i in range(0, 30):
            Profile(
                first_name=random.choice(
                    ["Саша", "Петя", "Вася", "Иван", "Маша", "Даша", "Нина", "Макс", "Артём", "Никита"]
                ),
                last_name=random.choice(
                    ["Иванов", "Петров", "Сидоров", "Хирный", "Колотовкин", "Куклина", "Попов", "Самарёв"]
                ),
                email=str(i) + '_' + random.choice(
                    ["1@mail.ru", "2@mail.ru", "petrov@mail.ru", "qwerty@mail.ru", "5@mail.ru"]
                ),
                username=random.choice(
                    ["biryani", "alex", "username", "sidor", "qwerty", "samsa", 'super', 'history']
                ) + str(i),
                avatar=random.choice(
                    ["1.png", "2.png", "3.png", "4.png", "5.png", "6.png", "7.png", "8.png"]
                ),
            ).save()
        users = Profile.objects.all()

        # Создание тегов
        for i in range(0, 30):
            try:
                Tag(name=random.choice(
                    ["Тэг1", "Тэг2", "Тэг3", "Тэг4", "Тэг5", "Тэг6", "Тэг7"]
                )).save()
            except Exception:
                pass
        tags = Tag.objects.all()

        # Создание вопросов
        for i in range(0, 50):
            q = Question(
                title=str(i) + '_' + ' ' + random.choice(
                    ["Вопрос1",
                     "Вопрос2",
                     "Вопрос3",
                     "Вопрос4",
                     "Вопрос5",
                     "Вопрос6",
                     "Вопрос0",
                     ]
                ),
                text=random.choice(
                    ["Вопрос1",
                     "Вопрос2",
                     "Вопрос3",
                     "Вопрос4",
                     "Вопрос5",
                     "Вопрос6",
                     "Вопрос0",
                     ]
                ),
                user=random.choice(users),
            )
            q.save()
            for _ in range(0, random.randint(0, 3)):
                q.tags.add(random.choice(tags))
        questions = Question.objects.all()

        # Создание ответов
        for i in range(0, 100):
            Answer(
                text=random.choice(
                    ["Ответ1",
                     "Ответ2",
                     "Ответ3",
                     "Ответ4",
                     "Ответ5",
                     "Ответ6",
                     "Ответ0",
                     ]
                ),
                question=random.choice(questions),
                user=random.choice(users)
            ).save()
        answers = Answer.objects.all()

        # Создание лайков вопросов
        for _ in range(0, 200):
            like = QuestionLike(
                question=random.choice(questions),
                user=random.choice(users),
                is_like=bool(random.randint(0, 1))
            )
            like.save()
            if like.is_like:
                like.question.rating += 1
            else:
                like.question.rating -= 1
            like.question.save()

        # Создание лайков ответов
        for _ in range(0, 200):
            like = AnswerLike(
                answer=random.choice(answers),
                user=random.choice(users),
                is_like=bool(random.randint(0, 1))
            )
            like.save()
            if like.is_like:
                like.answer.rating += 1
            else:
                like.answer.rating -= 1
            like.answer.save()
