from abc import ABCMeta, abstractmethod
from typing import List, Dict

class BaseNeuronMeta(metaclass=ABCMeta):
    """
    Абстрактный класс для нейрона в М-сети
    """

    @property
    @abstractmethod
    def id(self) -> int:
        """Уникальный идентификатор нейрона"""
        pass

    @property
    @abstractmethod
    def value(self) -> float:
        """Текущий накопленный сигнал"""
        pass

    @value.setter
    @abstractmethod
    def value(self, val: float):
        """Устанавливает значение накопленного сигнала"""
        pass

    @property
    @abstractmethod
    def target_ids(self) -> List[int]:
        """Список ID целевых нейронов"""
        pass

    @abstractmethod
    def add_target(self, target_id: int) -> None:
        """Добавляет ID целевого нейрона"""
        pass

    @abstractmethod
    def process_signal(self) -> None:
        """Обрабатывает входной сигнал (реализация зависит от типа нейрона)"""
        pass

    @abstractmethod
    def activate(self) -> None:
        """Активирует нейрон (можно переопределить для разных функций активации)"""
        pass

class BaseConnectionMeta(metaclass=ABCMeta):
    """
    Абстрактный класс для связи между нейронами в М-сети.
    """

    @property
    @abstractmethod
    def source_id(self) -> int:
        """ID нейрона-источника"""
        pass

    @property
    @abstractmethod
    def target_id(self) -> int:
        """ID нейрона-цели"""
        pass

    @property
    @abstractmethod
    def weight(self) -> float:
        """Вес связи"""
        pass

    @weight.setter
    @abstractmethod
    def weight(self, new_weight: float):
        """Устанавливает новый вес связи"""
        pass

    @property
    @abstractmethod
    def conn_type(self) -> str:
        """Тип связи ("excitation" или "inhibition")"""
        pass

    @abstractmethod
    def transmit_signal(self, signal: float) -> float:
        """
        Передает сигнал с учетом веса и типа связи.
        :param signal: Входной сигнал.
        :return: Преобразованный сигнал.
        """
        pass

class BaseNetworkMeta(metaclass=ABCMeta):
    """
    Абстрактный класс для М-сети.
    """

    @property
    @abstractmethod
    def neurons(self) -> Dict[int, "BaseNeuronMeta"]:
        """Список всех нейронов в сети (словарь {id: нейрон})"""
        pass

    @property
    @abstractmethod
    def connections(self) -> List["BaseConnectionMeta"]:
        """Список всех связей в сети"""
        pass

    @abstractmethod
    def add_neuron(self, neuron: "BaseNeuronMeta") -> None:
        """Добавляет нейрон в сеть"""
        pass

    @abstractmethod
    def add_connection(self, source_id: int, target_id: int, weight: float, conn_type: str) -> None:
        """Создает и добавляет связь между нейронами"""
        pass

    @abstractmethod
    def propagate_signal(self, input_signals: Dict[int, float]) -> None:
        """
        Передает сигналы по сети.
        :param input_signals: Словарь {id_нейрона: входной сигнал}.
        """
        pass

    @abstractmethod
    def get_result(self) -> "BaseNeuronMeta":
        """
        Возвращает нейрон, который имеет максимальный накопленный сигнал.
        """
        pass