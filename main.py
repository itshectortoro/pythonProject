from settings import * 
from sprites import * 
from groups import AllSprites
import json

class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Pong')
        self.clock = pygame.time.Clock()
        self.running = True
    
        # sprites 
        self.all_sprites = AllSprites()
        self.paddle_sprites = pygame.sprite.Group()
        self.player = Player((self.all_sprites, self.paddle_sprites))
        self.ball = Ball(self.all_sprites, self.paddle_sprites, self.update_score)
        Opponent((self.all_sprites, self.paddle_sprites), self.ball)

        # score 
        try:
            with open(join('data', 'score.txt')) as score_file:
                self.score = json.load(score_file)
        except:
            self.score = {'player': 0, 'opponent': 0}
        self.font = pygame.font.Font(None, 160)

    def display_score(self):
        # player 
        player_surf = self.font.render(str(self.score['player']), True, COLORS['bg detail'])
        player_rect = player_surf.get_rect(center = (WINDOW_WIDTH / 2 + 100, WINDOW_HEIGHT / 2))
        self.display_surface.blit(player_surf, player_rect)

        # opponent
        opponent_surf = self.font.render(str(self.score['opponent']), True, COLORS['bg detail'])
        opponent_rect = opponent_surf.get_rect(center = (WINDOW_WIDTH / 2 - 100, WINDOW_HEIGHT / 2))
        self.display_surface.blit(opponent_surf, opponent_rect)

        # line separator
        pygame.draw.line(self.display_surface, COLORS['bg detail'], (WINDOW_WIDTH /2, 0), (WINDOW_WIDTH /2, WINDOW_HEIGHT), 6)

    def update_score(self, side):
        self.score['player' if side == 'player' else 'opponent'] += 1

    def run(self):
        while self.running:
            dt = self.clock.tick() / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    with open(join('Pong', 'data', 'score.txt'), 'w') as score_file:
                        json.dump(self.score, score_file)
            
            # update 
            self.all_sprites.update(dt)

            # draw 
            self.display_surface.fill(COLORS['bg'])
            self.display_score()
            self.all_sprites.draw()
            pygame.display.update()
        pygame.quit()

if __name__ == '__main__':
    game = Game()
    game.run()
import random

word_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon",
             "mango", "nectarine", "orange", "papaya", "quince", "raspberry", "strawberry", "tangerine", "ugli",
             "vital", "watermelon", "yellowfruit", "zucchini", "abacus", "abandon", "abduct", "ability",
             "able", "absence", "absorb", "absurd", "accent", "accept", "access", "accident", "acclaim", "accord",
             "accuse", "achieve", "acquire", "address", "advance", "advice", "affect", "afford", "against", "agency",
             "alcohol", "allege", "alpine", "alter", "amazing", "ancient", "analyze", "animal", "annual", "answer",
             "anxiety", "applied", "approve", "around", "arrival", "arrive", "article", "artist", "aspect", "assault",
             "assert", "assess", "assure", "attain", "attempt", "average", "ballet", "battery", "bitter", "blanket",
             "bother", "bottle", "bottom", "bounce", "bracket", "bricks", "brides", "brother", "buckle", "buffer",
             "cabinet", "cattle", "chance", "change", "charge", "charms", "cherry", "choice", "choose", "church",
             "circle", "clutch", "courage", "coyote", "crater", "crisis", "crunch", "debate", "decade", "dental",
             "deploy", "design", "devote", "digest", "direct", "doubt", "douse", "drought", "duty", "echoes", "elbow",
             "enemy", "enrich", "enroll", "envoy", "escape", "escalate", "essay", "evoke", "exact", "examine", "expose",
             "extend", "extract", "facing", "famous", "fence", "final", "finish", "flame", "flour", "focus", "follow",
             "forbid", "force", "fortify", "found", "future", "gadget", "gather", "genuine", "giant", "global", "glove",
             "grasp", "grill", "group", "guilt", "gush", "habit", "hatch", "haunt", "hectic", "honey", "honor", "hover",
             "impact", "impose", "induce", "input", "invite", "island", "jacket", "juggle", "judge", "jumpy", "latch",
             "laugh", "leaf", "leap", "light", "liver", "lobby", "lunar", "luxury", "mango", "march", "merge", "mice",
             "model", "motor", "mouth", "music", "mutate", "mystic", "naive", "nurse", "number", "obtain", "occur",
             "olympic", "opera", "orbit", "order", "other", "outfit", "owner", "pace", "paint", "pause", "pencil",
             "pepper", "phase", "phone", "phrase", "place", "plaza", "point", "prize", "proof", "punch", "purse",
             "quote", "racket", "reach", "react", "reason", "rectify", "relax", "remedy", "repeat", "rescue", "result",
             "revise", "rider", "right", "robot", "sacred", "scout", "search", "sector", "shame", "sheet", "shock",
             "short", "shine", "slice", "slope", "smile", "splash", "stain", "stark", "start", "steel", "stool",
             "straw",
             "swarm", "swirl", "tackle", "tapes", "theme", "thick", "throne", "toxin", "towel", "track", "train",
             "trend",
             "treat", "troop", "truth", "under", "unity", "upper", "usage", "vigor", "visit", "vowel", "wager", "waste",
             "water", "wave", "wheel", "whisk", "wrack", "wrist", "write", "zebra", "zenith", "zone", "zoom"]


def get_word():
    term = random.choice(word_list)
    return term.upper()


def play(term):
    word_completion = "_" * len(term)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 0
    print("Let's test your word skills with a game of hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries < 6:
        guess = input("Please guess a letter or word:").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in term:
                print(guess, "is not in the word.")
                tries += 1
                guessed_letters.append(guess)
            else:
                print("Correct!", guess, "is in the word!")
                guessed_letters.append(guess)
        word_as_list = list(word_completion)
        indices = [i for i, letter in enumerate(term) if letter == guess]
        for index in indices:
            word_as_list[index] = guess
            word_completion = "".join(word_as_list)
            if "_" not in word_completion:
                guessed = True
        if len(guess) == len(term) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != term:
                print(guess, "is not the word.")
                tries += 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = term
        else:
            print("Not a valid guess.")
        print(display_hangman(tries))
        print(word_completion)
        print('Guessed Letters:',guessed_letters)
        print("\n")
    if guessed:
        print("Congrats, you guessed the word! You win!")
    else:
        print("Sorry you ran out of tries, better luck next time! The word was" + term)


def display_hangman(tries):
    stages = ["""
     -----
     |   |
         |
         |
         |
         |
    ------
    """,
              """
                -----
                |   |
                O   |
                    |
                    |
                    |
               ------
               """,
              """
                -----
                |   |
                O   |
                |   |
                    |
                    |
               ------
               """,
              """
                -----
                |   |
                O   |
               /|   |
                    |
                    |
               ------
               """,
              """
                -----
                |   |
                O   |
               /|\  |
                    |
                    |
               ------
               """,
              """
                -----
                |   |
                O   |
               /|\  |
               /    |
                    |
               ------
               """,
              """
                -----
                |   |
                O   |
               /|\  |
               / \  |
                    |
               ------
               """]
    return stages[tries]


def main():
    term = get_word()
    play(term)
    while input("Play Again? (Y/N) ").upper() == "Y":
        gword = get_word()
        play(term)


if __name__ == '__main__':
    main()