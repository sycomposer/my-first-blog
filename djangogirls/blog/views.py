from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone
from .forms import PostForm
from django.shortcuts import redirect

def post_list(request):
    #HttpResponse는 print()구문처럼 내부에 적은 문자열을 화면에 출력한다.
    #단, HttpResponse는 콘솔창에 출력하지 않고, 웹페이지에 출력해준다.
    #return HttpResponse('post_list준비중')
    posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    #render 함수는 바로 템플릿 파일을 지정해서 사용할 수 있다.
    return render(request, "blog/post_list.html", {'posts':posts})

'''Post.object.을 이용해서 다음 조건을 만족시키는 ORM을 사용해보세요.
1.배포 시간이 현재 시간 이전일 것
2.published_date 기준으로 내림차순'''
def post_detail(request,pk):
    post= get_object_or_404(Post,pk=pk)
    return render(request,"blog/post_detail.html",{'post':post})

def post_new(request):
    # when you create form 양식,forms.py내부의 자료를 form 이라는 변수에 저장받는다.
    if request.method == "POST":
        #PostForm양식을 받아오되 POST방식으로 전달된 데이터를 채워넣는다.
        #이렇게 되면 title,text, create_date 세개의 컬럼에 자료가 채워진다
        #However, there is no documents in the author, published_date.
        form = PostForm(request.POST)
    #It checks out whether incoming documents is right or not by .is_valid.
    #If the documents is right, the is_valid() will be TRUE.
    #It sents the Form to Template by using render method.
        if form.is_valid():
        #temporarily stores 3 documents for saving all documents 
        #if you operate save() method, commit=False
            post = form.save(commit=False)
            post.author = request.user
            #in author column, you should put in a request user.
            post.published_date = timezone.now()
            post.save()
            #This is a function to go to detailed page.
        return redirect('post_detail',pk=post.pk)
    else:
        form = PostForm()
        return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request,pk):
    #when the user accesses a place which has no users.
    post = get_object_or_404(Post, pk=pk)
    #in the case of POST method(in the case of edit button)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        #whether the information which is already written is valid or not .
        if form.is_valid():
            #when you make edit, you should also check out published_date and author.
            #Thus, first, you make temporal store, and then you type author and published_date.
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        #in the case of get method, the computer shows edit window 
        form =PostForm(instance=post)
    return render(request,'blog/post_edit.html', {'form':form})
# Create your views here.
