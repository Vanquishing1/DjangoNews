from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
from .filters import NewsFilter, PostFilter
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import PostForm
class NewsListView(ListView):
    model = Post
    template_name = 'news/news_list.html'
    context_object_name = 'news'
    paginate_by = 10

    def get_queryset(self):
        return Post.objects.filter(type='news').order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = context['paginator']
        page = context['page_obj']

        context['page_range'] = paginator.get_elided_page_range(number=page.number, on_each_side=2, on_ends=1)
        return context

class NewsDetailView(DetailView):
    model = Post
    template_name = 'news/news_detail.html'
    context_object_name = 'news_item'

def search_news(request):
    news_list = Post.objects.filter(category='news')
    news_filter = NewsFilter(request.GET, queryset=news_list)
    return render(request, 'news/news_search.html', {'filter': news_filter})


def search_news(request):
    news_list = Post.objects.filter(type='news')
    news_filter = PostFilter(request.GET, queryset=news_list)
    return render(request, 'news/news_search.html', {'filter': news_filter})



class NewsCreateView(CreateView):
        model = Post
        form_class = PostForm
        template_name = 'news/news_form.html'

        def form_valid(self, form):
            form.instance.category = 'news'
            return super().form_valid(form)

class NewsUpdateView(UpdateView):
        model = Post
        form_class = PostForm
        template_name = 'news/news_form.html'

class NewsDeleteView(DeleteView):
        model = Post
        success_url = reverse_lazy('news_list')
        template_name = 'news/news_confirm_delete.html'
