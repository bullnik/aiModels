from transformers import AutoTokenizer, BertForSequenceClassification, TextClassificationPipeline

from model import Model


class Crdc(Model):
    def __init__(self, model, tokenizer):
        tokenizer = AutoTokenizer.from_pretrained(tokenizer)
        label2id = {'common': 0, 'requirements': 1, 'duties': 2, 'conditions': 3}
        model = BertForSequenceClassification.from_pretrained(model, label2id=label2id)
        self.__pipeline = TextClassificationPipeline(model=model, tokenizer=tokenizer, top_k=None)

    def get_raw_result(self, request):
        return self.__pipeline(request)

    def get_json_result(self, request):
        label2id_list = self.get_raw_result(request)[0]
        output_dictionary = {}
        for d in label2id_list:
            if d['label'] == 'requirements':
                output_dictionary['requirements'] = d['score']
            elif d['label'] == 'common':
                output_dictionary['common'] = d['score']
            elif d['label'] == 'duties':
                output_dictionary['duties'] = d['score']
            elif d['label'] == 'conditions':
                output_dictionary['conditions'] = d['score']
        return output_dictionary
