from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator
from django.db import models


def validate_pdf_size(file_obj):
    max_size_mb = 15
    if file_obj.size > max_size_mb * 1024 * 1024:
        raise ValidationError(f"PDF size must not exceed {max_size_mb} MB.")


class Document(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(
        upload_to="pdfs/",
        validators=[
            FileExtensionValidator(allowed_extensions=["pdf"]),
            validate_pdf_size,
        ],
    )
    is_indexed = models.BooleanField(default=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-uploaded_at"]

    def __str__(self):
        return self.title
