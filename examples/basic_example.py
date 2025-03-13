from m_network.mnetwork import MNetwork
from m_network.neuron import Neuron

# Создаем сеть
net = MNetwork()

# Создаем нейроны
n1 = Neuron(1)  # Входной нейрон
n2 = Neuron(2)  # Промежуточный нейрон
n3 = Neuron(3)  # Выходной нейрон
n4 = Neuron(4)  # Выходной нейрон

# Добавляем нейроны в сеть
net.add_neuron(n1)
net.add_neuron(n2)
net.add_neuron(n3)
net.add_neuron(n4)

# Создаем связи
net.add_connection(1, 2, weight=0.5, conn_type="excitation")  # n1 -> n2
net.add_connection(2, 3, weight=0.8, conn_type="excitation")  # n2 -> n3

# Передаем входной сигнал (n1 получает 10.0)
net.propagate_signal({1: 10.0})

# Получаем выходные нейроны с максимальным value
winners = net.get_result()
print("Выходные нейроны с максимальным сигналом:")
for neuron in winners:
    print(neuron)
