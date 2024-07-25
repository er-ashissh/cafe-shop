from django.core.exceptions import ValidationError
from rest_framework.views import exception_handler
from utils.api_response_util import ApiResponse, ApiResponseStatus
import traceback


# Call REST framework's default exception handler first, 
def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    module_name = context['view'].__module__
    class_function_name = 'NA' + '-' + context['view'].__class__.__name__
    # severity_no = context['request'].session.slacknotify_severity
    severity_no = 2
    ex_msg = None
    traceback_data = traceback.format_exc()
    request_data = context['request']

    if response is None:
        if isinstance(exc, ValidationError):
            # ex_msg = ApiResponse.api_message_formatter(dict(exc), 'serializer')
            ex_msg = dict(exc)
            response = ApiResponse.api_response(status_code=400, status=ApiResponseStatus.WARNING, message=ex_msg)
        else:
            print('---custom_exception_handler---ex---', str(exc))
            print('---custom_exception_handler---traceback_data---', traceback_data)
            ex_msg = str(exc)
            response = ApiResponse.set_api_exception(module_name, class_function_name, severity_no, ex_msg, traceback_data, request_data)
    else:
        # ex_msg = ApiResponse.api_message_formatter(response.data, 'serializer')        
        ex_msg = dict(response.data)
        response = ApiResponse.api_response(status_code=400, status=ApiResponseStatus.ERROR, message=ex_msg)

    return response
