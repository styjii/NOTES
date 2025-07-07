from django.shortcuts import render, redirect
from api.notes import TableManager
from django.contrib import messages


def index_view(request):
    manager = TableManager()
    table_names = manager.get_all_table_names()
    return render(request, "webapp/index.html", {"tables": table_names})


def create_table_view(request):
    table_name = request.GET.get("table_name")
    manager = TableManager(table_name=table_name)
    try:
        was_created = manager.create(validate_name=True)
        if was_created:
            messages.success(request, f"Table '{table_name}' created successfully.")
        else:
            messages.warning(request, f"Table '{table_name}' already exists.")
    except ValueError as err:
        messages.error(request, str(err))

    return redirect("index")

def delete_table_view(request, table_name):
    manager = TableManager(table_name=table_name)
    was_deleted = manager.delete()
    if was_deleted:
        messages.success(request, f"Table '{table_name}' deleted successfully.")
    else:
        messages.warning(request, f"Table '{table_name}' does not exist.")
    return redirect("index")