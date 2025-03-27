from m_network.meta import BaseNeuronMeta
from typing import List, Union

class Neuron(BaseNeuronMeta):
    def __init__(self, neuron_id: int):
        """
        Инициализация нейрона.

        :param neuron_id: уникальный идентификатор нейрона (должен быть неотрицательным числом)
        """
        if not isinstance(neuron_id, int):
            raise TypeError(f"neuron_id должен быть int, получено {type(neuron_id).__name__}")
        if neuron_id < 0:
            raise ValueError(f"neuron_id должен быть неотрицательным числом, получено {neuron_id}")

        self._id: int = neuron_id
        self._value: float = 0.0
        self._target_ids: List[int] = []

    @property
    def id(self) -> int:
        """Возвращает идентификатор нейрона."""
        return self._id

    @property
    def value(self) -> float:
        """Возвращает значение нейрона."""
        return self._value

    @value.setter
    def value(self, val: Union[int, float]):
        """
        Устанавливает значение нейрона.

        :param val: новое значение (должно быть числом)
        """
        if not isinstance(val, (int, float)):
            raise TypeError(f"value должен быть числом (int или float), получено {type(val).__name__}")
        self._value = float(val)

    @property
    def target_ids(self) -> List[int]:
        """Возвращает список идентификаторов целей."""
        return self._target_ids

    def add_target(self, target_id: int):
        """
        Добавляет цель для нейрона.

        :param target_id: идентификатор цели (должен быть неотрицательным числом)
        """
        if not isinstance(target_id, int):
            raise TypeError(f"target_id должен быть int, получено {type(target_id).__name__}")
        if target_id < 0:
            raise ValueError(f"target_id должен быть неотрицательным числом, получено {target_id}")
        if target_id in self._target_ids:
            raise ValueError(f"Нейрон уже связан с target_id={target_id}")

        self._target_ids.append(target_id)

    def process_signal(self):
        """
        Обрабатывает входной сигнал.
        Пока заглушка – будет управляться `MNetwork`.
        """
        pass

    def activate(self):
        """
        Активирует нейрон.
        Пока заглушка – будет управляться `MNetwork`.
        """
        pass

    def __repr__(self) -> str:
        """Возвращает строковое представление нейрона."""
        return f"Neuron(id={self._id}, value={self._value}, targets={self._target_ids})"
