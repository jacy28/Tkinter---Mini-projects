# 36. Chess Game with Move Validation
# •	GUI chessboard with pieces (Canvas)
# •	Enforce legal moves and turns
# •	Highlight possible moves
# •	Save/load games
# •	Optional: play vs computer (stockfish integration)

import tkinter as tk
from PIL import Image, ImageTk
import chess
import chess.svg
import cairosvg
import io

class ChessApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Chess Game with Move Validation")
        self.board = chess.Board()

        self.canvas = tk.Canvas(root, width=480, height=480)
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.on_click)

        self.selected_square = None
        self.draw_board()

        # Save/load buttons
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=5)

        tk.Button(btn_frame, text="Save Game", command=self.save_game).pack(side=tk.LEFT, padx=10)
        tk.Button(btn_frame, text="Load Game", command=self.load_game).pack(side=tk.LEFT)

    def draw_board(self):
        svg_board = chess.svg.board(self.board, size=480,
                                    lastmove=self.board.peek() if self.board.move_stack else None,
                                    coordinates=True)
        png_data = cairosvg.svg2png(bytestring=svg_board)
        image = Image.open(io.BytesIO(png_data))
        self.photo = ImageTk.PhotoImage(image)
        self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)

    def on_click(self, event):
        col = event.x // 60
        row = 7 - (event.y // 60)
        square = chess.square(col, row)

        if self.selected_square is None:
            piece = self.board.piece_at(square)
            if piece and piece.color == self.board.turn:
                self.selected_square = square
        else:
            move = chess.Move(self.selected_square, square)
            if move in self.board.legal_moves:
                self.board.push(move)
                self.selected_square = None
                self.draw_board()
                if self.board.is_checkmate():
                    self.show_message("Checkmate!")
                elif self.board.is_stalemate():
                    self.show_message("Stalemate.")
                elif self.board.is_insufficient_material():
                    self.show_message("Draw by insufficient material.")
            else:
                self.selected_square = None  # Reset if illegal move

    def show_message(self, message):
        tk.messagebox.showinfo("Game Over", message)

    def save_game(self):
        with open("saved_game.pgn", "w") as f:
            exporter = chess.pgn.FileExporter(f)
            game = chess.pgn.Game.from_board(self.board)
            game.accept(exporter)

    def load_game(self):
        try:
            with open("saved_game.pgn") as f:
                game = chess.pgn.read_game(f)
                self.board = game.end().board()
                self.selected_square = None
                self.draw_board()
        except Exception as e:
            print("Failed to load:", e)

if __name__ == "__main__":
    import tkinter.messagebox
    root = tk.Tk()
    app = ChessApp(root)
    root.mainloop()
