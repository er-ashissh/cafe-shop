from django.core.exceptions import ValidationError
from django.core.files.images import get_image_dimensions
from django.core.files.uploadedfile import UploadedFile
from django.db.models.fields.files import ImageFieldFile
from utils.response.api_response import ApiResponse
from utils.validation.base_api_request_validation import BaseApiRequestValidation
from utils.validation.request_validation import RequestValidation
import csv, io


class FileValidation:

    def download_file_validation(request_data):
        flag = False
        msg = None

        if ('ids' not in request_data) or (('ids' in request_data) and (not request_data['ids'])) or (request_data['ids'][0] is 0 or ''):
            flag = True
            msg = ['ID\'s required!!']

        if (not flag) and (len(request_data['ids']) > 20):
            flag = True
            msg = ['ID\'s must be less than 20!!']

        if flag:
            BaseApiRequestValidation.set_error(None, msg)


    '''
    Image File Validation
    '''
    def validate_image(image):
        # allowed_extention = ['image/jpg', 'image/jpeg', 'image/png', 'image/gif']
        # if image.content_type not in allowed_extention:
        #     raise ValidationError("Upload valid image!")

        # width, height = get_image_dimensions(image)
        # if width != height:
        #     raise ValidationError("Image must be square in dimention!")

        # file_size = image.size
        # limit_mb = 2
        # if file_size > (limit_mb * 1024 * 1024):
        #     raise ValidationError("Max size of file is %s MB" % limit_mb)

        '''TRY_2'''
        if image and isinstance(image, UploadedFile):
            w, h = get_image_dimensions(image)

            if w != h:
                raise ValidationError("Image must be square in dimention!!")
            
            max_width = max_height = 2000
            if w >= max_width or h >= max_height:
                raise ValidationError(u'Please use an image that is %s x %s pixels or less.' % (max_width, max_height))

            main, sub = image.content_type.split('/')
            if not (main == 'image' and sub in ['jpg', 'jpeg', 'gif', 'png']):
                raise ValidationError(u'Please use a JPEG, GIF or PNG image.')

            if len(image) > (2 * 1024 * 1024):
                raise ValidationError(u'Image file size may not exceed 2MB.')

        elif image and isinstance(image, ImageFieldFile):
            # something
            pass

        else:
            raise ValidationError(u'File must be image.')

        return image
        

    ''' Request has CSV Validate '''
    def request_has_file_validate(request, file_name):
        if file_name not in request.FILES:
            BaseApiRequestValidation.set_error('Select CSV file to upload!!')


    ''' Upload File has CSV extension Validation '''
    def has_csv_extension_validate(upload_file):
        if 'text/csv' != upload_file.content_type:
            BaseApiRequestValidation.set_error('Only CSV file upload or allowed!!')


    ''' Upload CSV File has empty/blank '''
    def csv_has_empty(upload_file):
        if 2 > upload_file.size:
            BaseApiRequestValidation.set_error('Uploaded CSV file can\'t be empty!!')


    ''' Upload CSV File has must be lesstahn in 200 KB '''
    def csv_has_lessthan_twohundred_kb(upload_file):
        if 200000 < upload_file.size:
            BaseApiRequestValidation.set_error('Uploaded CSV file must be lessthan in 200 KB!!')


    ''' Upload CSV File has data except header '''
    def csv_has_data_except_header(datasets):
        if not datasets:
            BaseApiRequestValidation.set_error('Must hava a data in CSV file!!')


    ''' Upload CSV File has Valid Number of Rows '''
    def csv_has_row_in_limit(datasets):
        if 200 < len(datasets):
            BaseApiRequestValidation.set_error('Uploaded CSV must be have lessthan 200 rows of data!!')
