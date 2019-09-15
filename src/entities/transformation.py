from abc import ABC, abstractmethod


class Transformation(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def transform(self, to_transform):
        pass


class DataTransformation(Transformation):

    def __init__(self, norm_values, column_mask):
        super().__init__()
        self.__norm_values = norm_values
        self.__column_mask = column_mask

    def transform(self, to_transform):
        transformed = to_transform / self.__norm_values[None, :]
        transformed = transformed[:, self.__column_mask]

        return transformed
