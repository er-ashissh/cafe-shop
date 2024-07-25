
from django.core.exceptions import ValidationError
from login.validation.super_check_validation import SuperCheckValidation


'''
Used in Model Field Validation
'''
class FieldValidation:

    def first_name_validate(value):
        is_valid = SuperCheckValidation.first_name_check(value)
        if is_valid:
            raise ValidationError(is_valid)


    def email_validate(value):
        is_valid = SuperCheckValidation.email_check(value)
        if is_valid:
            raise ValidationError(is_valid)


    def password_check(value):
        if value and len(value) < 13:
            is_valid = SuperCheckValidation.password_check(value)
            if is_valid:
                raise ValidationError(is_valid)


    def dial_code_validate(value):
        dial_code_list = ['+91', '+93', '+355', '+213', '+1']
        if (value not in dial_code_list):
            raise ValidationError('invalid dial code!')


    def contact_number_validate(value):
        is_valid = SuperCheckValidation.contact_number_check(value)
        if is_valid:
            raise ValidationError(is_valid)