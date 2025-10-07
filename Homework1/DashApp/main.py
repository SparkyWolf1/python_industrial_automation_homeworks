# Dash application example
from dash import Dash
from Components.layout import create_layout
from data.load_data import load_data_csv


DATA_PATH = "DatasetsTesting\\Robot_Data\\dataset_02052023.csv"


def main() -> None:
    data = load_data_csv(DATA_PATH, list(range(0, 22)))
    app = Dash()
    app.title = "Dash module example"
    app.layout = create_layout(app, data)
    app.run(debug=True)


# Run program
if __name__ == '__main__':
    main()
