from abc import ABC, abstractmethod
from typing import Any


class ImproperDataError(Exception):

    def __init__(self, message="Error!!"):
        super().__init__(message)


class DataProcessor(ABC):

    def __init__(self) -> None:
        self._queue: list[str] = []
        self._count: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        rank = self._count - len(self._queue)
        first = self._queue.pop(0)
        return (rank, first)


class NumericProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True

        if isinstance(data, list):
            return all(isinstance(item, (int, float)) for item in data)

        return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise ImproperDataError("Improper numeric data")

        if isinstance(data, list):
            for x in data:
                self._queue.append(str(x))
                self._count += 1

        else:
            self._queue.append(str(data))
            self._count += 1


class TextProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True

        if isinstance(data, list):
            return all(isinstance(item, str) for item in data)

        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ImproperDataError("Improper text data")

        if isinstance(data, list):
            for x in data:
                self._queue.append(x)
                self._count += 1

        else:
            self._queue.append(data)
            self._count += 1


class LogProcessor(DataProcessor):

    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            return (
                all(isinstance(k, str) for k in data) and
                all(isinstance(v, str) for v in data.values())
            )

        if isinstance(data, list):
            return all(
                isinstance(item, dict) and
                all(isinstance(k, str) for k in item) and
                all(isinstance(v, str) for v in item.values())
                for item in data
            )

        return False

    def ingest(self, data: dict | list[dict]) -> None:
        if not self.validate(data):
            raise ImproperDataError("Improper log data")

        if isinstance(data, list):
            for x in data:
                self._queue.append(f"{x['log_level']}: {x['log_message']}")
                self._count += 1

        else:
            self._queue.append(f"{data['log_level']}: {data['log_message']}")
            self._count += 1


def main():
    print("=== Code Nexus - Data Processor ===", end='\n\n')

    print("Testing Numeric Processor...", end='\n ')

    NumProc = NumericProcessor()

    data = 42
    print(f"Trying to validate input '{data}': ", end='')
    print(NumProc.validate(data), end='\n ')

    data = "Hello"
    print(f"Trying to validate input '{data}': ", end='')
    print(NumProc.validate(data), end='\n ')

    data = "foo"
    try:
        NumProc.ingest(data)
    except ImproperDataError as e:
        print(f"Test invalid ingestion of string '{data}'", end='')
        print("without prior validation:", end='\n ')
        print(f"Got exception: {e}", end="\n ")

    data = [1, 2, 3, 4, 5]
    count = 3
    print(f"Processing data: {data}", end="\n ")
    NumProc.ingest(data)
    print(f"Extracting {count} values...", end='\n ')
    for i in range(count):
        rank, value = NumProc.output()
        print(f"Numeric value {rank}: {value}", end='\n ')

    print()

    print("Testing Text Processor...", end='\n ')

    TextProc = TextProcessor()

    data = 42
    print(f"Trying to validate input '{data}': ", end='')
    print(TextProc.validate(data), end='\n ')

    data = ['Hello', 'Nexus', 'World']
    count = 1
    print(f"Processing data: {data}", end="\n ")
    TextProc.ingest(data)
    print(f"Extracting {count} value...", end='\n ')
    for i in range(count):
        rank, value = TextProc.output()
        print(f"Text value {rank}: {value}", end='\n ')

    print()

    print("Testing Log Processor...", end='\n ')

    LogProc = LogProcessor()

    data = "Hello"
    print(f"Trying to validate input '{data}': ", end='')
    print(LogProc.validate(data), end='\n ')

    data = [{'log_level': 'NOTICE', 'log_message': 'Connection to server'},
            {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}]
    count = 2
    print(f"Processing data: {data}", end="\n ")
    LogProc.ingest(data)
    print(f"Extracting {count} value...", end='\n ')
    for i in range(count):
        rank, value = LogProc.output()
        print(f"Log entry {rank}: {value}", end='\n ')

    print('\b', end='')


if __name__ == "__main__":
    main()
