from bot import views
from django.urls import path

urlpatterns = [
    path("webhook", views.WebHook.as_view()),
    path("search",views.searchbook),
    path("chatbot",views.chatInterface),
    path("TitleStrip",views.TitleStrip),
    # path("deletebooks",views.deleteAllBooks),
]
