from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import DocumentUploadForm
from .models import Document


def home(request):
    if request.method == "POST":
        form = DocumentUploadForm(request.POST, request.FILES)
        if form.is_valid():
            doc = form.save()
            messages.success(request, f"Uploaded '{doc.title}' successfully.")
            return redirect("retrieval:home")
    else:
        form = DocumentUploadForm()

    documents = Document.objects.all()
    return render(
        request,
        "retrieval/home.html",
        {"form": form, "documents": documents},
    )