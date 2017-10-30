from django.core.exceptions import ValidationError

def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(
            ('%(value)s is not an even number'),
            params={'value': value},
        )


def clean_email(value):
    email = value
    if ".edu" in email:
        raise ValidationError("We do not accept EDU emails")


CATEGORIES = ['Mexican', 'Asian', 'American', 'Whatever']

def validate_categories(value):
    cat = value.capitalize()
    if not value in CATEGORIES and cat not in CATEGORIES:
        raise ValidationError(f"{value} not a valid food category")
