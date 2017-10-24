from rest_framework import serializers
from autoinput.models import W2
import ast

__all__ = ('W2Serializer', 'W2Serializer2')


class W2Serializer(serializers.ModelSerializer):

    class Meta:
        model = W2
        fields = '__all__'


class W2Serializer2(serializers.ModelSerializer):
    results = serializers.SerializerMethodField()
    img_size = serializers.SerializerMethodField()

    class Meta:
        model = W2
        fields = ('id', 'img', 'img_size', 'source_doc', 'order', 'results')

    def get_img_size(self, obj):
        img = obj.img
        return img.size

    def get_results(self, obj):
        w2 = W2.objects.filter(pk=obj.pk)[0]
        results = []
        queue = ["", "ssn", "", "ein", "wage", "federal_income", ["employer_name",
                 "employer_street", "employer_zip","employer_city","employer_state"]
                ,"social_security_wages", "social_security_tax","medicare_wages",
                "medicare_tax", "social_security_tips", "allocated_tips",
                "control_number","", "dependent_care_benefits", ["employee_first_name",
                "employee_last_name", "employee_zip_code", "employee_state", "employee_city"],
                "non_qualified_plans", "box12a", "box13_se", "box13_rp", "box13_tpsp",
                "box12b", "box12c", ["box14_type", "box14_amount"], "box12d","",
                 ["employer_state2", "employer_state_id"], "state_wages", "state_tax", "locality_name",
                "local_wages", "local_tax"]
        coordinate_index = 0
        index = 0
        cut_start_points = ast.literal_eval(w2.cut_start_points)
        cut_end_points = ast.literal_eval(w2.cut_end_points)
        while(coordinate_index < len(cut_start_points)):
            data = {}
            start_x = cut_start_points[coordinate_index][1]
            start_y = cut_start_points[coordinate_index][0]
            end_x = cut_end_points[coordinate_index][1]
            end_y = cut_end_points[coordinate_index][0]
            width = end_x - start_x
            height = end_y - start_y
            name = queue[coordinate_index]

            if name == "":
                coordinate_index += 1
                continue
            if type(name) == list:
                for dic_index, key in enumerate(name):
                    data['height'] = height
                    data['width'] = width
                    data['x'] = start_x
                    data['y'] = start_y
                    data['name'] = key
                    data['index'] = index
                    data['value'] = getattr(w2, data['name'])
                    # data['value'] =
                    results.append(data)
                    data = {}
                    index += 1
            else:
                data['height'] = height
                data['width'] = width
                data['x'] = start_x
                data['y'] = start_y
                data['index'] = index
                data['name'] = queue[coordinate_index]
                if data['name'] == "":
                    continue
                data['value'] = getattr(w2, data['name'])
                results.append(data)
                index += 1
            coordinate_index += 1

        return results


#     cut_start_points = models.TextField(blank=True)
#     cut_end_points = models.TextField(blank=True)
#     ssn = models.CharField(max_length=50, blank=True)
#     ein = models.CharField(max_length=50, blank=True)
#     wage = models.CharField(max_length=50, blank=True)
#     federal_income = models.CharField(max_length=50, blank=True)
#     employer_name = models.CharField(max_length=50, blank=True)
#     employer_street = models.CharField(max_length=50, blank=True)
#     employer_zip = models.CharField(max_length=50, blank=True)
#     employer_city = models.CharField(max_length=50, blank=True)
#     employer_state = models.CharField(max_length=50, blank=True)
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
#     employee_city = models.CharField(max_length=50, blank=True)
#     employer_state2 = models.CharField(max_length=50, blank=True)
#     employer_state_id = models.CharField(max_length=50, blank=True)
#     non_qualified_plans = models.CharField(max_length=50, blank=True)
#     box12a = models.CharField(max_length=50, blank=True)
#     box13_se = models.CharField(max_length=50, blank=True)
#     box13_rp = models.CharField(max_length=50, blank=True)
#     box13_tpsp = models.CharField(max_length=50, blank=True)
#     box12b = models.CharField(max_length=50, blank=True)
#     box12c = models.CharField(max_length=50, blank=True)
#     box14_type = models.CharField(max_length=50, blank=True)
#     box14_amount = models.CharField(max_length=50, blank=True)
#     box12d = models.CharField(max_length=50, blank=True)
#     employer_state2 = models.CharField(max_length=50, blank=True)
#     employer_state_id = models.CharField(max_length=50, blank=True)
#     state_wages = models.CharField(max_length=50, blank=True)
#     state_tax = models.CharField(max_length=50, blank=True)
#     locality_name = models.CharField(max_length=50, blank=True)
#     local_wages = models.CharField(max_length=50, blank=True)
#     local_tax = models.CharField(max_length=50, blank=True)