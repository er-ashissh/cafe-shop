from users.models.user_details import UserDetails
from utils.validations.base_api_request_validation import \
    BaseApiRequestValidation
from utils.validations.request_validation import RequestValidation


class UserDetailsValidation(BaseApiRequestValidation):

    def login_validate(params):
        required_fields = ['email', 'password']
        RequestValidation.required_fields_validate(params, required_fields)
        email_exist = UserDetails.objects.filter(email=params.get("email"))
        if email_exist:
            password_exist = email_exist.filter(password=params.get("password"))
            if password_exist:
                acc_is_enable = password_exist.filter(status=UserDetails.StautsType.ENABLE)
                if not acc_is_enable:
                    BaseApiRequestValidation.set_error('email', 'Your account is not active!!')
            else:
                BaseApiRequestValidation.set_error('password', 'Invalid password!!')
        else:
            BaseApiRequestValidation.set_error('email', 'Invalid email id!!')