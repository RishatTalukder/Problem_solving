# chess_pygame.py
# Run: python chess_pygame.py
# Requires: pygame (pip install pygame)

import pygame
import sys
import copy

pygame.init()
WIDTH, HEIGHT = 640, 680
BOARD_SIZE = 8
SQUARE = WIDTH // BOARD_SIZE
FPS = 60

# Colors
WHITE = (245, 245, 220)
BROWN = (118, 150, 86)
HIGHLIGHT = (246, 246, 105)
BLUE = (66, 135, 245)
RED = (220, 20, 60)
BLACK = (20, 20, 20)

# Unicode chess pieces (white/black)
UNICODE_PIECES = {
    'wK': '\u2654', 'wQ': '\u2655', 'wR': '\u2656', 'wB': '\u2657', 'wN': '\u2658', 'wP': '\u2659',
    'bK': '\u265A', 'bQ': '\u265B', 'bR': '\u265C', 'bB': '\u265D', 'bN': '\u265E', 'bP': '\u265F'
}

FONT = pygame.font.SysFont("DejaVu Sans", SQUARE - 8)
SMALL = pygame.font.SysFont("DejaVu Sans", 18)

def starting_board():
    # 8x8 board with strings: 'wP','bK', or None
    board = [[None]*8 for _ in range(8)]
    # pawns
    for i in range(8):
        board[1][i] = 'bP'
        board[6][i] = 'wP'
    # rooks
    board[0][0] = board[0][7] = 'bR'
    board[7][0] = board[7][7] = 'wR'
    # knights
    board[0][1] = board[0][6] = 'bN'
    board[7][1] = board[7][6] = 'wN'
    # bishops
    board[0][2] = board[0][5] = 'bB'
    board[7][2] = board[7][5] = 'wB'
    # queens & kings
    board[0][3] = 'bQ'
    board[0][4] = 'bK'
    board[7][3] = 'wQ'
    board[7][4] = 'wK'
    return board

