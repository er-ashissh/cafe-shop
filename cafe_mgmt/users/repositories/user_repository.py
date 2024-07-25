from django.conf import settings
from rest_framework import status as http_status
from users.models.user_details import UserDetails
from users.services.user_details_service import UserDetailsService
from utils.api_response_util import ApiResponse, ApiResponseStatus
import uuid


class UserRepository:
    
    def register(request):
        '''
        Register a User
        @request: request
        @response: dict api_status
        '''
        status_code, status, msg, data = http_status.HTTP_400_BAD_REQUEST, ApiResponseStatus.ERROR, [
            'Invalid request!'], None

        # -> Create User Activation Link..
        _activation_slug = str(uuid.uuid4())
        request.data.update({
            "activation_slug": _activation_slug
        })

        result = UserDetailsService.create(request.data)
        if result:
            status_code = http_status.HTTP_200_OK
            status = ApiResponseStatus.SUCCESS
            msg = ['User register successfully.']
            data = {
                "user_id": result,
                "activation_link": f"{settings.APPN_HOST}/users/activation/?email={request.data.get('email')}&activation_slug={_activation_slug}"
            }
        else:
            msg = ['User registration failed!!']

        return ApiResponse.api_status(status_code=status_code, status=status, message=msg, data=data)


    def activation(request):
        '''
        Activate a User
        @request: request
        @response: dict api_status
        '''
        status_code, status, msg, data = http_status.HTTP_400_BAD_REQUEST, ApiResponseStatus.ERROR, [
            'Invalid request!'], None

        # -> Activate User by checking Activation-slug..
        _email = request.GET.get("email")
        _activation_slug = request.GET.get("activation_slug")
        user_details_obj = UserDetails.objects.filter(email=_email, activation_slug=_activation_slug).first()
        if user_details_obj:
            req_data = {"status": UserDetails.StautsType.ENABLE}
            result = UserDetailsService.partial_update(req_data, user_details_obj.id)
            if result:
                status_code = http_status.HTTP_200_OK
                status = ApiResponseStatus.SUCCESS
                msg = ['User Activated successfully.']
                data = {"user_id": result}
        else:
            msg = ['Invalid activation-link!!']

        return ApiResponse.api_status(status_code=status_code, status=status, message=msg, data=data)


    def login(request):
        '''
        Login a User
        @request: request
        @response: dict api_status
        '''
        status_code, status, msg, data = http_status.HTTP_400_BAD_REQUEST, ApiResponseStatus.ERROR, [
            'Invalid request!'], None

        # -> Check User login Credentials..
        _email = request.data.get("email")
        _pwd = request.data.get("password")
        result = UserDetails.objects.filter(email=_email, password=_pwd, status=UserDetails.StautsType.ENABLE).first()
        if result:
            status_code = http_status.HTTP_200_OK
            status = ApiResponseStatus.SUCCESS
            msg = ['User logged-in successfully.']
            data = {"user_id": result.id}
        else:
            msg = ['Invalid login credentials!!']

        return ApiResponse.api_status(status_code=status_code, status=status, message=msg, data=data)
