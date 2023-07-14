import sys
import re
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PySide2.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class FunctionPlotter(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Function Plotter")
        self.setup_ui()

    def setup_ui(self):
        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        # Function input
        function_label = QLabel("Enter function (e.g., 5*x^3 + 2*x):")
        self.function_input = QLineEdit()

        # Range input
        range_label = QLabel("Enter range (min, max):")
        self.range_input = QLineEdit()

        # Plot button
        plot_button = QPushButton("Plot")
        plot_button.clicked.connect(self.plot_function)

        # Message label
        self.message_label = QLabel()
        self.message_label.setAlignment(Qt.AlignCenter)

        # Main layout
        layout = QVBoxLayout()
        layout.addWidget(function_label)
        layout.addWidget(self.function_input)
        layout.addWidget(range_label)
        layout.addWidget(self.range_input)
        layout.addWidget(plot_button)
        layout.addWidget(self.message_label)

        # Matplotlib figure
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)

        main_widget.setLayout(layout)

    def validate_input(self, function, x_min, x_max):
        # Check if function is empty
        if not function.strip():
            self.message_label.setText("Please enter a function.")
            return False

        # Check if range is empty
        if not x_min.strip() or not x_max.strip():
            self.message_label.setText("Please enter a range.")
            return False

        # Check if range values are numeric
        try:
            float(x_min)
            float(x_max)
        except ValueError:
            self.message_label.setText("Range values must be numeric.")
            return False

        # Check if x_min is less than x_max
        if float(x_min) >= float(x_max):
            self.message_label.setText("Minimum value must be less than maximum value.")
            return False

        # Check if function contains invalid characters
        pattern = r"[^\d\s\.\+\-\*\/\^\(\)x]"
        if re.search(pattern, function):
            self.message_label.setText("Invalid characters in the function.")
            return False

        # Check if function contains consecutive operators
        pattern = r"[\+\-\*\/\^]{2,}"
        if re.search(pattern, function):
            self.message_label.setText("Function contains consecutive operators.")
            return False

        return True

    def plot_function(self):
        self.message_label.clear()

        function = self.function_input.text()
        x_min, x_max = self.range_input.text().split(",")

        if not self.validate_input(function, x_min, x_max):
            return

        x_values = []
        y_values = []

        try:
            x_min = float(x_min)
            x_max = float(x_max)

            x = x_min
            while x <= x_max:
                x_values.append(x)
                y_values.append(eval(function.replace('^', '**')))
                x += 0.1

            self.figure.clear()
            ax = self.figure.add_subplot(111)
            ax.plot(x_values, y_values)
            ax.set_xlabel("x")
            ax.set_ylabel("f(x)")
            self.canvas.draw()

        except Exception as e:
            self.message_label.setText("An error occurred while plotting the function.")
            print(e)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FunctionPlotter()
    window.show()
    sys.exit(app.exec_())
