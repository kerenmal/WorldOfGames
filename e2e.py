from selenium import webdriver
from MainScores import score_server
import sys

def test_scores_service():
    dr = webdriver.Chrome()
    dr.get(f"data:text/html,{score_server()}")
    score = dr.find_element(by="id", value="score").text
    try:
        assert 1 <= int(score) <= 1000
        return True
    except AssertionError:
        return False


def main():
    if test_scores_service():
        return 0
    else:
        return -1


if __name__ == "__main__":
    sys.exit(main())