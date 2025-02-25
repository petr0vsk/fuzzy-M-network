from m_network.neuron import Neuron

class InputNeuron(Neuron):
    """
    Класс для представления входного нейрона.
    """

    def __init__(self, neuron_id: int):
        super().__init__(neuron_id)
        self.input_signal = 0.0  # Хранит входной сигнал

    def receive_input(self, input_signal: float):
        """
        Принимает входной сигнал.
        """
        self.input_signal = input_signal
        self.set_value(input_signal)

    def display_info(self):
        super().display_info()  # Вызов метода из родителя
        print(f"Input Signal: {self.input_signal}")