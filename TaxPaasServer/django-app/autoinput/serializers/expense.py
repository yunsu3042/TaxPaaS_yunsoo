from rest_framework import serializers
import ast
from autoinput.models import Ten99INT, Ten99DIV, Ten99G, Ten99MISC, \
    Ten99Mortgage, Ten98EStudentLoanInterest, ChildCare
from autoinput.models import W2

__all__ = ('Ten99INTSerializer', 'Ten99INTSerializer2', 'Ten99DIVSerializer',
           'Ten99DIVSerializer2', 'Ten99GSerializer', 'Ten99MISCSerializer',
           'Ten99MortgageSerializer','Ten98EStudentLoanInterestSerializer',
           'ChildCareSerializer')


class Ten99INTSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ten99INT
        fields = '__all__'


class Ten99INTSerializer2(serializers.ModelSerializer):
    results = serializers.SerializerMethodField()

    class Meta:
        model = Ten99INT
        fields = ('id', 'img', 'source_doc', 'order', 'results')

    def get_results(self, obj):
        int_obj = Ten99INT.objects.filter(pk=obj.pk)[0]
        results = []
        queue = [["payer_name", "street_address", "city", "state", "zip_code"],
                 "payer_rtn", "", "", "interest_income",
                 "early_withdrawal_penalty", "",
                 "payer_federal_in", "recipient_in",
                 "interest_us_saving_bonds",
                 ["recipient_first_name", "recipient_last_name",
                  "street_address", "city_check", "state_check",
                  "zip_code_check"], "federal_income_tax",
                 "investment_expenses",
                 "foreign_tax_paid", "foreign_country_us_possession",
                 "tax_exempt_interest", "specified_private_bond",
                 "market_discount", "bond_premium", "", "fatca_filling",
                 "", "bond_premium_tax_exempt", "account_number",
                 "tax_exempt_tax_credit",
                 "state_recheck", "state_in", "state_tax"
                 ]
        coordinate_index = 0
        index = 0
        try:
            cut_start_points = ast.literal_eval(int_obj.cut_start_points)
            cut_end_points = ast.literal_eval(int_obj.cut_end_points)
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
                    data['value'] = getattr(int_obj, data['name'])
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
                data['value'] = getattr(int_obj, data['name'])
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


class Ten99DIVSerializer2(serializers.ModelSerializer):
    results = serializers.SerializerMethodField()

    class Meta:
        model = Ten99DIV
        fields = ('id', 'img', 'source_doc', 'order', 'results')

    def get_results(self, obj):
        div = Ten99DIV.objects.filter(pk=obj.pk)[0]
        results = []
        queue = [
            ['payer_name', 'street_address', 'city', 'state', 'zip_code'],
            'total_ordinary_dividends',  '', '', 'qualified_dividends',
            'total_capital_gain_distr', 'unrecap', '', "payer_federal_in",
            "recipient_in", 'section_1202_gain', 'collectibles_gain',
            ['recipient_first_name', 'recipient_last_name'],
            "nondividend_distributions", "federal_income_tax",
            "street_address_recheck", "", "investment_expense",
            ["city_check", "state_check", "zip_code_check"], "foreign_tax",
            "foreign_country_possession", "", "fatca_filling",
            "cash_liquidation_distributions",
            "noncash_liquidation_distributions", "account_number", "",
            "exempt_interest_dividends", "specified_private_activity_bond", "",
            "", "state_recheck", "state_in", "state_tax"
        ]

        coordinate_index = 0
        index = 0
        try:
            cut_start_points = ast.literal_eval(div.cut_start_points)
            cut_end_points = ast.literal_eval(div.cut_end_points)
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
                    data['value'] = getattr(div, data['name'])
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
                data['value'] = getattr(div, data['name'])
                if data['value'] == "[]":
                    data['value'] = ""
                results.append(data)
                index += 1
            coordinate_index += 1
        return results



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
