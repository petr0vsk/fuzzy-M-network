from m_network.neuron import Neuron

class OutputNeuron(Neuron):
    """
    Класс для представления выходного нейрона.
    """

    def __init__(self, neuron_id: int):
        super().__init__(neuron_id)
        self.output_value = 0.0

    def compute_output(self):
        """
        Рассчитывает выходное значение на основе входных сигналов.
        """
        total_input = sum(conn.weight for conn in self.connections)
        self.output_value = total_input  # Пример простой агрегации

    def display_info(self):
        super().display_info()  # Вызов метода из родителя
        print(f"Input Signal: {self.output_value}")