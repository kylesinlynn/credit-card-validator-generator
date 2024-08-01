import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTabWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QFormLayout
from PyQt5.QtGui import QPixmap
import random
import qrcode
from PIL.ImageQt import ImageQt

class CreditCardApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Credit Card Validator and Generator")
        self.setGeometry(100, 100, 800, 600)

        self.layout = QVBoxLayout()
        self.tabs = QTabWidget()
        
        # Create tabs
        self.create_validator_tab()
        self.create_generator_tab()
        self.create_about_tab()

        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    def create_validator_tab(self):
        self.validator_tab = QWidget()
        self.tabs.addTab(self.validator_tab, "Validator")

        self.validator_layout = QVBoxLayout()

        self.validation_input = QLineEdit(self)
        self.validation_input.setPlaceholderText("Enter credit card number")
        self.validator_layout.addWidget(self.validation_input)

        self.validate_button = QPushButton("Validate Credit Card", self)
        self.validate_button.clicked.connect(self.validate_card)
        self.validator_layout.addWidget(self.validate_button)

        self.validation_result = QLabel("", self)
        self.validator_layout.addWidget(self.validation_result)

        self.validator_tab.setLayout(self.validator_layout)

    def create_generator_tab(self):
        self.generator_tab = QWidget()
        self.tabs.addTab(self.generator_tab, "Generator")

        self.generator_layout = QVBoxLayout()

        self.generator_input = QLineEdit(self)
        self.generator_input.setPlaceholderText("Enter initial number (optional)")
        self.generator_layout.addWidget(self.generator_input)

        self.generate_button = QPushButton("Generate Credit Card", self)
        self.generate_button.clicked.connect(self.generate_credit_card)
        self.generator_layout.addWidget(self.generate_button)

        self.generated_card_label = QLabel("", self)
        self.generator_layout.addWidget(self.generated_card_label)

        self.generated_card_type_label = QLabel("", self)
        self.generator_layout.addWidget(self.generated_card_type_label)

        self.generated_expiration_label = QLabel("", self)
        self.generator_layout.addWidget(self.generated_expiration_label)

        self.generated_qr_label = QLabel(self)
        self.generator_layout.addWidget(self.generated_qr_label)

        self.generator_tab.setLayout(self.generator_layout)

    def create_about_tab(self):
        self.about_tab = QWidget()
        self.tabs.addTab(self.about_tab, "About")

        self.about_layout = QVBoxLayout()

        self.about_text = QLabel("Credit Card Validator and Generator\n\nVersion 1.0\n\nDeveloped by Kyle Sin Lynn", self)
        self.about_layout.addWidget(self.about_text)

        self.about_tab.setLayout(self.about_layout)

    def validate_card(self):
        card_number = self.validation_input.text().strip()
        if not card_number:
            self.validation_result.setText("Please enter a credit card number.")
            return
        if self.validate_credit_card(card_number):
            self.validation_result.setText("Valid Credit Card Number")
        else:
            self.validation_result.setText("Invalid Credit Card Number")

    def validate_credit_card(self, card_number):
        def digits_of(n):
            return [int(d) for d in str(n)]
        digits = digits_of(card_number)
        odd_digits = digits[-1::-2]
        even_digits = digits[-2::-2]
        checksum = sum(odd_digits)
        for d in even_digits:
            checksum += sum(digits_of(d * 2))
        return checksum % 10 == 0

    def generate_credit_card(self):
        initial_number = self.generator_input.text().strip()
        if initial_number and self.validate_credit_card(initial_number):
            generated_number = initial_number
        else:
            generated_number = self.generate_random_credit_card()

        card_data = {
            "number": generated_number,
            "month": random.randint(1, 12),
            "year": random.randint(23, 30),
            "type": self.get_card_type(generated_number)
        }
        
        self.generated_card_label.setText(f"Generated Credit Card: {card_data['number']}")
        self.generated_card_type_label.setText(f"Card Type: {card_data['type']}")
        self.generated_expiration_label.setText(f"Expiration Date: {card_data['month']:02}/{card_data['year']}")
        self.display_qr_code(card_data['number'])

    def generate_random_credit_card(self):
        prefixes = {
            "Visa": "4",
            "MasterCard": "5",
            "American Express": "3"
        }
        card_type = random.choice(list(prefixes.keys()))
        prefix = prefixes[card_type]
        while True:
            number = prefix + "".join([str(random.randint(0, 9)) for _ in range(15 if card_type == "American Express" else 12)])
            if self.validate_credit_card(number):
                return number

    def get_card_type(self, number):
        if number.startswith("4"):
            return "Visa"
        elif number.startswith("5"):
            return "MasterCard"
        elif number.startswith("3"):
            return "American Express"
        else:
            return "Unknown"

    def display_qr_code(self, text):
        qr = qrcode.QRCode()
        qr.add_data(text)
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='white')
        qt_img = ImageQt(img)
        pixmap = QPixmap.fromImage(qt_img)
        self.generated_qr_label.setPixmap(pixmap)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = CreditCardApp()
    main_win.show()
    sys.exit(app.exec_())
