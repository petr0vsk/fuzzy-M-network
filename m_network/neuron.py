class Neuron:
    def __init__(self, neuron_id, initial_value=0.0):
        """
              Конструктор для инициализации нейрона.

              :param neuron_id: Уникальный идентификатор нейрона.
              :param initial_value: Начальное значение нейрона (по умолчанию 0.0).
        """
        self.neuron_id = neuron_id
        self.value = initial_value
    def display_info(self):
        """печатает информацию о нейроне"""
        print(f"Neuron_id: {self.neuron_id}, Value: {self.value}")