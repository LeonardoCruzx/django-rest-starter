from django.contrib.auth.base_user import BaseUserManager

from django.core.validators import validate_email

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Porfavor insira um email')
        email = self.normalize_email(email)
        validate_email(email)
        user = self.model(email = email,**extra_fields)
        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff',True)
        return self._create_user(email, password, **extra_fields)
