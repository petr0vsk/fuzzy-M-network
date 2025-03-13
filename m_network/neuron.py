from m_network.meta import BaseNeuronMeta
from typing import List

class Neuron(BaseNeuronMeta):
    def __init__(self, neuron_id: int):
        if not isinstance(neuron_id, int):
            raise TypeError(f"neuron_id должен быть int, получено {type(neuron_id).__name__}")
        if neuron_id < 0:
            raise ValueError(f"neuron_id должен быть неотрицательным числом, получено {neuron_id}")

        self._id = neuron_id
        self._value = 0.0
        self._target_ids: List[int] = []

    @property
    def id(self) -> int:
        return self._id

    @property
    def value(self) -> float:
        return self._value

    @value.setter
    def value(self, val: float):
        if not isinstance(val, (int, float)):
            raise TypeError(f"value должен быть числом (int или float), получено {type(val).__name__}")
        self._value = float(val)

    @property
    def target_ids(self) -> List[int]:
        return self._target_ids

    def add_target(self, target_id: int):
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

    def __repr__(self):
        return f"Neuron(id={self._id}, value={self._value}, targets={self._target_ids})"
