from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from feed.forms import FeedForm
from feed.models import Post


class FeedView(TemplateView):
    template_name= 'feed/feed_page.html'

    def get(self, request):
        form=FeedForm()
        posts= Post.objects.all().order_by('-date')
        return render(request,self.template_name,{'form': form,'posts': posts})

    def post(self, request):
        form= FeedForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.user= request.user
            post.save();
            return redirect('/feed/mainpage')

        return render(request,self.template_name,{'form':form})
