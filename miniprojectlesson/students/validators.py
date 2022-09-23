# icloud.com, gmail.com
from prompt_toolkit.validation import ValidationError


def valid_email_domain(value):
    valid_domain = ['@gmail.com', '@icloud.com']
    for domain in valid_domain:
        if domain in value:
            break
    else:
        raise ValidationError(f'Email {value} is incorrect')

class ValidEmailDomain:
    def __int__(self, *domains):
        self.domains = list(domains)

    def __call__(self, *args, **kwargs):
        for domain in self.domains:
            if args[0].endswith(domain):
                break
        else:
            raise ValidationError(f'Invalid email! Domain {args[0].split("@")[1]} not valid')