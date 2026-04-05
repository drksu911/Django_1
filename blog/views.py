from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.conf import settings
from .models import Blog

class BlogListView(ListView):
    model = Blog
    template_name = 'blog/blog_list.html'
    context_object_name = 'blogs'

    def get_queryset(self):
        return Blog.objects.filter(is_published=True)

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/blog_detail.html'
    context_object_name = 'blog'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        old_views = obj.views_count
        obj.views_count += 1
        obj.save(update_fields=['views_count'])
        if old_views < 100 <= obj.views_count:
            send_mail(
                subject='Статья достигла 100 просмотров!',
                message=f'Статья "{obj.title}" набрала 100 просмотров.',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=['drksu91@mail.ru'],  # замените на свой email
                fail_silently=True,
            )
        return obj

class BlogCreateView(CreateView):
    model = Blog
    fields = ['title', 'content', 'preview', 'is_published']
    template_name = 'blog/blog_form.html'
    success_url = reverse_lazy('blog_list')

class BlogUpdateView(UpdateView):
    model = Blog
    fields = ['title', 'content', 'preview', 'is_published']
    template_name = 'blog/blog_form.html'

    def get_success_url(self):
        return reverse_lazy('blog_detail', args=[self.object.id])

class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'blog/blog_confirm_delete.html'
    success_url = reverse_lazy('blog_list')