class GameState:
    def __init__(self):
        self.board = starting_board()
        self.turn = 'w'  # 'w' or 'b'
        self.selected = None  # (r,c)
        self.legal_moves = []  # list of (r,c)
        self.move_log = []  # list of Move objects (for en-passant/castling history)
        self.white_can_castle_k = True
        self.white_can_castle_q = True
        self.black_can_castle_k = True
        self.black_can_castle_q = True
        self.en_passant_target = None  # coordinate (r,c) where en-passant is possible
        self.game_over = False
        self.result_text = ""

    def in_bounds(self, r, c):
        return 0 <= r < 8 and 0 <= c < 8

    def piece_at(self, r, c):
        return self.board[r][c]

    def find_king(self, color):
        for r in range(8):
            for c in range(8):
                p = self.board[r][c]
                if p == (color + 'K'):
                    return (r, c)
        return None

    def is_square_attacked(self, r, c, by_color):
        """Return True if square (r,c) is attacked by side by_color."""
        # For each opponent piece, generate its pseudo-legal attacks and see if hits (r,c)
        for rr in range(8):
            for cc in range(8):
                p = self.board[rr][cc]
                if p and p[0] == by_color:
                    typ = p[1]
                    moves = pseudo_legal_moves_for(self.board, rr, cc, p, only_attacks=True, en_passant_target=self.en_passant_target)
                    if (r, c) in moves:
                        return True
        return False

    def is_in_check(self, color):
        king_pos = self.find_king(color)
        if not king_pos:
            return True
        return self.is_square_attacked(king_pos[0], king_pos[1], 'b' if color=='w' else 'w')

    def generate_legal_moves(self, from_sq=None):
        """Generate all legal moves for current player. If from_sq provided, only from that square."""
        legal = []
        color = self.turn
        squares = []
        if from_sq:
            squares = [from_sq]
        else:
            for r in range(8):
                for c in range(8):
                    p = self.board[r][c]
                    if p and p[0] == color:
                        squares.append((r,c))
        for (r,c) in squares:
            p = self.board[r][c]
            if not p: continue
            pseudo = pseudo_legal_moves_for(self.board, r, c, p, en_passant_target=self.en_passant_target)
            for dest in pseudo:
                # simulate move on copy and check for own king in check
                board_copy = copy_board(self.board)
                move_obj = create_move_object(board_copy, (r,c), dest, p, self.en_passant_target)
                apply_move_on_board(board_copy, move_obj)
                gs_copy = GameState()
                gs_copy.board = board_copy
                gs_copy.en_passant_target = None  # after simulated move, ep target consumed
                if not gs_copy.is_in_check(color):
                    legal.append(((r,c), dest))
        return legal

    def make_move(self, from_pos, to_pos):
        if self.game_over:
            return False
        r0,c0 = from_pos
        r1,c1 = to_pos
        p = self.board[r0][c0]
        if not p or p[0] != self.turn:
            return False
        legal = [m for m in self.generate_legal_moves() if m[0]==(r0,c0) and m[1]==(r1,c1)]
        if not legal:
            return False
        move_obj = create_move_object(self.board, (r0,c0), (r1,c1), p, self.en_passant_target)
        apply_move_on_board(self.board, move_obj)
        # update castling rights
        if p == 'wK':
            self.white_can_castle_k = self.white_can_castle_q = False
        elif p == 'bK':
            self.black_can_castle_k = self.black_can_castle_q = False
        if p == 'wR' and r0==7 and c0==7:
            self.white_can_castle_k = False
        if p == 'wR' and r0==7 and c0==0:
            self.white_can_castle_q = False
        if p == 'bR' and r0==0 and c0==7:
            self.black_can_castle_k = False
        if p == 'bR' and r0==0 and c0==0:
            self.black_can_castle_q = False
        # if rook captured, update opponent's castle rights accordingly
        captured = move_obj.captured
        if captured == 'wR':
            if move_obj.to_pos == (7,0):
                self.white_can_castle_q = False
            if move_obj.to_pos == (7,7):
                self.white_can_castle_k = False
        if captured == 'bR':
            if move_obj.to_pos == (0,0):
                self.black_can_castle_q = False
            if move_obj.to_pos == (0,7):
                self.black_can_castle_k = False

        # manage en-passant target: if pawn moved 2 squares, set target
        if p[1] == 'P' and abs(r1 - r0) == 2:
            # square behind pawn
            ep_row = (r0 + r1) // 2
            self.en_passant_target = (ep_row, c0)
        else:
            # en-passant used? handled in apply_move_on_board; but reset if not newly set
            self.en_passant_target = None

        self.move_log.append(move_obj)
        # switch turn
        self.turn = 'b' if self.turn == 'w' else 'w'
        # reset selection
        self.selected = None
        # check for checkmate/stalemate
        legal_after = self.generate_legal_moves()
        if not legal_after:
            if self.is_in_check(self.turn):
                self.game_over = True
                self.result_text = f"Checkmate! {'White' if self.turn=='b' else 'Black'} wins."
            else:
                self.game_over = True
                self.result_text = "Stalemate!"
        return True

def copy_board(board):
    return [row[:] for row in board]

class MoveObj:
    def __init__(self, from_pos, to_pos, piece, captured=None, is_castle=False, is_ep=False, promotion=None):
        self.from_pos = from_pos
        self.to_pos = to_pos
        self.piece = piece
        self.captured = captured
        self.is_castle = is_castle
        self.is_ep = is_ep
        self.promotion = promotion

def create_move_object(board, from_pos, to_pos, piece, en_passant_target):
    r0,c0 = from_pos
    r1,c1 = to_pos
    captured = board[r1][c1]
    is_castle = False
    is_ep = False
    promotion = None
    # detect castling: king moves two squares horizontally
    if piece[1] == 'K' and abs(c1 - c0) == 2:
        is_castle = True
    # detect en-passant: pawn moves diagonally to empty square that is en_passant_target
    if piece[1] == 'P' and captured is None and c0 != c1:
        # it must be en-passant capture
        if en_passant_target == (r1, c1) or en_passant_target == (r1 + (1 if piece[0]=='w' else -1), c1):
            is_ep = True
            # captured pawn is behind the destination square
            cap_row = r1 + (1 if piece[0]=='w' else -1)
            captured = board[cap_row][c1]
    # promotion if pawn reaches last rank
    if piece[1] == 'P' and (r1 == 0 or r1 == 7):
        promotion = piece[0] + 'Q'  # auto promote to queen
    return MoveObj(from_pos, to_pos, piece, captured, is_castle, is_ep, promotion)

