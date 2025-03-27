from m_network.meta import BaseConnectionMeta

# Класс, представляющий соединение между двумя узлами
class Connection(BaseConnectionMeta):
    def __init__(self, source_id: int, target_id: int, weight: float, conn_type: str):
        # Проверка типа данных для source_id и target_id, они должны быть целыми числами
        if not isinstance(source_id, int) or not isinstance(target_id, int):
            raise TypeError("source_id и target_id должны быть int")

        # Проверка типа данных для weight, он должен быть числом (целым или с плавающей точкой)
        if not isinstance(weight, (int, float)):
            raise TypeError("weight должен быть числом")

        # Проверка значения для conn_type, оно должно быть либо 'excitation', либо 'inhibition'
        if conn_type not in {"excitation", "inhibition"}:
            raise ValueError("conn_type должен быть 'excitation' или 'inhibition'")

        # Инициализация атрибутов соединения
        self._source_id = source_id
        self._target_id = target_id
        self._weight = float(weight)
        self._conn_type = conn_type

    @property
    def source_id(self) -> int:
        # Возвращает идентификатор исходного узла
        return self._source_id

    @property
    def target_id(self) -> int:
        # Возвращает идентификатор целевого узла
        return self._target_id

    @property
    def weight(self) -> float:
        # Возвращает вес соединения
        return self._weight

    @weight.setter
    def weight(self, new_weight: float):
        # Проверка типа данных для нового значения веса, оно должно быть числом (целым или с плавающей точкой)
        if not isinstance(new_weight, (int, float)):
            raise TypeError("weight должен быть числом")

        # Обновление веса соединения
        self._weight = float(new_weight)

    @property
    def conn_type(self) -> str:
        # Возвращает тип соединения (excitation или inhibition)
        return self._conn_type

    def transmit_signal(self, signal: float) -> float:
        # Проверка типа данных для сигнала, он должен быть числом (целым или с плавающей точкой)
        if not isinstance(signal, (int, float)):
            raise TypeError("signal должен быть числом")

        # Передача сигнала, модифицируя его в зависимости от типа соединения и веса
        return signal * self._weight if self._conn_type == "excitation" else -signal * self._weight

    def __repr__(self):
        # Возвращает строковое представление соединения
        return f"Connection(source={self._source_id}, target={self._target_id}, weight={self._weight}, type={self._conn_type})"