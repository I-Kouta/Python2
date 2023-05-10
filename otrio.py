# otrio
from flask import Flask, render_template, request

app = Flask(__name__)

# 3x3のボードを作成
board = [['', '', ''] for _ in range(3)]

# ボードにピースを配置する関数


def place_piece(board, row, col, piece):
    board[row][col] = piece

# ボードがすでに配置されているかどうかを確認する関数


def is_valid_move(board, row, col):
    return board[row][col] == ''

# ボードの状態を描画する関数


def render_board(board):
    return render_template('board.html', board=board)


@app.route('/')
def index():
    return render_board(board)


@app.route('/move', methods=['POST'])
def move():
    row = int(request.form['row'])
    col = int(request.form['col'])
    piece = request.form['piece']

    if is_valid_move(board, row, col):
        place_piece(board, row, col, piece)

    return render_board(board)


if __name__ == '__main__':
    app.run(debug=True)
