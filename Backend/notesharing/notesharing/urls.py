from django.contrib import admin

from django.urls import path
from users.views import (
    RegisterView,CurrentUserView,UpdateUserView
)

from notes.views import(
    NoteListCreateView, NoteDetailView
)

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),

    path("api/auth/register/", RegisterView.as_view(), name="register"),

    path("api/auth/token/", TokenObtainPairView.as_view(),
         name="token_obtain_pair"),     
    path("api/auth/token/refresh/",
         TokenRefreshView.as_view(), name="token_refresh"),
    path("api/auth/me/",
         CurrentUserView.as_view(), name="current_user"),
    path("api/auth/me/update/",
         UpdateUserView.as_view(), name="profile_update"),
    path("api/notes/", NoteListCreateView.as_view(), name="notes_list_create"),

    path("api/notes/<int:pk>/",NoteDetailView.as_view(),name="note_details")
    
]

