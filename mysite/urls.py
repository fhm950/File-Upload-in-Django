from django.contrib import admin
from django.urls import path
from mysite.core import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home.as_view(), name='home'),
    path('upload/', views.upload, name='upload'),
    path('books/', views.book_list, name='book_list'),
    path('books/upload/', views.upload_book, name='upload_book'),
    path('class/books/', views.BookListView.as_view(), name='class_book_list'),
    path ('class/books/upload/', views.UploadBookView.as_view(), name='class_upload_book'),
    path('books/<int:pk>/', views.delete_book, name='delete_book'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
