from utils import matches_screen

LOADING_REF = "images/loading_page_2.png"

def check_loading_screen():
    return matches_screen(LOADING_REF)