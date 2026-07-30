from abc import ABC, abstractmethod
from typing import Any, Protocol


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


class ExportPlugin(Protocol):

    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


class DataStream:

    def __init__(self) -> None:
        self._proc_queue: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._proc_queue.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for element in stream:
            processed = False

            for proc in self._proc_queue:
                if proc.validate(element):
                    proc.ingest(element)
                    processed = True
                    break

            if not processed:
                print(
                    "DataStream error - Can't process element:",
                    element
                )

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

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self._proc_queue:
            result = []
            for i in range(nb):
                if len(proc._queue) == 0:
                    break
                result.append(proc.output())
            plugin.process_output(result)


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


class CSVExportPlugin:

    def __init__(self) -> None:
        self._name: str = "CSV"

    def process_output(self, data: list[tuple[int, str]]) -> None:
        result = []
        for output in data:
            rank, value = output
            result.append(value)
        print(self._name, "Output:")
        print(",".join(result))


class JSONExportPlugin:

    def __init__(self) -> None:
        self._name: str = "JSON"

    def process_output(self, data: list[tuple[int, str]]) -> None:
        result = {}
        for output in data:
            rank, value = output
            result.update({f"item_{rank}": value})
        print(self._name, "Output")
        print(result)


def main() -> None:
    print("=== Code Nexus - Data Pipeline ===", end='\n\n')
    print("Initialize Data Stream...", end='\n\n')

    d_stream = DataStream()
    num_p = NumericProcessor()
    text_p = TextProcessor()
    log_p = LogProcessor()

    d_stream.print_processors_stats()

    print("Registering Processors", end='\n\n')
    d_stream.register_processor(num_p)
    d_stream.register_processor(text_p)
    d_stream.register_processor(log_p)

    print("Send first batch of data on stream: ['Hello world', "
          "[3.14, -1, 2.71],[{'log_level': 'WARNING', '"
          "log_message': 'Telnet access! Use ssh instead'}, "
          "{'log_level': 'INFO', 'log_message': 'User wil is"
          "connected'}], 42, ['Hi', 'five']]")
    data = ['Hello world',
            [3.14, -1, 2.71],
            [{'log_level': 'WARNING',
              'log_message': 'Telnet access! Use ssh instead'},
             {'log_level': 'INFO', 'log_message': 'User wil is connected'}],
            42,
            ['Hi', 'five']]
    d_stream.process_stream(data)

    d_stream.print_processors_stats()
    print()

    print("Send 3 processed data from each processor to a CSV plugin:")
    csv = CSVExportPlugin()
    d_stream.output_pipeline(3, csv)
    print()

    d_stream.print_processors_stats()
    print()

    print("Send another batch of data: [21, ['I love AI', "
          "'LLMs are wonderful', 'Stay healthy'], [{'log_level': '"
          "ERROR', 'log_message': '500 server crash'},"
          "{'log_level': 'NOTICE', 'log_message': 'Certificate"
          "expires in 10 days'}], [32, 42, 64, 84, 128, 168], 'World hello']",
          end='\n\n')
    data1 = [21,
             ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
             [{'log_level': 'ERROR', 'log_message': '500 server crash'},
              {'log_level': 'NOTICE',
               'log_message': 'Certificate expires in 10 days'}],
             [32, 42, 64, 84, 128, 168],
             'World hello']
    d_stream.process_stream(data1)

    d_stream.print_processors_stats()
    print()

    print("Send 5 processed data from each processor to a JSON plugin:")
    json = JSONExportPlugin()
    d_stream.output_pipeline(5, json)
    print()

    d_stream.print_processors_stats()


if __name__ == "__main__":
    main()
    # data_stream = DataStream()
    # data_stream.print_processors_stats()

    # num_proc = NumericProcessor()
    # txt_proc = TextProcessor()

    # data_stream.register_processor(num_proc)
    # data_stream.register_processor(txt_proc)

    # data_stream.print_processors_stats()

    # data_stream.process_stream([434, 4, 534, 6, 56, 53, 'ewgref',
    #                             ['rgfrwgfre', '453tvef']])
    # data_stream.print_processors_stats()

    # for i in range(random.randint(1, 6)):
    #     num_proc.output()

    # data_stream.print_processors_stats()
