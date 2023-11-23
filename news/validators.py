

from django.core.exceptions import ValidationError


def validate_not_single_word(value):
    if value is None:
        raise ValidationError("Este campo não pode estar vazio.")
    words = value.split()
    if len(words) == 1:
        raise ValidationError("O título deve conter pelo menos 2 palavras.")


def validate_date(value):
    if value is None:
        raise ValidationError("A data não pode ser nula.")
    if not value.strftime('%Y-%m-%d') == value.isoformat():
        raise ValidationError('O valor “invalid_date” tem um formato de data'
                              ' inválido. Deve ser no formato  YYYY-MM-DD.')


def validate_content(value):
    if value is None:
        raise ValidationError("Este campo não pode estar vazio.")
