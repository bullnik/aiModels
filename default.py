from model import Model


class Default(Model):

    def get_raw_result(self, request):
        return ''

    def get_json_result(self, request):
        return ''
