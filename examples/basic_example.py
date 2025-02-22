# examples/basic_example.py

from m_network.neuron import Neuron

# Создаем нейрон
n1 = Neuron(neuron_id=1)

# Выводим начальную информацию
n1.display_info()  # Neuron ID: 1, Value: 0.0

# Меняем значение нейрона
n1.set_value(0.85)

# Проверяем новое значение
print("Новое значение нейрона:", n1.get_value())  # Новое значение нейрона: 0.85

# Выводим обновленную информацию
n1.display_info()  # Neuron ID: 1, Value: 0.85