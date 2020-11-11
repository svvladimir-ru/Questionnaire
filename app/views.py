from django.shortcuts import get_object_or_404
from .models import Question, Poll, Choice, Answer
from .serializers import PollSerializer, QuestionSerializer, ChoiceSerializer, AnswerSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.response import Response
from django.utils import timezone
from rest_framework import viewsets


"""Создание опроса"""
@api_view(['POST'])
@permission_classes((IsAuthenticated, IsAdminUser,))
def poll_create(request):
    serializer = PollSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
        poll = serializer.save()
        return Response(PollSerializer(poll).data, status=201)
    return Response(serializer.errors, status=400)


"""Изменение опроса"""
@api_view(['PATCH', 'DELETE'])
@permission_classes((IsAuthenticated, IsAdminUser,))
def poll_update(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    if request.method == 'PATCH':
        serializer = PollSerializer(poll, data=request.data, partial=True)
        if serializer.is_valid():
            poll = serializer.save()
            return Response(PollSerializer(poll).data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        poll.delete()
        return Response("Опрос удален", status=204)


"""Получение всех опросов"""
@api_view(['GET'])
@permission_classes((AllowAny,))
def polls_view(request):
    polls = Poll.objects.all()
    serializer = PollSerializer(polls, many=True)
    return Response(serializer.data)


"""Создание вопроса"""
@api_view(['POST'])
@permission_classes((IsAuthenticated, IsAdminUser,))
def question_create(request):
    serializer = QuestionSerializer(data=request.data)
    if serializer.is_valid():
        question = serializer.save()
        return Response(QuestionSerializer(question).data, status=201)
    return Response(serializer.errors, status=400)


"""создание вопроса через viewset"""
class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [
        IsAuthenticated
    ]

    def perform_create(self, serializer):
        serializer.save()


"""Изменение вопроса"""
@api_view(['PATCH', 'DELETE'])
@permission_classes((IsAuthenticated, IsAdminUser,))
def question_update(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'PATCH':
        serializer = QuestionSerializer(question, data=request.data, partial=True)
        if serializer.is_valid():
            question = serializer.save()
            return Response(QuestionSerializer(question).data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        question.delete()
        return Response("Вопрос удален", status=204)


"""Создание выбора ответа"""
@api_view(['POST'])
@permission_classes((IsAuthenticated, IsAdminUser,))
def choice_create(request):
    serializer = ChoiceSerializer(data=request.data)
    if serializer.is_valid():
        choice = serializer.save()
        return Response(ChoiceSerializer(choice).data, status=201)
    return Response(serializer.errors, status=400)


"""Изменение выбор"""
@api_view(['PATCH', 'DELETE'])
@permission_classes((IsAuthenticated, IsAdminUser,))
def choice_update(request, choice_id):
    choice = get_object_or_404(Choice, pk=choice_id)
    if request.method == 'PATCH':
        serializer = ChoiceSerializer(choice, data=request.data, partial=True)
        if serializer.is_valid():
            choice = serializer.save()
            return Response(ChoiceSerializer(choice).data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        choice.delete()
        return Response("Выбор удален", status=204)


"""просмотр активных опросов"""
@api_view(['GET'])
@permission_classes((AllowAny,))
def active_polls_view(request):
    polls = Poll.objects.filter(
        end_date__gte=timezone.now()).filter(
        pub_date__lte=timezone.now()
    )
    serializer = PollSerializer(polls, many=True)
    return Response(serializer.data)


"""Создание ответа"""
@api_view(['POST'])
@permission_classes((AllowAny,))
def answer_create(request):
    serializer = AnswerSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
        answer = serializer.save()
        return Response(AnswerSerializer(answer).data, status=201)
    return Response(serializer.errors, status=400)


"""Просмотр ответов"""
@api_view(['GET'])
@permission_classes((AllowAny,))
def answer_view(request, user_id):
    answers = Answer.objects.filter(user_id=user_id)
    serializer = AnswerSerializer(answers, many=True)
    return Response(serializer.data)


"""Изменение ответа"""
@api_view(['PATCH', 'DELETE'])
@permission_classes((AllowAny,))
def answer_update(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.method == 'PATCH':
        serializer = AnswerSerializer(answer, data=request.data, partial=True)
        if serializer.is_valid():
            answer = serializer.save()
            return Response(AnswerSerializer(answer).data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        answer.delete()
        return Response("Ответ удален", status=204)
