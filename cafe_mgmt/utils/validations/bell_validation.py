# from customers.validations.customer_address_validation import CustomerAddressValidation
# from customers.validations.customer_validation import CustomerValidation

from django.core.exceptions import ValidationError
from utils.validations.base_api_request_validation import BaseApiRequestValidation
import importlib


class BellValidation:

    '''
    Note:
    - need to add `self` keyword in every validation function at 1st positon
    '''

    @staticmethod
    def get_module(cls_name):
        module_dict = {
            'CustomerAddressValidation': 'customers.validations.customer_address_validation',
            'CustomerValidation': 'customers.validations.customer_validation',
        }
        return module_dict[cls_name]


    @staticmethod
    def check_has_error():
        has_error = BaseApiRequestValidation.get_error()
        if has_error:
            raise ValidationError(has_error)


    '''
    Bulk Validation Process
    # ---IN-CALLER---
    validation_dict = {
            'CustomerValidation': {
                'customer_is_exist': {'id': id},
                'customer_is_exist_without_status': {'id': id}
            },
            # 'check': 'true',
            # 'CustomerValidation': {
            #     'customer_is_exist': {'id': 42424},
            #     'customer_is_exist_without_status': {'id': id}
            # }
        }
        # Validation Bell
        BellValidation.validate(validation_dict)
    
    # ---IN-CALLEE--
    def validate(params):
        BaseApiRequestValidation.clear_error()

        for k1, v1 in params.items():
            if 'check' == k1:
                BellValidation.check_has_error()
            else:
                module = importlib.import_module(BellValidation.get_module(k1))
                instance = getattr(module, k1)()
                for k2, v2 in v1.items():
                    # k1.k2(v2)
                    getattr(instance, k2)(**v2)

        BellValidation.check_has_error()
    '''