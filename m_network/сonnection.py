from m_network.meta import BaseConnectionMeta

class Connection(BaseConnectionMeta):
    def __init__(self, source_id: int, target_id: int, weight: float, conn_type: str):
        if not isinstance(source_id, int) or not isinstance(target_id, int):
            raise TypeError("source_id и target_id должны быть int")
        if not isinstance(weight, (int, float)):
            raise TypeError("weight должен быть числом")
        if conn_type not in {"excitation", "inhibition"}:
            raise ValueError("conn_type должен быть 'excitation' или 'inhibition'")

        self._source_id = source_id
        self._target_id = target_id
        self._weight = float(weight)
        self._conn_type = conn_type

    @property
    def source_id(self) -> int:
        return self._source_id

    @property
    def target_id(self) -> int:
        return self._target_id

    @property
    def weight(self) -> float:
        return self._weight

    @weight.setter
    def weight(self, new_weight: float):
        if not isinstance(new_weight, (int, float)):
            raise TypeError("weight должен быть числом")
        self._weight = float(new_weight)

    @property
    def conn_type(self) -> str:
        return self._conn_type

    def transmit_signal(self, signal: float) -> float:
        if not isinstance(signal, (int, float)):
            raise TypeError("signal должен быть числом")

        return signal * self._weight if self._conn_type == "excitation" else -signal * self._weight

    def __repr__(self):
        return f"Connection(source={self._source_id}, target={self._target_id}, weight={self._weight}, type={self._conn_type})"
