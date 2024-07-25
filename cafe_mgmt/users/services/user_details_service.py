from users.models.user_details import UserDetails
from users.serializers.user_details_serializer import UserDetailsSerializer


class UserDetailsService:

    '''
    Create UserDetails
    @request: dict request_data
    @response: int user_details_id
    '''
    def create(request_data):
        serializer = UserDetailsSerializer(data=request_data)
        if serializer.is_valid(raise_exception=True):
            return (serializer.save()).id


    '''
    Update a user_details
    @request: dict request_data, int user_details_id
    @response: int user_details_id
    '''
    def update(request_data, id):
        user_details_object = UserDetails.objects.get(id=id)
        serializer = UserDetailsSerializer(user_details_object, data=request_data)
        if serializer.is_valid(raise_exception=True):
            return (serializer.save()).id


    '''
    Partial update a user_details
    @request: dict request_data, int user_details_id
    @response: int user_details_id
    '''
    def partial_update(request_data, id):
        user_details_object = UserDetails.objects.get(id=id)
        serializer = UserDetailsSerializer(user_details_object, data=request_data, partial=True)
        if serializer.is_valid(raise_exception=True):
            return (serializer.save()).id


    '''
    Get list of a user_details
    @request: request
    @response: object queryset, json serializer
    '''
    def get_list(request):
        queryset = FilterPagination.filter_and_pagination(request, UserDetails)
        serializer = UserDetailsSerializer(queryset['queryset'], many=True).data
        return queryset, serializer


    '''
    Get detail of a user_details by ID
    @request: int user_details_id
    @response: dict user_details_detail
    '''
    def get_detail(id):
        user_details_object = UserDetails.objects.get(id=id, status=StatusBase.ACTIVE)
        serializer = UserDetailsSerializer(user_details_object)
        return serializer.data


    '''
    Delete user_details detail by ID
    @request: int user_details_id
    @response: boolean True
    '''
    def delete(id):
        user_details_object = UserDetails.objects.get(id=id)
        user_details_object.delete()
        return True


    '''
    Fetch listing user_details data 
    @request: list ids, list field_list
    @response: list response
    '''
    def fetch_listing_user_details_data(ids, field_list):
        user_details_ids = sorted(ids)
        user_details_object = UserDetails.objects.filter(id__in=user_details_ids).values(*field_list)
        return (list(user_details_object))
