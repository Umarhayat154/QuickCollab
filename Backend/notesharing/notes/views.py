from rest_framework import permissions, generics
from .models import Note
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from .serializers import NoteSerializer

class NoteListCreateView(generics.ListCreateAPIView):
    serializer_class=NoteSerializer
    permission_classes=[permissions.IsAuthenticated]

    def get_queryset(self):
        user=self.request.user
        if user.role =='author':
            return Note.objects.filter(author=user)
        else: 
            return Note.objects.filter(is_public=True)
        
        
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    

class NoteDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=NoteSerializer
    permission_classes=[permissions.IsAuthenticated]

    def get_queryset(self):
        user= self.request.user
        if user.role == "author":
            return Note.objects.filter(author=user)
        else:
            return Note.objects.filter(is_public=True)
        

    def perform_update(self, serializer):
        if self.request.user.role != 'author':
            raise PermissionDenied("Reader cannot update the Note")
        serializer.save()

    def perform_destroy(self, instance):
        if self.request.user.role !='author':
            raise PermissionDenied("Reader cannot delete the Note")
        instance.delete()



