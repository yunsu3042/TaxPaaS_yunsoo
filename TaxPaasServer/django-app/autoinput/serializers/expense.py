from rest_framework import serializers

from autoinput.models import Ten99INT, Ten99DIV, Ten99G, Ten99MISC, \
    Ten99Mortgage, Ten98EStudentLoanInterest, ChildCare

__all__ = ('Ten99INTSerializer', 'Ten99DIVSerializer', 'Ten99GSerializer',
           'Ten99MISCSerializer', 'Ten99MortgageSerializer',
           'Ten98EStudentLoanInterestSerializer','ChildCareSerializer')


class Ten99INTSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ten99INT
        fields = '__all__'

class Ten99INTSerializer2(serializers.ModelSerializer):
    results = serializers.SerializerMethodField()

    class Meta:
        model = Ten99INT
        fields= ('id', 'img', 'source_doc', 'order', 'results')

    def get_results(self, obj):
        pass


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
        try:
            cut_start_points = ast.literal_eval(w2.cut_start_points)
            cut_end_points = ast.literal_eval(w2.cut_end_points)
        except:
            return {"status": "not finished"}
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
                    if data['value'] == "[]":
                        data['value'] = ""
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
                if data['value'] == "[]":
                    data['value'] = ""
                results.append(data)
                index += 1
            coordinate_index += 1
        return results







class Ten99DIVSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ten99DIV
        fields = '__all__'


class Ten99GSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ten99G
        fields = '__all__'


class Ten99MISCSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ten99MISC
        fields = '__all__'


class Ten99MortgageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ten99Mortgage
        fields = '__all__'


class Ten98EStudentLoanInterestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ten98EStudentLoanInterest
        fields = '__all__'


class ChildCareSerializer(serializers.ModelSerializer):

    class Meta:
        model = ChildCare
        fields = '__all__'
