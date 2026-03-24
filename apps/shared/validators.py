import re
from django.utils import timezone
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

phone_regex = RegexValidator(
    regex=r'^\+998\d{9}$',
    message="Telefon raqam quyidagi formatda bo'lishi kerak: '+998XXXXXXXXX' (masalan, +998901234567)."
)

def validate_age(value):
    today = timezone.now().date()

    # Not in the future
    if value > today:
        raise ValidationError("Birth date cannot be in the future.")

    # Max 100 years ago
    try:
        hundred_years_ago = today.replace(year=today.year - 100)
    except ValueError:  # handle Feb 29 edge case
        hundred_years_ago = today.replace(month=2, day=28, year=today.year - 100)

    # Min 16 years ago
    try:
        sixteen_years_ago = today.replace(year=today.year - 16)
    except ValueError:
        sixteen_years_ago = today.replace(month=2, day=28, year=today.year - 16)

    if value < hundred_years_ago:
        raise ValidationError("Birth date cannot be more than 100 years ago.")
    if value > sixteen_years_ago:
        raise ValidationError("You must be at least 16 years old.")

def validate_full_name(value):
    # Split by whitespace and filter out empty strings
    parts = [p for p in value.strip().split(" ") if p]
    if len(parts) < 2:
        raise ValidationError("Please enter both first name and last name.")

def validate_email_lower(value: str):
    """Force lowercase emails."""
    if value != value.lower():
        raise ValidationError("Email must be lowercase.")


def validate_username(value: str):
    """Reject empty usernames."""
    if not value.strip():
        raise ValidationError("Username cannot be blank.")


def validate_password(value: str):
    """Ensure password is set (not blank)."""
    if not value.strip():
        raise ValidationError("Password cannot be blank.")


def validate_numeric_code(value: str):
    """Ensure value is exactly 4 digits."""
    if not re.match(r'^\d{4}$', value):
        raise ValidationError("Code must be exactly 4 digits.")

def validate_not_past(value):
    """Ensure datetime is not in the past."""
    if value < timezone.now():
        raise ValidationError("Expiration time cannot be in the past.")