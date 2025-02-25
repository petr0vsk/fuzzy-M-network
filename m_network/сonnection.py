class Connection:
    def __init__(self, target_neuron_id: int, weight: float, connection_type: str = "excitatory"):
        """
        Инициализация связи.
        :param target_neuron_id: ID целевого нейрона.
        :param weight: Вес связи.
        :param connection_type: Тип связи ('excitatory' или 'inhibitory').
        """
        self.target_neuron_id = target_neuron_id
        self.weight = weight
        self.connection_type = connection_type

    def __repr__(self):
        return f"Connection(to={self.target_neuron_id}, weight={self.weight}, type={self.connection_type})"
