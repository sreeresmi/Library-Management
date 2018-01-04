from django.conf.urls import include, url
from django.contrib import admin
from librarymgmt import views


urlpatterns = [
    # Examples:
    # url(r'^$', 'weavedin.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^book_info', views.book_info),
    url(r'^book_info', views.book_info),
   
    url(r'bookdetail/(?P<bookname>[a-zA-z]+)$', views.bookdetail, name='bookview'),
	url(r'author_info/(?P<authorname>[a-zA-z]+)$', views.authordetail, name='booklist'),
	url(r'^author_info', views.author_info),

]

