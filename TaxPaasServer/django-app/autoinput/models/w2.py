from django.db import models

__all__ = ('W2', )


class W2(models.Model):
    img = models.ImageField(upload_to="w2")
    source_doc = models.ForeignKey('autoinput.SourceDoc', blank=True,
                                   null=True)
    order = models.IntegerField(default=0)
    auto_start = models.BooleanField(default=False)
    ssn = models.CharField(max_length=50, blank=True)
    ein = models.CharField(max_length=50, blank=True)
    wage = models.CharField(max_length=20, blank=True)
    federal_income = models.CharField(max_length=20, blank=True)
    name = models.CharField(max_length=150, blank=True)
    ss_wages = models.CharField(max_length=30, blank=True)
    ss_tax = models.CharField(max_length=30, blank=True)
    medicare_wages = models.CharField(max_length=30, blank=True)
    medicare_tax = models.CharField(max_length=30, blank=True)
    ss_tips = models.CharField(max_length=30, blank=True)
    all_tips = models.CharField(max_length=30, blank=True)
    control_number = models.CharField(max_length=30, blank=True)
    dp_care_benefits = models.CharField(max_length=30, blank=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    zip_code = models.CharField(max_length=30, blank=True)
    nq_plans = models.CharField(max_length=30, blank=True)
    box12a = models.CharField(max_length=30, blank=True)
    box12b = models.CharField(max_length=30, blank=True)
    box12c = models.CharField(max_length=30, blank=True)
    box12d = models.CharField(max_length=30, blank=True)
    st_employee = models.CharField(max_length=30, blank=True)
    retire_plan = models.CharField(max_length=30, blank=True)
    tp_sick_pay = models.CharField(max_length=30, blank=True)
    other = models.CharField(max_length=30, blank=True)
    state = models.CharField(max_length=30, blank=True)
    st_id_number = models.CharField(max_length=30, blank=True)
    st_wages = models.CharField(max_length=30, blank=True)
    st_tax = models.CharField(max_length=30, blank=True)
    locality_name = models.CharField(max_length=30, blank=True)
    lc_wages = models.CharField(max_length=30, blank=True)
    lc_tax = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return "w2"
