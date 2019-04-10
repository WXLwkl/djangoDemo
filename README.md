# django学习
> 小白学django笔记
> 转到虚拟环境 workon xx
> cd到django_pycharm 
> 运行`./manage.py runserver 9999`

1、安装python环境 `brew install python3`

2、安装虚拟环境Virtualenv及管理工具Virtualenvwrapper
`pip3 nstall virtualenv virtualenvwrapper`
修改~/.bash_profile或其它环境变量相关文件(如 .bashrc 或用 ZSH 之后的 .zshrc)
利用`which virtualenvwrapper.sh/python3`查找正确的路径
后添加一下：

```
# virtualenv-wrappper path
export WORKON_HOME=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python3
export VIRTUALENVWRAPPER_VIRTUALENV=/usr/local/bin/virtualenv
source /usr/local/bin/virtualenvwrapper.sh
```
执行 `source ~/.bash_profile`。 如果重新打开不能使用，则在`~/.zshrc`文件最后，增加一行： `source ~/.bash_profile`

3、创建虚拟环境

```
mkvirtualenv test：创建运行环境test

workon test: 工作在 test 环境 或 从其它环境切换到 test 环境

deactivate: 退出终端环境
```
4、虚拟环境
安装django(可指定不同版本) `pip3 install django==2.2`


其他 

```
workon ENV：激活运行环境ENV
rmvirtualenv ENV：删除运行环境ENV
mkproject mic：创建mic项目和运行环境mic
mktmpenv：创建临时运行环境
lsvirtualenv: 列出可用的运行环境
lssitepackages: 列出当前环境安装了的包
```

### 初体验(虚拟环境下)
1、创建项目 `django-admin startproject django_workspace`
启动项目`cd django_workspace` `./manage.py runserver 9999`
2、创建应用 `django-admin startapp hello`
主要修改的文件有
    - hello/views.py
    - templates/index.html
    - django_workspace/urls.py
    - django_workspace/settings.py

3、添加html
在django目录下新建templates文件夹，添加index.html文件。
4、修改hello/views.py （应用的视图文件）

```
from django.http import HttpResponse

def hello(request):
    return HttpResponse('hello')

def index(request):
    return render(request, "index.html")

```
5、django_workspace/urls.py 的修改

```
from django.conf.urls import url
from django.contrib import admin
from hello import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello', views.hello),
    url(r'^index', views.index),
]
```
6、django_workspace/settings.py 的配置

* 配置允许被访问的地址`ALLOWED_HOSTS = ["*"]`
* 添加应用
```
INSTALLED_APPS = [
    'hello',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```
* 增加模版路径
```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates').replace('\\', '/'),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

***这里附上一份简单的配置说明***

```
BASE_DIR            // 根目录
DEBUG               // 调试开关，开发模式下为True
INSTALLED_APPS      // APP路径，默认添加同名app名称即可
DATABASES           // 数据库配置，默认SQLITE3，如果使用MYSQL需要另行配置，此处不做阐述
ALLOWED_HOSTS       // 允许被访问的IP，此处可在括号内填星号，表示允许所有IP
STATIC_URL          // 静态文件临时调用目录
STATICFILES_DIRS    // 静态文件目录
MIDDLEWARE          // 中间件，自己写的中间件要填在系统自带中间件之后
TEMPLATES           // 模版
```

#### 使用静态文件
在html文件中，需要添加js、css等文件。django中一般将文件放到static目录中。在django目录下新建static文件夹，在static文件下添加js、css、imgs文件夹。
为了让django找到这个目录，依然需要对settings进行配置
`STATIC_URL = '/static/'` 这个指的是引用指针，不是具体的目录，可以改成你想要的任何名字。但是在html文件中，要与它保持对应。


```
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
```
新建一行，写上这个固定的全局变量名，赋值一个元祖。括号中的static和目录的名字对应，和html的引用无关。
在html中写`<script src="/static/js/jquery.js"></script>` 这个`static`是在settings文件中的那个引用字符串，不是目录里的static目录。

#### 数据请求时会用到跨域请求，需要在settings中的`MIDDLEWARE`中把`django.middleware.csrf.CsrfViewMiddleware`注释掉。

#### 使用数据库
使用自带的数据库
在app的models.py文件中修改，创建2个字段，分别保存用户的名字和密码

```
class UserInfo(models.Model):
    user = models.CharField(max_length=32)
    pwd = models.CharField(max_length=32)

```

在teminal中通过命令行创建数据库的表。2个命令：
1、`python3 manage.py makemigrations`/`./manage.py makemigrations`
2、`python3 manage.py migrate`
修改views.py的业务处理
`models.Userinfo.objects.create(user=username, pwd=password)`添加数据
`user_list = models.UserInfo.objects.all()`读取数据




