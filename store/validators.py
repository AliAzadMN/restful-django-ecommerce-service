from django.core.exceptions import ValidationError


def validate_id_card_number(value):
    if not (value.isdigit() and len(value) == 10):
        return ValidationError(
            "Invalid ID CARD Number! Please Enter a valid ID CARD Number (10-Digits)"
        )
        