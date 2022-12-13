from transformers import pipeline

from model import Model


class Ner(Model):
    def __init__(self, model):
        self.__pipeline = pipeline("token-classification",
                                   model=model,
                                   aggregation_strategy="simple")

    def get_raw_result(self, request):
        return self.__pipeline(request)

    def get_json_result(self, request):
        result = self.get_raw_result(request)
        for e in result:
            e['score'] = float(str(e['score']))
        return result
