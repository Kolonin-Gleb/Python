from abc import ABC, abstractmethod

class FighterAbstract(ABC):
  def __init__(self, name: str):
    self.name = name

class ContestAbstract(ABC):
  winner: FighterAbstract #Должен быть атрибут класса
  @classmethod
  @abstractmethod
  def meet_fighters(cls, first: FighterAbstract, second: FighterAbstract) -> None:
      '''Инициализация боя'''

  @classmethod
  @abstractmethod
  def start_battle(cls) -> None:  # -> None - подсказка, что класс ничего не возращает
    '''Здесь описывается логика боя'''


