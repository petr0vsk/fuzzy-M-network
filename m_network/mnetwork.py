from m_network.meta import BaseNetworkMeta
from m_network.neuron import Neuron
from m_network.сonnection  import Connection
from typing import Dict, List

class MNetwork(BaseNetworkMeta):
    def __init__(self):
        """
        Конструктор для М-сети.
        """
        self._neurons: Dict[int, Neuron] = {}  # Словарь {id: Neuron}
        self._connections: List[Connection] = []  # Список всех связей

    @property
    def neurons(self) -> Dict[int, Neuron]:
        """Возвращает список всех нейронов."""
        return self._neurons

    @property
    def connections(self) -> List[Connection]:
        """Возвращает список всех связей."""
        return self._connections

    def add_neuron(self, neuron: Neuron):
        """
        Добавляет нейрон в сеть.
        :param neuron: Объект Neuron.
        """
        if neuron.id in self._neurons:
            raise ValueError(f"Нейрон с id={neuron.id} уже существует в сети")

        self._neurons[neuron.id] = neuron

    def add_connection(self, source_id: int, target_id: int, weight: float, conn_type: str):
        """
        Создает и добавляет связь между нейронами.
        :param source_id: ID нейрона-источника.
        :param target_id: ID нейрона-цели.
        :param weight: Вес связи.
        :param conn_type: Тип связи ("excitation" или "inhibition").
        """
        if source_id not in self._neurons or target_id not in self._neurons:
            raise ValueError("Один или оба нейрона не существуют в сети")

        # Создаем соединение
        conn = Connection(source_id, target_id, weight, conn_type)
        self._connections.append(conn)

        # Добавляем ID связи в нейрон-источник
        self._neurons[source_id].add_target(target_id)

    def propagate_signal(self, input_signals: Dict[int, float]):
        """
        Передает сигналы по сети.
        :param input_signals: Словарь {id_нейрона: входной сигнал}.
        """
        # Устанавливаем начальные сигналы
        for neuron_id, signal in input_signals.items():
            if neuron_id in self._neurons:
                self._neurons[neuron_id].value = signal

        # Передаём сигналы по связям
        for conn in self._connections:
            source_neuron = self._neurons[conn.source_id]
            target_neuron = self._neurons[conn.target_id]

            # Получаем сигнал с учетом веса и типа связи
            signal = conn.transmit_signal(source_neuron.value)

            # Обновляем значение целевого нейрона
            target_neuron.value += signal

    def get_result(self) -> List[Neuron]:
        """
        Возвращает список выходных нейронов с наибольшим накопленным сигналом.
        Выходной нейрон — это нейрон, у которого нет исходящих связей.
        """
        if not self._neurons:
            raise ValueError("Сеть пуста, невозможно получить результат")

        # Находим выходные нейроны (те, у кого нет исходящих связей)
        output_neurons = [neuron for neuron in self._neurons.values() if not neuron.target_ids]

        if not output_neurons:
            raise ValueError("В сети нет выходных нейронов")

        # Находим максимальное значение среди выходных нейронов
        max_value = max(neuron.value for neuron in output_neurons)

        # Возвращаем список всех выходных нейронов с этим значением
        return [neuron for neuron in output_neurons if neuron.value == max_value]

    def __repr__(self):
        return f"MNetwork(neurons={list(self._neurons.keys())}, connections={len(self._connections)})"
