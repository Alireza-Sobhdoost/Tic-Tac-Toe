import pygame
import sys
from Board import *
from Mcts import *

# --- Window Setup ---
WINDOW_SIZE = 600
FPS = 60
BOARD_MARGIN = 50
CELL_SIZE = (WINDOW_SIZE - 2 * BOARD_MARGIN) // 3

# --- Colors ---
BG_COLOR = (10, 10, 20)
GRID_COLOR = (180, 0, 255)      # purple glow
X_COLOR = (255, 30, 30)         # neon red
O_COLOR = (0, 180, 255)         # neon blue
TEXT_COLOR = (255, 255, 255)

pygame.init()
FONT = pygame.font.SysFont("Orbitron", 36, bold=True)
LARGE_FONT = pygame.font.SysFont("Orbitron", 52, bold=True)
SCREEN = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE + 100))
pygame.display.set_caption("Tic Tac Toe — Neon Edition")
CLOCK = pygame.time.Clock()



# --- Utility Functions ---
def neon_line(surface, color, start_pos, end_pos, width=1, glow=15):
    """Draws a neon-style line with glow effect."""
    for i in range(glow, 0, -3):
        alpha = max(10, int(255 * (i / glow)))
        glow_color = (*color, alpha)
        glow_surface = pygame.Surface(surface.get_size(), pygame.SRCALPHA)
        pygame.draw.line(glow_surface, glow_color, start_pos, end_pos, width + i)
        surface.blit(glow_surface, (0, 0))
    pygame.draw.line(surface, color, start_pos, end_pos, width)


def neon_circle(surface, color, center, radius, width=3, glow=15):
    """Draws a glowing neon circle."""
    for i in range(glow, 0, -3):
        alpha = max(10, int(255 * (i / glow)))
        glow_color = (*color, alpha)
        glow_surface = pygame.Surface(surface.get_size(), pygame.SRCALPHA)
        pygame.draw.circle(glow_surface, glow_color, center, radius + i // 2, width)
        surface.blit(glow_surface, (0, 0))
    pygame.draw.circle(surface, color, center, radius, width)


def neon_x(surface, color, center, size, width=4, glow=15):
    """Draws a glowing neon X."""
    offset = size // 2
    for i in range(glow, 0, -3):
        alpha = max(10, int(255 * (i / glow)))
        glow_color = (*color, alpha)
        glow_surface = pygame.Surface(surface.get_size(), pygame.SRCALPHA)
        pygame.draw.line(glow_surface, glow_color,
                         (center[0] - offset - i//3, center[1] - offset - i//3),
                         (center[0] + offset + i//3, center[1] + offset + i//3),
                         width + i)
        pygame.draw.line(glow_surface, glow_color,
                         (center[0] + offset + i//3, center[1] - offset - i//3),
                         (center[0] - offset - i//3, center[1] + offset + i//3),
                         width + i)
        surface.blit(glow_surface, (0, 0))
    pygame.draw.line(surface, color, (center[0] - offset, center[1] - offset),
                     (center[0] + offset, center[1] + offset), width)
    pygame.draw.line(surface, color, (center[0] + offset, center[1] - offset),
                     (center[0] - offset, center[1] + offset), width)


def draw_board(surface, board):
    """Draw glowing grid and pieces."""
    surface.fill(BG_COLOR)

    # Draw grid
    start = BOARD_MARGIN
    for i in range(1, 3):
        x = start + i * CELL_SIZE
        neon_line(surface, GRID_COLOR, (x, start), (x, start + 3 * CELL_SIZE), 1, glow=20)
        y = start + i * CELL_SIZE
        neon_line(surface, GRID_COLOR, (start, y), (start + 3 * CELL_SIZE, y), 1, glow=20)

    # Draw X and O
    for r in range(3):
        for c in range(3):
            val = board.position[r, c]
            if val == '.':
                continue
            cx = start + c * CELL_SIZE + CELL_SIZE // 2
            cy = start + r * CELL_SIZE + CELL_SIZE // 2
            if val == 'x':
                neon_x(surface, X_COLOR, (cx, cy), CELL_SIZE // 2)
            elif val == 'o':
                neon_circle(surface, O_COLOR, (cx, cy), CELL_SIZE // 3)


def pixel_to_cell(pos):
    x, y = pos
    start = BOARD_MARGIN
    if x < start or y < start or x > start + 3 * CELL_SIZE or y > start + 3 * CELL_SIZE:
        return None
    col = (x - start) // CELL_SIZE
    row = (y - start) // CELL_SIZE
    return (int(row), int(col))


def draw_message(surface, text):
    txt = FONT.render(text, True, TEXT_COLOR)
    rect = txt.get_rect(center=(WINDOW_SIZE // 2, WINDOW_SIZE + 50))
    surface.blit(txt, rect)


# --- Main Loop ---
def run_gui(iterates):
    GAME_BOARD = Board()
    mcts = MCTS()
    message = f"{GAME_BOARD.player_1.upper()} to move"
    winner = None
    running = True

    while running:
        CLOCK.tick(FPS)
        draw_board(SCREEN, GAME_BOARD)
        draw_message(SCREEN, message)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if winner:  # Restart on click after game over
                    GAME_BOARD = Board()
                    mcts = MCTS()
                    winner = None
                    message = f"{GAME_BOARD.player_1.upper()} to move"
                    continue

                cell = pixel_to_cell(event.pos)
                if not cell:
                    continue

                # Player move
                Result = GAME_BOARD.make_move(cell)
                if Result is None:
                    message = "Invalid move!"
                    continue

                GAME_BOARD = Result
                winner = GAME_BOARD.check_winner()
                if winner:
                    message = f"{winner.upper()} wins!"
                    continue

                if GAME_BOARD.check_draw() == 0:
                    message = "It's a draw!"
                    winner = "draw"
                    continue

                # Computer move
                message = "Computer thinking..."
                draw_board(SCREEN, GAME_BOARD)
                draw_message(SCREEN, message)
                pygame.display.flip()

                best_move = mcts.search(GAME_BOARD, iterates)
                GAME_BOARD = best_move.board

                winner = GAME_BOARD.check_winner()
                if winner:
                    message = f"{winner.upper()} wins!"
                    continue

                if GAME_BOARD.check_draw() == 0:
                    message = "It's a draw!"
                    winner = "draw"
                else:
                    message = f"{GAME_BOARD.player_1.upper()} to move"

        # End-of-game overlay
        if winner:
            overlay = pygame.Surface((WINDOW_SIZE, WINDOW_SIZE), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 140))
            SCREEN.blit(overlay, (0, 0))
            text = LARGE_FONT.render("GAME OVER", True, TEXT_COLOR)
            sub = FONT.render(message, True, TEXT_COLOR)
            SCREEN.blit(text, text.get_rect(center=(WINDOW_SIZE // 2, WINDOW_SIZE // 2 - 20)))
            SCREEN.blit(sub, sub.get_rect(center=(WINDOW_SIZE // 2, WINDOW_SIZE // 2 + 30)))

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    iterates = int(sys.argv[-1])
    run_gui(iterates)
