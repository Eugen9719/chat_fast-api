from dataclasses import dataclass

from backend.domain.exceptions.base import ApplicationException


@dataclass(eq=False)
class TitleToLongException(ApplicationException):
    text: str

    @property
    def message(self):
        return f'{self.text} слишком длинный текст сообщения'

@dataclass(eq=False)
class EmptyTextError(ApplicationException):

    @property
    def message(self):
        return f'Текст не может быть пустым'