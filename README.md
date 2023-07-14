import PySide2

import matplotlib.pyplot as plt

def plot_function(function, min_x, max_x):
    """Plots the function."""
    x_values = np.linspace(min_x, max_x, 100)
    y_values = eval(function)
    plt.plot(x_values, y_values)
    plt.show()

def main():
    """Main function."""
    app = PySide2.QtWidgets.QApplication([])
    window = PySide2.QtWidgets.QWidget()
    window.setWindowTitle('Function Plotter')

    function_input = PySide2.QtWidgets.QLineEdit()
    function_input.setPlaceholderText('Enter function')

    min_x_input = PySide2.QtWidgets.QLineEdit()
    min_x_input.setPlaceholderText('Enter min x')

    max_x_input = PySide2.QtWidgets.QLineEdit()
    max_x_input.setPlaceholderText('Enter max x')

    plot_button = PySide2.QtWidgets.QPushButton('Plot')
    plot_button.clicked.connect(lambda: plot_function(function_input.text(), min_x_input.text(), max_x_input.text()))

    layout = PySide2.QtWidgets.QVBoxLayout()
    layout.addWidget(function_input)
    layout.addWidget(min_x_input)
    layout.addWidget(max_x_input)
    layout.addWidget(plot_button)

    window.setLayout(layout)
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
