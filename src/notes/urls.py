from .views import table_detail_view ,create_note_view, update_note_view, delete_note_view
from django.urls import path

urlpatterns = [
    path('detail-<str:table_name>', table_detail_view, name="table-detail"),
    path('create-note/', create_note_view, name="create-note"),
    path('update-note/', update_note_view, name="update-note"),
    path('delete-note/', delete_note_view, name="delete-note")
]
