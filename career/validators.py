from django.core.exceptions import ValidationError


def validate_file_size(file):
    max_size_mb = 2
    if file.size > max_size_mb * 1024 *102:
        raise ValidationError(f'The file size should not exxceed {max_size_mb} MB')
