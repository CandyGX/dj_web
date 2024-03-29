from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
# Create your views here.
from django.template import loader
from django.urls import reverse
from helloworld.models import Question, Choice


def index(request):
    """
    request 就是作为参数传进来的请求对象
    :param request:
    :return: HttpResponse 处理完请求的返回对象
    """
    # return HttpResponse('Helle World')

    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('helloworld/index.html')
    # context = {
    #     'latest_question_list': latest_question_list,
    # }
    # return HttpResponse
    # (template.render(context, request))

    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'helloworld/index.html', context)


def detail(request, question_id):
    # question = get_object_or_404(Question, pk=question_id)
    # return render(request, 'helloworld/detail.html', {'question': question})
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'helloworld/detail.html', {'question': question})


def results(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'helloworld/detail.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'helloworld/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('helloworld:results', args=(question.id,)))