def apply_move_on_board(board, move):
    r0,c0 = move.from_pos
    r1,c1 = move.to_pos
    piece = move.piece
    # handle castling
    if move.is_castle:
        # king move already indicated; move rook accordingly
        board[r0][c0] = None
        board[r1][c1] = piece
        if c1 > c0:
            # kingside
            board[r1][c1-1] = board[r1][7]
            board[r1][7] = None
        else:
            # queenside
            board[r1][c1+1] = board[r1][0]
            board[r1][0] = None
        return
    # handle en-passant
    if move.is_ep and move.piece[1] == 'P':
        board[r0][c0] = None
        board[r1][c1] = piece
        cap_row = r1 + (1 if piece[0]=='w' else -1)
        board[cap_row][c1] = None
        return
    # normal capture / move
    board[r0][c0] = None
    board[r1][c1] = piece
    # promotion
    if move.promotion:
        board[r1][c1] = move.promotion

def pseudo_legal_moves_for(board, r, c, piece, only_attacks=False, en_passant_target=None):
    """Generate pseudo-legal moves (may leave king in check). 
    If only_attacks=True, pawns only produce diagonal captures (useful for attack detection)."""
    color = piece[0]
    typ = piece[1]
    moves = []
    if typ == 'P':
        dir = -1 if color == 'w' else 1
        start_row = 6 if color == 'w' else 1
        # forward move
        if not only_attacks:
            if in_board(r+dir, c) and board[r+dir][c] is None:
                moves.append((r+dir, c))
                if r == start_row and board[r+2*dir][c] is None:
                    moves.append((r+2*dir, c))
        # captures
        for dc in (-1,1):
            rr, cc = r+dir, c+dc
            if in_board(rr,cc):
                target = board[rr][cc]
                if target and target[0] != color:
                    moves.append((rr,cc))
                else:
                    # en-passant capture possibility: capture a pawn that moved two last turn and sits adjacent
                    if en_passant_target and (rr,cc) == en_passant_target:
                        moves.append((rr,cc))
    elif typ == 'N':
        deltas = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
        for dr,dc in deltas:
            rr,cc = r+dr, c+dc
            if in_board(rr,cc):
                t = board[rr][cc]
                if t is None or t[0] != color:
                    moves.append((rr,cc))
    elif typ == 'B' or typ == 'R' or typ == 'Q':
        dirs = []
        if typ in ('B','Q'):
            dirs += [(-1,-1),(-1,1),(1,-1),(1,1)]
        if typ in ('R','Q'):
            dirs += [(-1,0),(1,0),(0,-1),(0,1)]
        for dr,dc in dirs:
            rr,cc = r+dr, c+dc
            while in_board(rr,cc):
                t = board[rr][cc]
                if t is None:
                    moves.append((rr,cc))
                else:
                    if t[0] != color:
                        moves.append((rr,cc))
                    break
                rr += dr; cc += dc
    elif typ == 'K':
        for dr in (-1,0,1):
            for dc in (-1,0,1):
                if dr==0 and dc==0: continue
                rr,cc = r+dr, c+dc
                if in_board(rr,cc):
                    t = board[rr][cc]
                    if t is None or t[0] != color:
                        moves.append((rr,cc))
        # castling (only if not only_attacks)
        if not only_attacks:
            if color == 'w':
                king_row = 7
                # kingside
                if board[r][c] == 'wK' and r==7 and c==4:
                    # squares must be empty and rook present
                    if board[7][5] is None and board[7][6] is None and board[7][7]=='wR':
                        moves.append((7,6))
                    # queenside
                    if board[7][1] is None and board[7][2] is None and board[7][3] is None and board[7][0]=='wR':
                        moves.append((7,2))
            else:
                if board[r][c] == 'bK' and r==0 and c==4:
                    if board[0][5] is None and board[0][6] is None and board[0][7]=='bR':
                        moves.append((0,6))
                    if board[0][1] is None and board[0][2] is None and board[0][3] is None and board[0][0]=='bR':
                        moves.append((0,2))
    return moves

