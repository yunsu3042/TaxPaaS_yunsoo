from rest_framework import serializers
from autoinput.models import W2
import ast

__all__ = ('W2Serializer', )


class W2Serializer(serializers.ModelSerializer):

    class Meta:
        model = W2
        fields = '__all__'
#
#
# class W2Serializer2(serializers.ModelSerializer):
#     results = serializers.SerializerMethodField()
#
#
#     class Meta:
#         model = W2
#         fields = ('id', 'img', 'source_doc', 'order', 'results')
#
#     def get_results(self, obj):
#         w2 = W2.objects.filter(pk=obj.pk)[0]
#         context = {}
#         results = []
#         w2.cut_start_points
#         w2.cut_end_points
#
#         queue = ["ssn", "ein", "wage", "federal_income", "social_security_wages", "social_security_tax", ""]
#         for i, (y, x) in enumerate(ast.literal_eval(w2.cut_start_points)):
#             for end_y, end_x in ast.literal_eval(w2.cut_end_points):
#                 width = end_x - x
#                 height = end_y - y
#                 data = {}
#                 data['height'] = height
#                 data['width'] = width
#                 data['index'] = i + 1
#
#                 results.append({"index": , "name": , "x": , "y": , "width": , "height"})
#
#
#
#     cut_start_points = models.TextField(blank=True)
#     cut_end_points = models.TextField(blank=True)
#     ssn = models.CharField(max_length=50, blank=True)
#     ein = models.CharField(max_length=50, blank=True)
#     wage = models.CharField(max_length=50, blank=True)
#     federal_income = models.CharField(max_length=50, blank=True)
#     social_security_wages = models.CharField(max_length=50, blank=True)
#     social_security_tax = models.CharField(max_length=50, blank=True)
#     medicare_wages = models.CharField(max_length=50, blank=True)
#     medicare_tax = models.CharField(max_length=50, blank=True)
#     social_security_tips = models.CharField(max_length=50, blank=True)
#     allocated_tips = models.CharField(max_length=50, blank=True)
#     control_number = models.CharField(max_length=50, blank=True)
#     dependent_care_benefits = models.CharField(max_length=50, blank=True)
#     employee_first_name = models.CharField(max_length=50, blank=True)
#     employee_last_name = models.CharField(max_length=50, blank=True)
#     employee_zip_code = models.CharField(max_length=50, blank=True)
#     employee_state = models.CharField(max_length=50, blank=True)
#     employer_name = models.CharField(max_length=50, blank=True)
#     employer_city = models.CharField(max_length=50, blank=True)
#     employer_state = models.CharField(max_length=50, blank=True)
#     employer_street = models.CharField(max_length=50, blank=True)
#     employer_zip = models.CharField(max_length=50, blank=True)
#     employer_state2 = models.CharField(max_length=50, blank=True)
#     employer_state_id = models.CharField(max_length=50, blank=True)
#     non_qualified_plans = models.CharField(max_length=50, blank=True)
#     box12a = models.CharField(max_length=50, blank=True)
#     box12b = models.CharField(max_length=50, blank=True)
#     box12c = models.CharField(max_length=50, blank=True)
#     box12d = models.CharField(max_length=50, blank=True)
#     box13_se = models.CharField(max_length=50, blank=True)
#     box13_rp = models.CharField(max_length=50, blank=True)
#     box13_tpsp = models.CharField(max_length=50, blank=True)
#     box14_type = models.CharField(max_length=50, blank=True)
#     box14_amount = models.CharField(max_length=50, blank=True)
#     state_wages = models.CharField(max_length=50, blank=True)
#     state_tax = models.CharField(max_length=50, blank=True)
#     locality_name = models.CharField(max_length=50, blank=True)
#     local_wages = models.CharField(max_length=50, blank=True)
#     local_tax = models.CharField(max_length=50, blank=True)