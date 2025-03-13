from m_network.mnetwork import MNetwork
from m_network.neuron import Neuron

# Создаём сеть
net = MNetwork()

# Создаём нейроны
n1 = Neuron(1)
n2 = Neuron(2)
n3 = Neuron(3)

# Добавляем нейроны в сеть
net.add_neuron(n1)
net.add_neuron(n2)
net.add_neuron(n3)

# Создаём связи между нейронами
net.add_connection(1, 2, weight=0.5, conn_type="excitation")
net.add_connection(2, 3, weight=0.8, conn_type="excitation")

# Передаём входной сигнал (n1 получает 10.0)
net.propagate_signal({1: 10.0})

# Выводим состояние сети
print(n1)  # Neuron(id=1, value=10.0, targets=[2])
print(n2)  # Neuron(id=2, value=5.0, targets=[3])
print(n3)  # Neuron(id=3, value=4.0, targets=[])

# Получаем "победителя" – нейрон с максимальным value
winner = net.get_result()
print(f"Нейрон с максимальным сигналом: {winner}")
