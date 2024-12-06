from django.core.exceptions import ValidationError


def image_size_validator(image):
    max_size_mb = 2
    if image.size > max_size_mb * 1024 * 1024:
        raise ValidationError(f"Photo file size cannot be over {max_size_mb}MB.")