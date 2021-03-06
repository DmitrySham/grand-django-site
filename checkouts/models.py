from django.db import models


class Checkout(models.Model):
    class Meta:
        verbose_name_plural = 'Заказы'
        verbose_name = 'Заказ'
        ordering = ['-created_at']

    one_c = models.ForeignKey(
        to='production.OneC', related_name='checkout',
        on_delete=models.SET_NULL,
        null=True, blank=True, verbose_name='1С')
    grand_smeta = models.ForeignKey(
        to='core.GrandSmeta', related_name='checkout',
        on_delete=models.SET_NULL, null=True, blank=True,
        verbose_name='Гранд Смета')
    online_cashbox = models.ForeignKey(
        to='production.OnlineCashbox', related_name='checkout',
        on_delete=models.SET_NULL, null=True, blank=True,
        verbose_name='Онлайн кассы')
    name = models.CharField(max_length=255, verbose_name='Имя')
    email = models.EmailField(verbose_name='E-mail')
    message = models.TextField(
        verbose_name='Сообщение', null=True, blank=True)
    is_agree = models.BooleanField(
        verbose_name='Ознокомолен', default=False,
        help_text='Отмечено если с политикой конфидецияальности ознакомлен')
    created_at = models.DateTimeField(
        verbose_name='Создано', auto_now_add=True, null=True)
    updated_at = models.DateTimeField(
        verbose_name='Обнавлено', auto_now=True, null=True)

    def __str__(self):
        return '{} - {}'.format(self.id, self.name)

    @property
    def get_type(self):
        if self.one_c:
            return self.one_c.title
        elif self.grand_smeta:
            return self.grand_smeta.title
        elif self.online_cashbox:
            return self.online_cashbox.title
        return 'Нет привязки'
