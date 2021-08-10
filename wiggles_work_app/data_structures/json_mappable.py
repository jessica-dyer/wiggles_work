from abc import ABC, abstractmethod

class JsonMappable(ABC):
    @abstractmethod
    def to_dict_or_list(self):
        pass

    @classmethod
    def serialize_list(cls, list_of_objects):
        list_of_dicts = []
        for d in list_of_objects:
            list_of_dicts.append(d.to_dict_or_list())
        return list_of_dicts

    @classmethod
    def rehydrate_list(cls, list_of_dicts, class_type):
        list_of_objects = []
        for d in list_of_dicts:
            route = class_type.construct_from_dict(d)
            list_of_objects.append(route)
        return list_of_objects