from django.conf import settings
from django.shortcuts import redirect
from rest_framework import status as http_status
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
# from slacknotify.services.slacknotify_service import SlacknotifyService


class ApiResponseStatus:

    WARNING = "warning"
    ERROR = "error"
    EXCEPTION = "exception"
    SUCCESS = "success"


class ApiResponse:

    ''' Use in view file '''
    def api_response(status_code=400, status=ApiResponseStatus.ERROR, message=['NA'], data=None):
        response_format = {
            'status_code': status_code,
            'status': status,  # warning / error / success
            'message': message,
            'data': data
        }
        return Response(response_format, status_code)


    ''' Use in service or other file '''
    def api_status(status_code=400, status=ApiResponseStatus.ERROR, message=['NA'], data=None):
        # message = []  # empty list
        response_format = {
            'status_code': status_code,
            'status': status,
            'message': message,
            'data': data
        }
        return response_format


    ''' Set except Exception in **View file '''
    def set_api_exception(module_name, class_fun_name, severity, ex_type, traceback, request):
        ex_data = {
            'module_name': module_name,
            'class_fun_name': class_fun_name,
            'severity': severity,
            'ex_type': ex_type,
            'traceback': traceback,
            'request': request
        }
        return ApiResponse.api_exception(data=ex_data)


    ''' Use in except Exception section '''
    def api_exception(status_code=500, status=ApiResponseStatus.EXCEPTION, message=['NA'], data=None):
        
        # if (int(settings.SLACK_POST_MESSAGE)):
        #     SlacknotifyService.send_message_to_slack_channel(data)
        
        response_format = {
            'status_code': status_code,
            'status': status,
            'message': [data['ex_type']],
            'data': None
        }
        return Response(response_format, status_code)


    ''' Use in api response message section '''
    def api_message_formatter(message, message_type):
        # print('---message---', message)
        # print('---message_type---', message_type)
        message_list = []
        message_dict = {}

        if 'serializer' == message_type:
            for k, v in message.items():
                msg_list = []
                for i in v:
                    msg_list.append(str(i))
                message_dict.update({k: msg_list})

            # Comment Bellow Chunks of Code, When you want error data in Like this format {'field_name': ['msg1', 'msg2', 'msg3']}
            for k, v in message_dict.items():
                for i in v:
                    message_list.append(k.replace('_', ' ').capitalize() + ': ' + i)

        return message_list


    ''' Use in middleware file '''
    def middleware_response(status_code=400, status=ApiResponseStatus.ERROR, message=['NA'], data=None):
        response = ApiResponse.api_response(status_code=status_code, status=status, message=message, data=data)
        response.accepted_renderer = JSONRenderer()
        response.accepted_media_type = "application/json"
        response.renderer_context = {}
        return response


    ''' 
    API or UI Return Response 
    Note: Add-on new http_code condition by http_code ascending order
    '''
    def api_or_ui_response(params, http_code):
        ret = None
        if 200 == http_code:
            if 'Postman-Token' in params:
                ret = ApiResponse.middleware_response(http_status.HTTP_200_OK, ApiResponseStatus.SUCCESS, ['All okk'], None)  # For API
            else:
                ret = redirect('/')  # For UI
        elif 401 == http_code:
            if 'Postman-Token' in params:
                ret = ApiResponse.middleware_response(http_status.HTTP_401_UNAUTHORIZED, ApiResponseStatus.WARNING, ['Login required!'], None)
            else:
                ret = redirect('/user/login/')
        elif 503 == http_code:
            if 'Postman-Token' in params:
                ret = ApiResponse.middleware_response(http_status.HTTP_503_SERVICE_UNAVAILABLE, ApiResponseStatus.ERROR, ['Website under maintenance!'], None)
            else:
                ret = redirect('/user/under-maintenance/')
        elif 1001 == http_code:
            if 'Postman-Token' in params:
                ret = ApiResponse.middleware_response(http_status.HTTP_400_BAD_REQUEST, ApiResponseStatus.ERROR, ['Login again session expired!'], None)
            else:
                ret = redirect('/user/login/')
        else:
            pass
        return ret