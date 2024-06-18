
from random import randint
class Colors:
    # Reset
    end = '\033[0m'
    
    # Regular Colors
    black = '\033[30m'
    red = '\033[31m'
    green = '\033[32m'
    yellow = '\033[33m'
    blue = '\033[34m'
    magenta = '\033[35m'
    cyan = '\033[36m'
    white = '\033[37m'
    orange = '\033[38;5;214m'
    pink = '\033[38;5;205m'

    # Bold
    bold_black = '\033[1;30m'
    bold_red = '\033[1;31m'
    bold_green = '\033[1;32m'
    bold_yellow = '\033[1;33m'
    bold_blue = '\033[1;34m'
    bold_magenta = '\033[1;35m'
    bold_cyan = '\033[1;36m'
    bold_white = '\033[1;37m'

    # Underline
    underline_black = '\033[4;30m'
    underline_red = '\033[4;31m'
    underline_green = '\033[4;32m'
    underline_yellow = '\033[4;33m'
    underline_blue = '\033[4;34m'
    underline_magenta = '\033[4;35m'
    underline_cyan = '\033[4;36m'
    underline_white = '\033[4;37m'

    # Background
    background_black = '\033[40m'
    background_red = '\033[41m'
    background_green = '\033[42m'
    background_yellow = '\033[43m'
    background_blue = '\033[44m'
    background_magenta = '\033[45m'
    background_cyan = '\033[46m'
    background_white = '\033[47m'

    # High Intensity
    high_intens_black = '\033[90m'
    high_intens_red = '\033[91m'
    high_intens_green = '\033[92m'
    high_intens_yellow = '\033[93m'
    high_intens_blue = '\033[94m'
    high_intens_magenta = '\033[95m'
    high_intens_cyan = '\033[96m'
    high_intens_white = '\033[97m'

    # High Intensity backgrounds
    high_intens_background_black = '\033[100m'
    high_intens_background_red = '\033[101m'
    high_intens_background_green = '\033[102m'
    high_intens_background_yellow = '\033[103m'
    high_intens_background_blue = '\033[104m'
    high_intens_background_magenta = '\033[105m'
    high_intens_background_cyan = '\033[106m'
    high_intens_background_white = '\033[107m'

    # High Intensity underline
    high_intens_underline_black = '\033[4;90m'
    high_intens_underline_red = '\033[4;91m'
    high_intens_underline_green = '\033[4;92m'
    high_intens_underline_yellow = '\033[4;93m'
    high_intens_underline_blue = '\033[4;94m'
    high_intens_underline_magenta = '\033[4;95m'
    high_intens_underline_cyan = '\033[4;96m'
    high_intens_underline_white = '\033[4;97m'

    # High Intensity backgrounds underline
    high_intens_background_underline_black = '\033[4;100m'
    high_intens_background_underline_red = '\033[4;101m'
    high_intens_background_underline_green = '\033[4;102m'
    high_intens_background_underline_yellow = '\033[4;103m'
    high_intens_background_underline_blue = '\033[4;104m'
    high_intens_background_underline_magenta = '\033[4;105m'
    high_intens_background_underline_cyan = '\033[4;106m'
    high_intens_background_underline_white = '\033[4;107m'

    