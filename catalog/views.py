from django.shortcuts import render
from .models import Product, Category, Blog
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from pytils.translit import slugify


# def index(request):
#     context = {
#         'object_list': Product.objects.all()[:100],
#         'title': 'Продукты'
#     }
#     return render(request, 'catalog/index.html', context)


class IndexListView(ListView):
    model = Product
    template_name = 'catalog/index.html'


# def product(request, pk):
#     product_item = Product.objects.get(pk=pk)
#     context = {
#         'object_list': Product.objects.filter(pk=pk),
#         'title': f'{product_item.name}'
#     }
#     return render(request, 'catalog/product_detail.html', context)


class ProductDetailView(DetailView):
    model = Product


def contacts(request):
    context = {
        'title': 'Контакты'
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f"{name} - ({phone}): {message}")
    return render(request, 'catalog/contacts.html', context)


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'body', 'preview')
    success_url = reverse_lazy('catalog:view_blog')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()

        return super().form_valid(form)


class BlogListView(ListView):
    model = Blog
    template_name = 'catalog/blog_list.html'

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'body', 'preview')
    # success_url = reverse_lazy('catalog:view_blog')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('catalog:detail_blog', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('catalog:view_blog')
