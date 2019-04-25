TEXT_ON_BUTTONS = {
    "START_BUTTON": "START",
    "EXIT_BUTTON": "EXIT",
    "NEXT_BUTTON": "NEXT",
    "BACK_BUTTON": "BACK",
    "END_GAME": "END GAME"
}

MAIN_WINDOW_STYLES = "background-color: brown;"
MIN_WIDTH_OF_VERTICAL_LAYOUT = "min-width: 300px;"
START_LOGO_IMAGE = "assets/sapper.jpg"
START_LOGO_IMAGE_STYLES = MIN_WIDTH_OF_VERTICAL_LAYOUT + \
                          "border-image: url(" + START_LOGO_IMAGE + ") 1 1 1 1 stretch stretch;" + \
                          "border-width: auto;"

BOARD_SIZE = {
    "HEIGHT_MIN": 5,
    "HEIGHT_MAX": 25,
    "WIDTH_MIN": 5,
    "WIDTH_MAX": 25
}

INFORMATIVE_TEXTS = {
    "ENTER_THE_HEIGHT": "PODAJ WYSOKOŚĆ: ",
    "ENTER_THE_WIDTH": "PODAJ SZEROKOŚĆ: ",
    "ENTER_THE_NUMBER_OF_MINES": "PODAJ LICZBĘ MIN: ",
    "INFORM_ABOUT_THE_SCORE": "TWÓJ WYNIK TO: "
}

SIZE_LABEL_STYLES = "font-weight:bold; " \
                    "font-size: 15px;"

MINIMUM_AMOUNT_OF_MINES = 1

VALUES_OF_BOARD_FIELDS = {
    "INITIAL_VALUE_OF_THE_FIELD": "",
    "BOMB": "BOMB"
}

BOMB_ICON = 'assets/bomb.png'

GAME_BUTTONS_COLORS = {
    "INITIAL_COLOR": "background-color: blue;",
    "BOMB_COLOR": "background-color: #FF1730;",
    "COLOR_OF_REVEALED_FIELD": "background-color: #C0C0C0;",
}