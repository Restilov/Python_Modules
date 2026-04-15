from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._storage: list[tuple[int, str]] = []
        self._counter: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self._storage:
            raise IndexError("No data available in processor")
        item = self._storage[0]
        self._storage.pop(0)
        return item

    def _store(self, value: str) -> None:
        self._storage.append((self._counter, value))
        self._counter += 1


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, bool):
            return False
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            return all(
                isinstance(x, (int, float)) and not isinstance(x, bool)
                for x in data
            )
        return False

    def ingest(
        self,
        data: int | float | list[int | float]
    ) -> None:
        if not self.validate(data):
            raise TypeError("Improper numeric data")
        if isinstance(data, list):
            for item in data:
                self._store(str(item))
        else:
            self._store(str(data))


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return bool(data) and all(isinstance(x, str) for x in data)
        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise TypeError("Improper text data")
        if isinstance(data, list):
            for item in data:
                self._store(item)
        else:
            self._store(data)


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            return all(
                isinstance(k, str) and isinstance(v, str)
                for k, v in data.items()
            )
        if isinstance(data, list):
            return bool(data) and all(
                isinstance(d, dict) and all(
                    isinstance(k, str) and isinstance(v, str)
                    for k, v in d.items()
                )
                for d in data
            )
        return False

    def ingest(
        self,
        data: dict[str, str] | list[dict[str, str]]
    ) -> None:
        if not self.validate(data):
            raise TypeError("Improper log data")
        if isinstance(data, list):
            for entry in data:
                self._store(
                    f"{entry['log_level']}: {entry['log_message']}"
                )
        else:
            self._store(
                f"{data['log_level']}: {data['log_message']}"
            )


def main() -> None:
    print("=== Code Nexus - Data Processor ===")

    print("\nTesting Numeric Processor...")
    num_proc = NumericProcessor()
    print(f" Trying to validate input '42': {num_proc.validate(42)}")
    print(
        f" Trying to validate input 'Hello': {num_proc.validate('Hello')}"
    )
    print(
        " Test invalid ingestion of string 'foo' without prior validation:"
    )
    try:
        num_proc.ingest("foo")  # type: ignore
    except TypeError as e:
        print(f" Got exception: {e}")
    data_num = [1, 2, 3, 4, 5]
    print(f" Processing data: {data_num}")
    num_proc.ingest(data_num)
    print(" Extracting 3 values...")
    for _ in range(3):
        rank, val = num_proc.output()
        print(f" Numeric value {rank}: {val}")

    print("\nTesting Text Processor...")
    txt_proc = TextProcessor()
    print(f" Trying to validate input '42': {txt_proc.validate(42)}")
    data_txt = ['Hello', 'Nexus', 'World']
    print(f" Processing data: {data_txt}")
    txt_proc.ingest(data_txt)
    print(" Extracting 1 value...")
    rank, val = txt_proc.output()
    print(f" Text value {rank}: {val}")

    print("\nTesting Log Processor...")
    log_proc = LogProcessor()
    print(
        f" Trying to validate input 'Hello': {log_proc.validate('Hello')}"
    )
    data_log: list[dict[str, str]] = [
        {'log_level': 'NOTICE', 'log_message': 'Connection to server'},
        {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}
    ]
    print(f" Processing data: {data_log}")
    log_proc.ingest(data_log)
    print(" Extracting 2 values...")
    for _ in range(2):
        rank, val = log_proc.output()
        print(f" Log entry {rank}: {val}")


main()