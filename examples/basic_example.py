# examples/basic_example.py

from m_network.neuron import Neuron  # Импортируем класс

# Создаем объект нейрона
n1 = Neuron(neuron_id=1)
n2 = Neuron(neuron_id=2, initial_value=0.75)
print(type(n1))  # Проверим тип объекта
# Вывод информации о нейронах
n1.display_info()  # Ожидаемый вывод: Neuron ID: 1, Value: 0.0
n2.display_info()  # Ожидаемый вывод: Neuron ID: 2, Value: 0.75
print(Neuron.__doc__)