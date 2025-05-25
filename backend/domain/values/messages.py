from dataclasses import dataclass

from backend.domain.exceptions.messages import EmptyTextError, TitleToLongException
from backend.domain.values.base import BaseValueObject


@dataclass(frozen=True)
class Text(BaseValueObject[str]):
    value: str
    def validate(self):
        if not self.value:
            raise EmptyTextError()


    def as_generic_type(self):
        return self.value

@dataclass(frozen=True)
class Title(BaseValueObject[str]):
    value: str
    def validate(self):
        if not self.value:
            raise EmptyTextError()
        if len(self.value)>255:
            raise TitleToLongException(self.value)

    def as_generic_type(self):
        return self.value