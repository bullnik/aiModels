import os
from transformers import pipeline
from transformers import AutoModelForMaskedLM, AutoTokenizer
from transformers import BertForSequenceClassification
from transformers import TextClassificationPipeline

from crdc import Crdc
from default import Default
from ner import Ner
from mask import Mask


def list_full_paths(directory):
    return [os.path.join(directory, file) for file in os.listdir(directory)]


class Models:
    def __init__(self, path='C:\Documents\Projects\Jupyter\models'):
        self.__models = {'default': Default()}
        self.__path_to_models_folder = path
        self.__tokenizer_model = "DeepPavlov/rubert-base-cased"

    def get_model(self, group, name):
        path = f"{self.__path_to_models_folder}\\{group}\\{name}"
        if not os.path.exists(f'{path}\\config.json'):
            return self.__models['default']

        abspath = os.path.abspath(path)
        if not abspath.startswith(self.__path_to_models_folder):
            return self.__models['default']

        if abspath in self.__models:
            return self.__models[abspath]

        if group == 'mask':
            self.__models[abspath] = Mask(abspath, self.__tokenizer_model)
        elif group == 'ner':
            self.__models[abspath] = Ner(abspath)
        elif group == 'crdc':
            self.__models[abspath] = Crdc(abspath, self.__tokenizer_model)

        return self.__models[abspath]
