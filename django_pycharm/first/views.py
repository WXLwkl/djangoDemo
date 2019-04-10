from django.shortcuts import render
from django.shortcuts import HttpResponse
from first import models

user_list = [
    {'user':'jack', 'pwd':'abc'},
    {'user':'tom', 'pwd':'def'},
]

def index(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        # temp = {'user':username, 'pwd':password}
        # user_list.append(temp)

        models.UserInfo.objects.create(user=username, pwd=password)

        print(username, password)
    user_list = models.UserInfo.objects.all()
    return render(request,"index.html", {'data': user_list})

def hello(request):
    return HttpResponse('''
    
    The Zen of Python, by Tim Peters \n

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
    
    
    ''')