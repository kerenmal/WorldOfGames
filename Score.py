

def add_score(difficulty):
    POINTS_OF_WINNING = (int(difficulty) * 3) + 5
    try:
        file = open('Scores.txt', 'r+')
    except FileNotFoundError:
        file = open('Scores.txt', 'w+')
        file.write('0')
    file = open('Scores.txt', 'r+')
    current_points = int(file.read())
    file = open('Scores.txt', 'w+')
    file.seek(0)
    file.truncate()
    file = open('Scores.txt', 'r+')
    file.write(str(POINTS_OF_WINNING + current_points))
    file.close()

