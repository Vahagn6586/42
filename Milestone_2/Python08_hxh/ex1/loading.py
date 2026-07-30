import importlib


REQUIRED_PACKAGES = {
    "numpy": "Numerical computation",
    "pandas": "Data manipulation",
    "matplotlib": "Visualization",
    "requests": "Network access",
}


def installation_help(missing):
    print("\nMissing dependencies detected.")

    print("\nUsing pip:")
    print("pip install -r requirements.txt")

    print("\nUsing Poetry:")
    print("poetry install")

    print("\nMissing:")
    for package in missing:
        print(f"- {package}")


def generate_matrix_data():
    import numpy as np

    print("Analyzing Matrix data...")

    data = np.random.normal(
        loc=100,
        scale=20,
        size=1000
    )

    return data


def analyze_data(data):
    import pandas as pd

    df = pd.DataFrame(
        {
            "matrix_value": data
        }
    )

    print(
        f"Processing {len(df)} data points..."
    )

    print("\nMatrix statistics:")
    print(df.describe())

    return df


def visualize(df):
    import matplotlib.pyplot as plt

    print("Generating visualization...")

    plt.figure(figsize=(10, 5))

    plt.plot(
        df["matrix_value"]
    )

    plt.title(
        "Matrix Data Simulation"
    )

    plt.xlabel(
        "Data Point"
    )

    plt.ylabel(
        "Matrix Value"
    )

    plt.savefig(
        "matrix_analysis.png"
    )

    plt.close()

    print(
        "Analysis complete!"
    )

    print(
        "Results saved to: matrix_analysis.png"
    )


def compare_dependencies():
    print("\nDependency management comparison:")
    print("--------------------------------")

    print(
        """
pip:
- Installs packages globally or in venv
- Uses requirements.txt
- Simple package installer
- User manages environments

Poetry:
- Dependency manager + environment manager
- Uses pyproject.toml
- Creates isolated environments automatically
- Handles versions and locking
        """
    )


def check_dependencies():
    print("Checking dependencies:")

    missing = []

    for package, description in REQUIRED_PACKAGES.items():
        try:
            module = importlib.import_module(package)

            version = getattr(module, "__version__", "unknown")

            print(
                f"[OK] {package} ({version}) - {description} ready"
            )

        except ImportError:
            print(
                f"[MISSING] {package} - {description} unavailable"
            )
            missing.append(package)

    return missing


def main():

    print(
        "LOADING STATUS: Loading programs...\n"
    )

    missing = check_dependencies()

    if missing:
        installation_help(missing)
        return

    data = generate_matrix_data()

    df = analyze_data(data)

    visualize(df)

    compare_dependencies()


if __name__ == "__main__":
    main()
