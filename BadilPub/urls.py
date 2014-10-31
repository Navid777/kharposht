from django.conf.urls import patterns, include, url
from books import views
from django.conf import settings
from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'BadilPub.views.home', name='home'),
    # url(r'^BadilPub/', include('BadilPub.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.home),
    url(r'^authors/(\d+)/$', views.author),
    url(r'^books/(\d+)/$', views.book),
    url(r'^author_list/(\w+)/$', views.author_list),
    url(r'^all_authors/$', views.all_authors),
    url(r'^all_books/$', views.all_books),
    url(r'^contact_us/$', views.contact_us),
    url(r'^books_by_subject/(\d+)$', views.books_by_subject),
    url(r'^not_published/$', views.not_published_books),
    url(r'^published/$', views.published_books),
    url(r'^about_us/$', views.about_us),
    url(r'^search/([\w,\-,\s]+)/$', views.search),
    url(r'^m/search/$', views.m_search),
    url(r'^send_mail/$', views.send_mail_from_server),
    url(r'^all_news/$', views.all_news),
    url(r'^news_by_subject/(\d+)$', views.news_by_subject),
    url(r'^all_articles/$', views.all_articles),
    url(r'^articles_by_subject/(\d+)$', views.articles_by_subject),
    url(r'^article/(\d+)$', views.article),
    url(r'^news/(\d+)$', views.news),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
