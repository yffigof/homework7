from django.db import models

class Advertisement(models.Model):
    id = models.CharField('id', max_length=64, primary_key=True)
    title = models.CharField(verbose_name='заголовок', max_length=128)
    description = models.TextField('описание объявления')
    price = models.DecimalField('цена', max_digits=10, decimal_places=2)
    auction = models.BooleanField('торг', help_text='Отметьте если торг уместен')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'<Advertisement: Advertisement(id={self.id}, title={self.title}, price={self.price}>'


class Meta:
    db_table = 'advertisements'



