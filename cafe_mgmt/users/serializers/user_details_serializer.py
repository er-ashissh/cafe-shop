from utils.date_time_util import DateTimeUtil
from django.utils.translation import gettext_lazy as _
from users.models.user_details import UserDetails
from rest_framework import serializers, validators


class UserDetailsSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        rep = super(UserDetailsSerializer, self).to_representation(instance)
        rep['full_name'] = instance.get_full_name()
        return rep

    class Meta:
        model = UserDetails
        fields = "__all__"
        extra_kwargs = {
            'first_name': {
                'error_messages': {
                    'required': 'is required!',
                    'null': 'can\'t be null!',
                    'blank': 'can\'t be blank!'
                }
            },
            'last_name': {
                'error_messages': {
                    'required': 'is required!',
                    'null': 'can\'t be null!',
                    'blank': 'can\'t be blank!'
                }
            },
            'email': {
                'error_messages': {
                    'required': 'is required!',
                    'null': 'can\'t be null!',
                    'blank': 'can\'t be blank!',
                    'invalid': 'must be valid!',
                    'unique': 'must be unique!',
                }
            },
            'password': {
                'write_only': True,
                'error_messages': {
                    'required': 'is required!',
                    'null': 'can\'t be null!',
                    'blank': 'can\'t be blank!'
                }
            },
            'mob_number': {
                'error_messages': {
                    'min_length': 'must be 10 digit in length!',
                    'invalid': 'must be valid!'
                }
            }
        }
