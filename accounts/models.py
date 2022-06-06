from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager, PermissionsMixin
from django.core.mail import send_mail


class UserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('メールアドレス', unique=True)
    first_name = models.CharField('姓', max_length=30)
    last_name = models.CharField('名', max_length=30)

    is_staff = models.BooleanField(
        'staff status',
        default=False,
        help_text='ユーザーが管理サイトにログインできるかどうかを指定します。',
    )
    is_active = models.BooleanField(
        'active',
        default=True,
        help_text=(
            'このユーザーをアクティブとして扱うかどうかを指定します. '
            'アカウントを削除する際、データを残す場合は選択解除してください'
        ),
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

    @property
    def username(self):
        return self.email

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def __str__(self):  # __unicode__ in python 2.*
        return self.first_name + " " + self.last_name + " 【" + self.email + "】"


class Test(models.Model):
    text = models.CharField(max_length=255)
    retext = models.CharField(max_length=255)
    fields = models.JSONField(blank=True, null=True)
