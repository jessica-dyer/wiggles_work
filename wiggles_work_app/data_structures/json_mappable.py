import importlib
from abc import ABC, abstractmethod

class JsonMappable(ABC):
    @abstractmethod
    def to_dict_or_list(self):
        pass

    @classmethod
    def serialize_list(cls, list_of_objects, includeClassName=False):
        list_of_dicts = []
        for obj in list_of_objects:
            d = obj.to_dict_or_list()
            if includeClassName:
                d['type_class_name'] = obj.__module__ + '.' + type(obj).__name__
            list_of_dicts.append(d)

        return list_of_dicts

    @classmethod
    def rehydrate_list(cls, list_of_dicts, class_type=None):
        list_of_objects = []
        for d in list_of_dicts:
            if class_type is None:
                type_string = d['type_class_name']
                moduleNameString, classNameString = type_string.rsplit('.',1)
                module = importlib.import_module(moduleNameString)
                class_type = getattr(module, classNameString)
            obj = class_type.construct_from_dict(d)
            list_of_objects.append(obj)
        return list_of_objects