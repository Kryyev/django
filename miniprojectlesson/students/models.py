import datetime

from django.db import models
from django.core.validators import MinLengthValidator
from .validators import valid_email_domain, ValidEmailDomain

VALID_DOMAIN_LIST = ['@gmail.com', '@icloud.com'
]

class Student(models.Model):
    first_name = models.CharField(max_length=30,
                                  verbose_name='Имя',
                                  db_column='first name',
                                  validators=[MinLengthValidator(3, 'First name can not be less than 3 symbols ')])
    last_name = models.CharField(max_length=30,
                                 verbose_name='Фамилия',
                                 db_column='last name',
                                 validators=[MinLengthValidator(3, 'Last name can not be less than 3 symbols')])
    birthday = models.DateField(default=datetime.datetime.today, null=True, blank=True)

    #email = models.EmailField(validators=[valid_email_domain])
    email = models.EmailField(validators=[ValidEmailDomain(VALID_DOMAIN_LIST)])

    def clean_fields(self, exclude=None):
        return

st = Student
st()


# class Meta:
#     db_table = 'Student'