def in_board(r,c):
    return 0 <= r < 8 and 0 <= c < 8

# UI functions
def draw_board(screen, gs):
    screen.fill(BLACK)
    # draw chessboard
    for r in range(8):
        for c in range(8):
            rect = pygame.Rect(c*SQUARE, r*SQUARE, SQUARE, SQUARE)
            color = BROWN if (r+c)%2 else WHITE
            pygame.draw.rect(screen, color, rect)
    # highlight selected
    if gs.selected:
        r,c = gs.selected
        srect = pygame.Rect(c*SQUARE, r*SQUARE, SQUARE, SQUARE)
        pygame.draw.rect(screen, HIGHLIGHT, srect)
    # highlight legal moves
    for m in gs.generate_legal_moves(from_sq=gs.selected) if gs.selected else []:
        dest = m[1]
        rect = pygame.Rect(dest[1]*SQUARE, dest[0]*SQUARE, SQUARE, SQUARE)
        pygame.draw.rect(screen, BLUE, rect, width=4)

    # draw pieces
    for r in range(8):
        for c in range(8):
            piece = gs.board[r][c]
            if piece:
                glyph = UNICODE_PIECES.get(piece, '?')
                text = FONT.render(glyph, True, BLACK if piece[0]=='w' else WHITE)
                text_rect = text.get_rect(center=(c*SQUARE+SQUARE//2, r*SQUARE+SQUARE//2))
                screen.blit(text, text_rect)
    # draw bottom bar with turn and status
    bar_rect = pygame.Rect(0, 8*SQUARE, WIDTH, HEIGHT - 8*SQUARE)
    pygame.draw.rect(screen, (200,200,200), bar_rect)
    turn_txt = SMALL.render(f"Turn: {'White' if gs.turn=='w' else 'Black'}", True, BLACK)
    screen.blit(turn_txt, (10, 8*SQUARE+8))
    if gs.game_over:
        rez = SMALL.render(gs.result_text, True, RED)
        screen.blit(rez, (160, 8*SQUARE+8))
    # move log last move
    if gs.move_log:
        m = gs.move_log[-1]
        last = SMALL.render(f"Last: {pretty_move(m)}", True, BLACK)
        screen.blit(last, (10, 8*SQUARE+30))

def pretty_move(m):
    fx,fy = m.from_pos
    tx,ty = m.to_pos
    return f"{chr(fy+97)}{8-fx}->{chr(ty+97)}{8-tx}"

def get_square_under_mouse(pos):
    x,y = pos
    if y >= 8*SQUARE:
        return None
    c = x // SQUARE
    r = y // SQUARE
    return (r,c)

def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pygame Chess")
    clock = pygame.time.Clock()
    gs = GameState()

    running = True
    while running:
        clock.tick(FPS)
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                running = False
                break
            elif ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                sq = get_square_under_mouse(ev.pos)
                if sq:
                    r,c = sq
                    piece = gs.board[r][c]
                    if gs.selected:
                        # attempt move
                        moved = gs.make_move(gs.selected, (r,c))
                        if not moved:
                            # if clicking another of own pieces, change selection
                            if piece and piece[0] == gs.turn:
                                gs.selected = (r,c)
                            else:
                                gs.selected = None
                        else:
                            # success: selection cleared by make_move
                            pass
                    else:
                        # select if own piece
                        if piece and piece[0] == gs.turn:
                            gs.selected = (r,c)
            elif ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_r:
                    gs = GameState()  # reset
        draw_board(screen, gs)
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
