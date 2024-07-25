from utils.encode_decode_string import decode_json
from utils.date_time_util import DateTimeUtil

class ApiRequestUtil:

    def auth_toekn_isvalid(token):
        result = {"isvalid": False}
        try:
            if token:
                decode_token = decode_json(token)
                if decode_token:
                    token_valid_till = decode_token.get("token_valid_till", 0)
                    current_dt = DateTimeUtil.get_datetime_int()
                    if current_dt <= token_valid_till:
                        result.update({"token_payload": decode_token})
                        result.update({"isvalid": True})
                    else:
                        result.update({"reason": "auth-token is expired!!"})
                else:
                    result.update({"reason": "Invalid auth-token!!"})
            else:
                result.update({"reason": "auth-token is missing!!"})
        except Exception as ex:
            result.update({"reason": f"Invalid auth-token!, {ex}"})
        finally:
            return result