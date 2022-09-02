from django.db import models
# git commit,创建完本地模型后需要执行  python manage.py makemigrations(类似git commit)
# 会在当前应用migrations目录下生成相应记录文件
# git push,进行数据库同步 python manage.py migrate


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_data = models.DateTimeField('date published')


class Choice(models.Model):
    # 大项目里面一般不会用ForeignKey，
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)  # 不指定长度会报错
    votes = models.IntegerField(default=0)  # 投票数

