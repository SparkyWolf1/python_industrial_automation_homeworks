# Dash application example
from dash import Dash
from Components.layout import create_layout
from data.load_data import load_data_csv

DATA_PATH = ""


def main() -> None:
    #data = load_data_csv(DATA_PATH)
    app = Dash()
    app.title = "Dash module example"
    app.layout = create_layout(app)
    app.run(debug=True)


# Run program
if __name__ == '__main__':
    main()
