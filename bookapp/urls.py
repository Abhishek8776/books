from django.urls import path
from .views import *

urlpatterns = [
    path("", BooksView.as_view(), name="book"),
    path("<uuid:id>/", BooksView.as_view(), name="book"),
    # path("editbook/<uuid:id>/",name="editbook"),
    path("bookdetails/<uuid:id>/", BookDetailsView.as_view(), name="bookdetails"),
    path("deletebook/<uuid:id>/", BookDeleteView.as_view(), name="deletebook"),
]
