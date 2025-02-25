from m_network.сonnection import Connection
class Neuron:
    """
    Класс для представления нейрона в М-сети.
    """
    def __init__(self, neuron_id: int, connections: list = None, initial_value: float = 0.0):
        """
        Конструктор для инициализации нейрона.
        :param neuron_id: Уникальный идентификатор нейрона.
        :param initial_value: Начальное значение нейрона (по умолчанию 0.0).
        """
        self.neuron_id = neuron_id
        self.value = initial_value
        self.connections = connections if connections is not None else []

    def display_info(self):
        print(f"Neuron ID: {self.neuron_id}, Value: {self.value}")
        print("Connections:")
        for conn in self.connections:
            print(f" -> {conn}")

    def set_value(self, new_value: float) -> None:
        """
        Устанавливает новое значение для нейрона.
        :param new_value: Новое значение для нейрона.
        """
        self.value = new_value

    def set_connections(self, connections: list) -> None:
        """
        Устанавливает новое значение для нейрона.
        :param new_value: Новое значение для нейрона.
        """
    def get_value(self) -> list:
        """
        Возвращает текущее значение нейрона.
        :return: Значение нейрона.
        """
        return self.value

    def get_connections(self) -> float:
        """
        Возвращает текущее значение нейрона.
        :return: Значение нейрона.
        """
        return self.connections

    def add_connection(self, target_neuron_id: int, weight: float, connection_type: str = "excitatory"):
        """
        Добавляет новое подключение к другому нейрону.
        """
        new_connection = Connection(target_neuron_id, weight, connection_type)
        self.connections.append(new_connection)