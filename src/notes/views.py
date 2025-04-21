from django.shortcuts import redirect, render
from django.contrib import messages
from api.notes import Note, TableManager

def table_detail_view(request, table_name):
    manager = TableManager(table_name=table_name)
    notes = manager.get_all_contents()
    return render(request, "notes/index.html", {"notes": notes, "table_name": table_name})

def create_note_view(request):
    table_name = request.POST.get("table_name")
    note_content = request.POST.get("content")
    note = Note(table_name=table_name, content=note_content)
    try:
        was_saved = note.save(validate_content=True)
        if was_saved:
            messages.success(request, "Note added successfully.")
        else:
            messages.warning(request, "Note already exists.")
    except ValueError as err:
        messages.error(request, str(err))

    return redirect("table-detail", table_name)

def update_note_view(request):
    table_name = request.POST.get("table_name")
    current_content = request.POST.get("content")
    updated_content = request.POST.get("new_content")
    note = Note(table_name=table_name, content=current_content)
    try:
        was_updated = note.update(new_content=updated_content, validate_content=True)
        if was_updated:
            messages.success(request, "Note updated successfully.")
        else:
            messages.warning(request, "Note already exists or modification not required.")
    except ValueError as err:
        messages.error(request, str(err))

    return redirect("table-detail", table_name)

def delete_note_view(request):
    table_name = request.POST.get("table_name")
    note_content = request.POST.get("content")
    note = Note(table_name=table_name, content=note_content)
    was_deleted = note.delete()
    if was_deleted:
        messages.success(request, "Note deleted successfully.")
    else:
        messages.warning(request, "Note not found.")

    return redirect("table-detail", table_name)