from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from question.models import Topic
from question.forms import CommentForm

def hello_world(request):
    print(dir(request))
    print(request.GET)
    a = request.GET.get('a', 0)
    b = request.GET.get('b', 0)
    res = "Hello, world!<br/>a={}<br/>b={}".format(a, b)
    return HttpResponse(res)

def index(request):
    topics = Topic.objects.all()[:10]
    context = {'topics': topics}
    return render(request, 'question/index.html', context)

class TopicView(DetailView):
    model = Topic
    template_name = 'question/topic.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print (dir(Topic))
        context['comment_add_url'] = f"/topic/{context['topic'].id}/comment_add"
        return context

class CommentAdd(CreateView):
    template_name = 'question/comment_add.html'
    form_class = CommentForm

    def get_initial(self):
        return {
            'topic': self.kwargs['topic_pk']
        }

    def get_success_url(self):
        return f"/topic/{self.kwargs['topic_pk']}"
