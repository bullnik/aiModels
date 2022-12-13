from abc import ABC, abstractmethod


class Model(ABC):

    @abstractmethod
    def get_raw_result(self, request):
        pass

    @abstractmethod
    def get_json_result(self, request):
        pass
