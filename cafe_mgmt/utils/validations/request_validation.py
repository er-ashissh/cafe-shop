from utils.validations.base_api_request_validation import BaseApiRequestValidation


class RequestValidation(BaseApiRequestValidation):

    '''
    Required Field in Request(request.data) validate 
    @params: params dict, required_fields list
    @return: None
    '''
    def required_fields_validate(params: dict, required_fields: list):
        params_keys = list(params.keys())
        for required_field in required_fields:
            if (required_field not in params_keys) or ((isinstance(params[required_field], str)) and (not params[required_field].strip())):
                BaseApiRequestValidation.set_error(required_field, 'field required!!')


    '''
    Restricted Field in Request(request.data) validate 
    @params: params dict, restricted_fields list
    @return: None
    '''
    def restricted_fields_validate(params: dict, restricted_fields: list):
        params_keys = list(params.keys())
        for restricted_field in restricted_fields:
            if (restricted_field in params_keys):
                BaseApiRequestValidation.set_error(restricted_field, 'field not allowed in request!!')

