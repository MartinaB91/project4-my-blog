from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views.generic import ListView, DetailView, View
from blog_post.models import Post, Category, User
from django.views import generic
from django.http import HttpResponse
from django.db.models import Q

# class HomeView(ListView):
#     """ 
#      Used for showing posts on homepage
#      """
#     model = Post
#     template_name = 'index.html'


class BlogPostList(generic.ListView):
    """ 
     Used for showing posts on homepage
     """
    model = Post
    template_name = 'index.html'
    context_object_name = 'index'
    
    def get_queryset(self):
        all_published_posts = Post.objects.filter(published=1).order_by('-created_on')
        categories = Category.objects.all()

        queryset = {
            'all_published_posts': all_published_posts,
            'categories': categories,
        }

        return queryset
   

def like_post_home(request, slug):
    user = request.user
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_obj = get_object_or_404(Post, id=post_id)

        if post_obj.likes.filter(id=request.user.id).exists():
            post_obj.likes.remove(user.id)
            post_obj.number_of_likes -= 1
            post_obj.save()

        else:
            post_obj.likes.add(user.id)
            post_obj.number_of_likes += 1
            post_obj.save()

    return HttpResponse(post_obj.number_of_likes)

class CategoryPostList(generic.ListView):
    """ 
     Used for sorting out selected category on page for a specifik category.
     """
    model = Post
    template_name = 'posts_by_category.html'
    context_object_name = 'posts_by_category'
    
    def get_queryset(self):
        all_published_posts = Post.objects.filter(published=1).order_by('-created_on')
        categories = Category.objects.all()

        # Todo: Try to do better, split string on '/', category is second from last index.
        wsgiRequestSplitted = str(self.request).split('/')  
        # 'un-slugify' the string, in template acutal title is used so we replace '-' with ' '
        selected_category = wsgiRequestSplitted[len(wsgiRequestSplitted)-2].replace('-', ' ')

        queryset = {
            'all_published_posts': all_published_posts,
            'categories': categories,
            'selected_category': selected_category
        }
        return queryset

# Inspiration from:
# https://stackoverflow.com/questions/739776/how-do-i-do-an-or-filter-in-a-django-query
class SearchResult(View):
    def get(self, request):
        if request.method == 'GET':
            search = request.GET['search']
            # Filter on if post title or content contains text from search box
            posts = Post.objects.filter(Q(title__contains=search, published=1) | Q(content__contains=search, published=1))
            categories = Category.objects.filter(Q(name__contains=search))

            return render(request, 'search_result.html', {'search':search, 'posts': posts, 'categories': categories},)
        else: 
            return render(request, 'search_result.html', {})


