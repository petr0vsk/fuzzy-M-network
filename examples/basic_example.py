# examples/basic_example.py

from m_network.neuron import Neuron
from m_network.input_neuron import InputNeuron
from m_network.output_neuron import OutputNeuron

# Создаем нейрон
n1 = Neuron(neuron_id=1)

# Добавляем подключения
n1.add_connection(target_neuron_id=2, weight=0.9)
n1.add_connection(target_neuron_id=3, weight=-0.4, connection_type="inhibitory")

# Выводим информацию
n1.display_info()



# Создаем нейроны
input_n = InputNeuron(neuron_id=1)
output_n = OutputNeuron(neuron_id=2)

# Передаем входной сигнал
input_n.receive_input(0.8)
input_n.display_info()  # Input Neuron ID: 1, Input Signal: 0.8

# Подключаем input_n к output_n
output_n.add_connection(target_neuron_id=input_n.neuron_id, weight=1.0)

# Вычисляем результат
output_n.compute_output()
output_n.display_info()  # Output Neuron ID: 2, Output Value: 1.0

