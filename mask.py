from transformers import pipeline

from model import Model


class Mask(Model):
    def __init__(self, model, tokenizer):
        self.__pipeline = pipeline("fill-mask",
                                   model=model,
                                   tokenizer=tokenizer)

    def get_raw_result(self, request, top_k=5):
        return self.__pipeline(request, top_k=top_k)

    def get_json_result(self, request, top_k=5):
        return self.get_raw_result(request, top_k=top_k)
