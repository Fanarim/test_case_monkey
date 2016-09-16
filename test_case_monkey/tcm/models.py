from django.db import models


class Organisation(models.Model):
    name = models.CharField(max_length=50,
                            primary_key=True)


class Project(models.Model):
    name = models.CharField(max_length=50,
                            primary_key=True)
    description = models.TextField()
    organisation = models.ForeignKey(Organisation,
                                     on_delete=models.CASCADE,
                                     related_name='projects')


class TestRun(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True)
    results_due_date = models.DateTimeField(null=True)
    finished = models.BooleanField()
    author = models.CharField(max_length=50)  # TODO use real username


class TestScenarioBase(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    class Meta:
        abstract = True


class TestScenarioTemplate(TestScenarioBase):
    project = models.ForeignKey(Project,
                                on_delete=models.CASCADE,
                                related_name='scenarios')


class TestScenario(TestScenarioBase):
    based_on = models.ForeignKey(TestScenarioTemplate,
                                 null=True,
                                 related_name='scenarios')
    test_run = models.ForeignKey(TestRun,
                                 on_delete=models.CASCADE,
                                 related_name='scenarios')
    asignee = models.CharField(max_length=50)  # TODO use real username


class TestScenarioAttributesBase(models.Model):
    DATATYPE_OPTIONS = (
        ('SB', 'Select box'),
        ('TX', 'Text'),
    )

    key = models.CharField(max_length=50)
    datatype = models.CharField(max_length=2, choices=DATATYPE_OPTIONS)
    value = models.TextField()

    class Meta:
        abstract = True


class TestScenarioTemplateAttributes(TestScenarioAttributesBase):
    pass


class TestScenarioAttributes(TestScenarioAttributesBase):
    pass


class TestCaseBase(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    expected_result = models.TextField(null=True)

    class Meta:
        abstract = True


class TestCaseTemplate(TestCaseBase):
    scenario = models.ForeignKey(TestScenarioTemplate,
                                 on_delete=models.CASCADE,
                                 related_name='templates')


class TestCase(TestCaseBase):
    STATUS_OPTIONS = (
        ('PASS', 'PASS'),
        ('FAIL', 'FAIL'),
        ('SKIP', 'SKIP'),
    )
    scenario = models.ForeignKey(TestScenario,
                                 on_delete=models.CASCADE,
                                 related_name='testcases')
    result_status = models.CharField(choices=STATUS_OPTIONS,
                                     default='PASS',
                                     null=True,
                                     max_length=4)
    result = models.TextField(null=True)
    based_on = models.ForeignKey(TestCaseTemplate,
                                 null=True,
                                 related_name='testcases')


class Bugs(models.Model):
    STATUS_OPTIONS = (
        ('CL', 'CLOSED'),
        ('OP', 'OPEN'),
    )

    subject = models.CharField(max_length=150)
    status = models.CharField(choices=STATUS_OPTIONS,
                              max_length=2)
    status_verbose = models.CharField(max_length=50)
    testcase_template = models.ForeignKey(TestCaseTemplate)
