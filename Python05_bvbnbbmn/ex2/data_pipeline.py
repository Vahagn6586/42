from abc import ABC, abstractmethod
from typing import Any


class ImproperDataError(Exception):

    def __init__(self, message="Error!!"):
        super().__init__(message)


class DataProcessor(ABC):

    def __init__(self) -> None:
        self._queue: list[str] = []
        self._count: int = 0
        self._name: str = ""

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


class DataStream:

    def __init__(self):
        self._proc_queue: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._proc_queue.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for element in stream:
            for proc in self._proc_queue:
                if proc.validate(element):
                    proc.ingest(element)
                    break
                else:
                    print("DataStream error - Can't process element in stream:"
                          f" {element}")

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self._proc_queue:
            print("No processor found, no data")
            return
        for proc in self._proc_queue:
            name = proc._name
            total = proc._count
            remaining = len(proc._queue)
            print(f"{name}: total {total} items processed, "
                  f"remaining {remaining} on processor")


class NumericProcessor(DataProcessor):

    def __init__(self):
        super().__init__()
        self._name = "Numeric Processor"

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

    def __init__(self):
        super().__init__()
        self._name = "Text Processor"

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

    def __init__(self):
        super().__init__()
        self._name = "Log Processor"

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
    print("=== Code Nexus - Data Stream ===", end='\n\n')

    print("Initialize Data Stream...")

    data_stream = DataStream()
    data_stream.print_processors_stats()
    print()

    print("Registering Numeric Processor", end='\n\n')

    num_proc = NumericProcessor()
    data_stream.register_processor(num_proc)

    print("Send first batch of data on stream: ['Hello world',"
          "[3.14, -1, 2.71], [{'log_level': 'WARNING', '"
          "log_message': 'Telnet access! Use ssh instead'},"
          "{'log_level': 'INFO', 'log_message': 'User wil is"
          "connected'}], 42, ['Hi', 'five']]")

    data = ['Hello world',
            [3.14, -1, 2.71],
            [{'log_level': 'WARNING',
              'log_message': 'Telnet access! Use ssh instead'},
             {'log_level': 'INFO', 'log_message': 'User wil isconnected'}],
            42,
            ['Hi', 'five']]
    data_stream.process_stream(data)
    data_stream.print_processors_stats()
    print()

    print("Registering other data processors")

    text_proc = TextProcessor()
    log_proc = LogProcessor()
    data_stream.register_processor(text_proc)
    data_stream.register_processor(log_proc)

    print("Send the same batch again")

    data_stream.process_stream(data)
    data_stream.print_processors_stats()
    print()

    print("Consume some elements from the data processors: "
          "Numeric 3, Text 2, Log 1")
    for i in range(3):
        num_proc.output()
    for i in range(2):
        text_proc.output()
    for i in range(1):
        log_proc.output()
    data_stream.print_processors_stats()


if __name__ == "__main__":
    main()
