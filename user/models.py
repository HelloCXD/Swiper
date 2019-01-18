import datetime

from django.db import models

# Create your models here.
from lib.orm import ModelMixin


class User(models.Model):
    nickname = models.CharField(max_length=32, unique=True)
    phonenum = models.CharField(max_length=16, unique=True)
    sex = models.BooleanField(default=True)  # 性别，默认是True表示男
    avatar = models.CharField(max_length=256)  # 头像地址
    location = models.CharField(max_length=128)  # 位置
    birth_year = models.IntegerField(default=2000)  # 出生年
    birth_month = models.IntegerField(default=1)  # 出生月
    birth_day = models.IntegerField(default=1)  # 出生日

    # 让age函数可以通过点语法调用， 如user.age
    @property
    def age(self):
        today = datetime.date.today()
        birth_date = datetime.date(self.birth_year, self.birth_month, self.birth_day)
        ages = (today - birth_date).days // 365
        return ages

    # 重写头to_dict
    def to_dict(self):
        return {
            'uid': self.id,
            'nickname': self.nickname,
            'phonenum': self.phonenum,
            'sex': self.sex,
            'avatar': self.avatar,
            'location': self.location,
            'age': self.age
        }

    # 用户交友配置
    @property
    def profile(self):
        if not hasattr(self, '_profile'):
            self._profile = Profile.objects.get_or_create(id=self.id)
        return self._profile


# 用户的交友配置
class Profile(models.Model, ModelMixin):
    SEX = [
        ('male', '男'),
        ('female', '女'),
    ]
    dating_sex = models.CharField(max_length=16, default='female', choices=SEX, verbose_name='匹配的性别')
    location = models.CharField(max_length=32, verbose_name='目标城市')

    min_distance = models.IntegerField(default=1, verbose_name='最小交友距离')
    max_distance = models.IntegerField(default=100, verbose_name='最大交友距离')
    min_dating_age = models.IntegerField(default=18, verbose_name='最小交友年龄')
    max_dating_age = models.IntegerField(default=80, verbose_name='最大交友年龄')

    vibration = models.BooleanField(default=True, verbose_name='是否开启震动')
    only_match = models.BooleanField(default=False, verbose_name='不让匹配的人看到我的相册')
    auto_play = models.BooleanField(default=True, verbose_name='是否自动播放')







