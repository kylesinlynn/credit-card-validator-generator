# Credit Card Validator and Generator

This project is a PyQt5 application that provides a user-friendly interface for validating and generating credit card numbers. It includes tabs for validation, generation, and information about the application.

## Features

- **Credit Card Validation**: Uses the Luhn algorithm to validate credit card numbers.
- **Credit Card Generation**: Generates valid credit card numbers with random expiration dates and identifies card types (Visa, MasterCard, American Express).
- **QR Code Generation**: Creates a QR code for the generated credit card number.
- **About Page**: Provides information about the application.

## Installation

### Requirements

- Python 3.x
- PyQt5
- qrcode
- Pillow

### Setup

1. **Clone the repository**:

   ```sh
   git clone https://github.com/kylesinlynn/credit-card-validator-generator.git
   cd credit-card-validator-generator
   ```

2. **Create and activate a virtual environment** (optional but recommended):

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies**:

   ```sh
   pip install -r requirements.txt
   ```

## Usage

1. **Run the application**:

   ```sh
   python main.py
   ```

2. **Navigate through tabs**:
   - **Validator Tab**: Enter a credit card number to validate its authenticity.
   - **Generator Tab**: Enter an initial number (optional) and generate a valid credit card number with details.
   - **About Tab**: View information about the application.

## Development

To contribute to this project, follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [PyQt5 Documentation](https://www.riverbankcomputing.com/static/Docs/PyQt5/)
- [qrcode Documentation](https://pypi.org/project/qrcode/)
- [Pillow Documentation](https://pillow.readthedocs.io/)
