from django.db import models

from schedule.models import Course


class Call(models.Model):
    class Meta:
        verbose_name_plural = 'Заявки на звонки'
        verbose_name = 'Заявка'

    course = models.ForeignKey(Course, verbose_name='Курс', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name='Имя')
    email = models.EmailField(null=True, blank=True, verbose_name='Email')
    phone = models.CharField(verbose_name='Номер телефона', max_length=64)
    message = models.TextField(verbose_name='Сообщение', null=True, blank=True)
    is_agree = models.BooleanField(
        verbose_name='Ознокомолен', default=False,
        help_text='Отмечено если с политикой конфидецияальности ознакомлен')
    created_at = models.DateTimeField(verbose_name='Создано', auto_now_add=True, null=True)
    updated_at = models.DateTimeField(verbose_name='Обнавлено', auto_now=True, null=True)

    def __str__(self):
        return '{} - {}'.format(self.id, self.name)
