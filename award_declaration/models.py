from django.db import models

# Create your models here.
import settings


class Organization(models.Model):
    org_name = models.CharField(max_length=100, verbose_name="所属组织", db_index=True)
    principal = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name="负责人", related_name="principal")
    apply_person = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name="可申报人员", related_name="apply_person")
    operator = models.CharField(verbose_name="更新人", max_length=20)
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    update_time = models.DateTimeField(verbose_name="最后修改时间", auto_now=True)

    class Meta:
        verbose_name = "组织信息表"
        verbose_name_plural = verbose_name
        ordering = ["-create_time"]
        db_table = "award_declaration_organization"

    def __str__(self):
        return self.org_name


class ApplyStatus:
    EFFECT = 1
    EXPIRED = 0


class Award(models.Model):
    STATUS = [
        (ApplyStatus.EXPIRED, "已过期"),
        (ApplyStatus.EFFECT, "生效中"),
    ]
    AWARD_LEVEL_LIST = [(1, '中心级'), (2, '部门级'), (3, '普照奖')]
    belonging_org = models.ForeignKey(Organization, models.CASCADE)
    award_level = models.IntegerField(verbose_name="奖项级别", choices=AWARD_LEVEL_LIST)
    award_name = models.CharField(verbose_name="奖项名称", max_length=50)
    requirement = models.TextField(verbose_name="参评要求")
    status = models.IntegerField(verbose_name="申请状态", choices=STATUS, default=ApplyStatus.EFFECT)
    start_time = models.DateTimeField(verbose_name="开始时间")
    end_time = models.DateTimeField(verbose_name="结束时间")
    apply_person_num = models.IntegerField(verbose_name="申报人数", default=0)
    award_person_num = models.IntegerField(verbose_name="获奖人数", default=0)
    need_attachment = models.SmallIntegerField(verbose_name="上传附件", choices=[(1, '打开'), (0, '关闭')], default=1)
    operator = models.CharField(verbose_name="更新人", max_length=20)
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    update_time = models.DateTimeField(verbose_name="最后修改时间", auto_now=True)

    class Meta:
        verbose_name = "奖项信息表"
        verbose_name_plural = verbose_name
        ordering = ["-create_time"]
        db_table = "award_declaration_award"

    def __str__(self):
        return self.award_name