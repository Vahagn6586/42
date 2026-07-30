import sys


def add_archive_marker(content) -> str:
    lines = content.split("\n")

    new_content = ""

    for line in lines:
        if line != "":
            new_content += line + "#"
        new_content += "\n"

    return new_content


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_archive_creation.py <file>")
        return

    filename = sys.argv[1]

    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{filename}'")

    try:
        file = open(filename)
        content = file.read()
        print("---")
        print(content, end="")
        print("---")
        file.close()
        print(f"File '{filename}' closed.")

    except OSError as e:
        print(f"[STDERR] Error opening file '{filename}': {e}",
              file=sys.stderr)
        return

    print("Transform data:")

    new_content = add_archive_marker(content)

    print("---")
    print(new_content, end="", flush=True)
    print("---")

    print("Enter new file name (or empty): ", end="")
    save_name = sys.stdin.readline().strip()
    if save_name == "":
        print("Not saving data.")
        return

    print(f"Saving data to '{save_name}'")

    try:
        new_file = open(save_name, "w")
        new_file.write(new_content)
        new_file.close()
        print(f"Data saved in file '{save_name}'.")
    except OSError as e:
        print(f"[STDERR] Error saving file '{save_name}': {e}",
              file=sys.stderr)


if __name__ == "__main__":
    main()
