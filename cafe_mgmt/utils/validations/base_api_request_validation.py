

class BaseApiRequestValidation:

    '''
    error_msg_bucket = []

    def clear_error():
        BaseApiRequestValidation.error_msg_bucket = []

    def set_error(msg):
        BaseApiRequestValidation.error_msg_bucket.append(msg)

    def get_error():
        return BaseApiRequestValidation.error_msg_bucket
    '''

    error_msg_bucket = {}

    def clear_error():
        BaseApiRequestValidation.error_msg_bucket = {}

    def set_error(field_name:str, msg:str):
        field_name = field_name or 'non_field_errors'
        BaseApiRequestValidation.error_msg_bucket.setdefault(field_name, []).append(msg)

    def get_error():
        return BaseApiRequestValidation.error_msg_bucket
