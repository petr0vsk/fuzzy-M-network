class Neuron:
    """
    Класс для представления нейрона в М-сети.
    """
    def __init__(self, neuron_id, initial_value=0.0, connections=None):
        """
        Конструктор для инициализации нейрона.
        :param neuron_id: Уникальный идентификатор нейрона.
        :param initial_value: Начальное значение нейрона (по умолчанию 0.0).
        """
        self.neuron_id = neuron_id
        self.value = initial_value
        self.connections = connections if connections else []

    def display_info(self):
        """Печатает информацию о нейроне."""
        print(f"Neuron_id: {self.neuron_id}, Value: {self.value}")

    def set_value(self, new_value: float) -> None:
        """
        Устанавливает новое значение для нейрона.
        :param new_value: Новое значение для нейрона.
        """
        self.value = new_value

    def get_value(self) -> float:
        """
        Возвращает текущее значение нейрона.
        :return: Значение нейрона.
        """
        return self.value
