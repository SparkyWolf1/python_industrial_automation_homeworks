# Dash application example
from dash import Dash
from Components.layout import create_layout


def main() -> None:
    app = Dash()
    app.title = "Dash module example"
    app.layout = create_layout(app)
    app.run(debug=True)


# Run program
if __name__ == '__main__':
    main()
