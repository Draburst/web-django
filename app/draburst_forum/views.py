from typing import Any, Dict
from django.forms.models import BaseModelForm
from .forms import QuestionForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .models import Question


def main(request: HttpRequest):
    return render(request, 'main.html')


#def create_post(request):
#    if request.method == 'POST':
#        form = PostForm(request.POST)
#        if form.is_valid():
#            print(form.data.get('text'))
#            print(form.data.get('title'))
#            post = Question.objects.create(author_id=1, title=form.data.get('title'), text=form.data.get('text'))
#            post.save()
#        return redirect('/post')
#    else:
#        posts = Question.objects.all()
#        print(posts)
#        form = PostForm()
#
#    return render(request, 'main.html', {'form': form, 'posts': posts})

class PostViev(CreateView):
    model = Question
    form_class = QuestionForm
    template_name = 'main.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        contex =  super().get_context_data(**kwargs)
        contex['posts'] = Question.objects.all()
        return contex