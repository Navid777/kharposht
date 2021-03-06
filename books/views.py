# -*- coding: utf-8 -*-s
from books.models import Book, Author, Subject, News, Article
from django.core.mail import send_mail
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from smtplib import SMTPException

def home(request):
    home_books = Book.objects.filter(on_homepage=True)
    featured_book = Book.objects.filter(featured_homepage=True)
    noted_authors = Author.objects.filter(on_homepage=True)
    if noted_authors.count() > 6:
        noted_authors = noted_authors[0:6]
    if featured_book.count() > 0:
        featured_book = featured_book[0]
    else:
        featured_book = None
    return render(request, 'home.html', {
        'books': home_books,
        'featured_book': featured_book,
        'noted_authors': noted_authors,
    })
    
def search(request, term):
    books = Book.objects.filter(Q(title__contains=term)|Q(description__contains=term))
    authors = Author.objects.filter(Q(first_name__contains=term)|Q(last_name__contains=term)|Q(description__contains=term))
    if not books :
        book_width = 0
    elif books.count() == 1:
        book_width = 12
    elif books.count() == 2:
        book_width = 6
    elif books.count() == 3:
        book_width = 4
    else:
        book_width = 3
    return render(request, 'search.html', {
        'book': book,
        'books': books,
        'book_width': book_width,
        'authors': authors,
        'term':term,
    })

def m_search(request):
    term = request.GET['search']
    books = Book.objects.filter(Q(title__contains=term)|Q(description__contains=term))
    authors = Author.objects.filter(Q(first_name__contains=term)|Q(last_name__contains=term)|Q(description__contains=term))
    if not books :
        book_width = 0
    elif books.count() == 1:
        book_width = 12
    elif books.count() == 2:
        book_width = 6
    elif books.count() == 3:
        book_width = 4
    else:
        book_width = 3
    return render(request, 'search.html', {
        'book': book,
        'books': books,
        'book_width': book_width,
        'authors': authors,
        'term':term,
    })
    

def author(request, id):
    author = get_object_or_404(Author, id=id)
    books = Book.objects.filter(Q(authors=author) | Q(translators=author))
    if books.count() == 1:
        book_width = 12
    elif books.count() == 2:
        book_width = 6
    elif books.count() == 3:
        book_width = 4
    else:
        book_width = 3
    return render(request, 'author.html', {
        'author': author,
        'books': books,
        'book_width': book_width,
        'mode': 1,
    })

def book(request, id):
    book = get_object_or_404(Book, id=id)
    books = Book.objects.filter(Q(authors__in=book.authors.all()) | 
                                Q(translators__in=book.authors.all()) |
                                Q(translators__in=book.translators.all()) | 
                                Q(authors__in=book.translators.all())).exclude(id=book.id)
    if not books :
        book_width = 0
    elif books.count() == 1:
        book_width = 12
    elif books.count() == 2:
        book_width = 6
    elif books.count() == 3:
        book_width = 4
    else:
        book_width = 3
    return render(request, 'book.html', {
        'book': book,
        'books': books,
        'book_width': book_width,
        'mode':1
    })

def all_books(request):
    books = Book.objects.all()
    book_width = 4
    title="همه‌ی ِکتاب‌ها"
    return render(request, 'book_list.html', {
        'books': books,
        'title':title,
        'mode':1
    })

def author_list(request, first):
    if first==u'ا':
        second = "آ"
        authors = Author.objects.filter(Q(last_name__startswith=first) | Q(last_name__startswith=second)|Q(first_name__startswith=first)|Q(first_name__startswith=second))
    else:
        authors = Author.objects.filter(Q(last_name__startswith=first) | Q(first_name__startswith=first))
    return render(request, 'author_list.html', {'authors':authors})

def all_authors(request):
    authors = Author.objects.all()
    return render(request, 'author_list.html', {'authors':authors})

def contact_us(request):
    return render(request, 'contact.html')

def books_by_subject(request, id):
    books = Book.objects.filter(subjects=id)
    title = Subject.objects.get(id=id).name
    return render(request, 'book_list.html', {'books':books, 'title':title, 'mode':1})

def news_by_subject(request, id):
    news = News.objects.filter(subjects=id)
    title = "اخبار"
    return render(request, 'book_list.html', {'books':news, 'title':title, 'mode':3})

def all_news(request):
    news = News.objects.all()
    title = "اخبار"
    return render(request, 'book_list.html', {'books':news, 'title':title, 'mode':3})

def articles_by_subject(request, id):
    articles = Article.objects.filter(subjects=id)
    title = "مقالات"
    return render(request, 'book_list.html', {'books':articles, 'title':title, 'mode':2})

def all_articles(request):
    articles = Article.objects.all()
    title = "مقالات"
    return render(request, 'book_list.html', {'books':articles, 'title':title, 'mode':2})

def not_published_books(request):
    books = Book.objects.filter(published=False)
    title = "منتشر می‌شود"
    return render(request, 'book_list.html', {'books':books, 'title':title, 'mode':1})

def published_books(request):
    books = Book.objects.filter(published=True)
    title="منتشر شد"
    return render(request, 'book_list.html', {'books':books, 'title':title, 'mode':1})

def about_us(request):
    return render(request, 'about_us.html')

def article(request, id):
    article = get_object_or_404(Article, id=id)
    articles = None
    if not articles :
        article_width = 0
    elif articles.count() == 1:
        article_width = 12
    elif articles.count() == 2:
        article_width = 6
    elif articles.count() == 3:
        article_width = 4
    else:
        article_width = 3
    return render(request, 'book.html', {
        'book': article,
        'books': articles,
        'book_width': article_width,
        'mode':2,
    })

def news(request, id):
    news = get_object_or_404(News, id=id)
    newss = None
    if not newss :
        news_width = 0
    elif newss.count() == 1:
        news_width = 12
    elif newss.count() == 2:
        news_width = 6
    elif newss.count() == 3:
        news_width = 4
    else:
        news_width = 3
    return render(request, 'book.html', {
        'book': news,
        'books': newss,
        'book_width': news_width,
        'mode': 3
    })

@csrf_exempt
def send_mail_from_server(request):
    if request.method == "POST":
        try:
            subject = request.POST['subject']
            message = request.POST['message']
            from_mail = request.POST['from']
            to_mail = request.POST['to']
            send_mail(subject, message, from_mail, [to_mail], fail_silently=False)
            #send_mail("salam", "salam", "contact@vandadjalili.com", ["contact@vandadjalili.com"], fail_silently=False)
            return render(request, 'json/success.json')
        except SMTPException:
            return render(request, 'json/error.json')
    else:
        return HttpResponseNotAllowed(request)