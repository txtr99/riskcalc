# Trading Risk Calculator

Welcome to the Trading Risk Calculator. This handy Python tool helps you to calculate the risk and reward associated with your trading positions.

## Prerequisites

- Python 3.x installed. You can download it from [here](https://www.python.org/downloads/).

## Getting Started

Follow these steps to clone the repository, setup a virtual environment, install the required packages and run the application.

1. **Clone the repository**:

    In your terminal, navigate to the folder where you want to store the project and run the following command:
    ```bash
    git clone https://github.com/txtr99/riskcalc
    ```

2. **Navigate to the project folder**:
    ```bash
    cd trading-risk-calculator
    ```

3. **Create a virtual environment**:

    We recommend creating a virtual environment to keep the dependencies of this project separate from your other Python projects.
    ```bash
    python3 -m venv venv
    ```

4. **Activate the virtual environment**:

    - On macOS and Linux:
        ```bash
        source venv/bin/activate
        ```
    - On Windows:
        ```bash
        .\venv\Scripts\activate
        ```

5. **Upgrade pip**:

    It's usually a good idea to upgrade pip, the Python package installer, before installing any dependencies.
    ```bash
    pip install --upgrade pip
    ```

6. **Install the required packages**:

    The `requirements.txt` file lists all Python libraries that your project depends on. You can install them with:
    ```bash
    pip install -r requirements.txt
    ```

7. **Run the main script**:

    Now you're ready to run the trading risk calculator:
    ```bash
    python risk.py
    ```

8. **Provide the required inputs**:

    The script will prompt you to enter various inputs such as entry price, stoploss price, direction, TP prices and percents, account balance, and risk percent. If you don't provide a value for an optional input, the script will use a default value.

Enjoy using the Trading Risk Calculator!

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
