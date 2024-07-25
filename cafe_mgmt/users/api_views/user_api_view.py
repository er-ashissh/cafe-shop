from django.db import transaction
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from users.repositories.user_repository import UserRepository
from utils.api_response_util import ApiResponse
from utils.validations.bell_validation import BellValidation
from users.validations.user_details_validation import UserDetailsValidation
from utils.validations.base_api_request_validation import BaseApiRequestValidation

import logging


class UserApiView(APIView):

    @api_view(['POST'])
    @transaction.atomic
    def register(request):
        result = UserRepository.register(request)
        return ApiResponse.api_response(**result)


    @api_view(['GET'])
    @transaction.atomic
    def activation(request):
        result = UserRepository.activation(request)
        return ApiResponse.api_response(**result)


    @api_view(['POST'])
    @transaction.atomic
    def login(request):

        BaseApiRequestValidation.clear_error()
        UserDetailsValidation.login_validate(request.data)
        BellValidation.check_has_error()

        result = UserRepository.login(request)
        return ApiResponse.api_response(**result)



