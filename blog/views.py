from django.shortcuts import render, redirect
from blog.forms import PostForm
from blog.models import Post, Restaurant
from django.views.generic import CreateView
from blog.forms import PostForm
from blog.formsfor import RestaurantForm


def index(request):
    # 전체 포스팅을 가져올 준비. 아직 가져오지는 않음.
    post_qs = Post.objects.all().order_by("-id") # pk = id
    return render(request, "blog/index.html", {
    "post_list" : post_qs,
    })
    # {}는 () 안으로 들어가야 함 = 3번째 인자가 되어야 함!


def single_post_page(request, pk):
    post = Post.objects.get(pk=pk) # all 전부 get 한가지
    return render(request, "blog/single_post_page.html", {
    "post" : post,
    })

# post_new = CreateView.as_view(
#     form_class=PostForm,
#     model=Post,
#     success_url="/blog/",
# )

def post_new(request):
    # print("request.method =", request.method)
    # print("request.POST =", request.POST)
    if request.method == "GET":
        form = PostForm()
    else:
        form = PostForm(request.POST)
        if form.is_valid():
            # 유효성 검사에 통과한 값들이 저장된 dict
            # form.cleaned_data
            post = form.save() # ModelForm에서 지원
            # return redirect("/blog/")
            # return redirect(f"/blog/{post.pk}")
            # return redirect(post.get_absolute_url())
            return redirect(post)

    return render(request, "blog/post_form.html", {
        "form" : form,
    })


####################################


def index_restaurant(request):
    post_qs = Restaurant.objects.all().order_by("-id") # pk = id
    return render(request, "blog/restaurant_index.html", {
    "post_list" : post_qs,
    })


def single_post_page_restaurant(request, pk):
    post = Restaurant.objects.get(pk=pk) # all 전부 get 한가지
    return render(request, "blog/restaurant_single_post_page.html", {
    "post" : post,
    })

def post_new_restaurant(request):
    if request.method == "GET":
        form = RestaurantForm()
    else:
        form = RestaurantForm(request.POST)
        if form.is_valid():
            restaurant = form.save() # ModelForm에서 지원
            return redirect(restaurant)
            # return redirect(f"/blog/restaurant/{restaurant.pk}/")

    return render(request, "blog/restaurant_post_form.html", {
        "form" : form,
    })