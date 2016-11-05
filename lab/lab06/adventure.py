from data import *

try:
    import readline
except ImportError:
    pass

###########
# Parsing #
###########

def adv_parse(line):
    tokens = line.split()
    if not tokens:
        raise SyntaxError('No command given')
    command = tokens.pop(0)
    if command in ('talk', 'go'):
        if not tokens or tokens[0] != 'to':
            raise SyntaxError('Did you mean "{}"?'.format(COMMAND_FORMATS[command]))
        return (command + '_to', ' '.join(tokens[1:]))
    elif command == 'check':
        if not tokens or tokens[0] != 'backpack':
            raise SyntaxError('Did you mean "{}"?'.format(COMMAND_FORMATS['check backpack']))
        return ('check_backpack', '')
    elif command == 'unlock':
        return ('unlock', ' '.join(tokens))
    else:
        return (command, ' '.join(tokens))

##############
# Evaluation #
##############

def adv_eval(exp):
    operator, operand = exp[0], exp[1]
    if operator not in COMMAND_NUM_ARGS:
        help()
        raise SyntaxError('Invalid command: {}'.format(operator))
    elif operator in SPECIAL_FORMS:
        function = SPECIAL_FORMS[operator]
    else:
        function = getattr(me, operator)

    if COMMAND_NUM_ARGS[operator] == 0:
        function()
    else:
        function(operand)

def help():
    print('There are {} possible commands:'.format(len(COMMAND_FORMATS)))
    for usage in COMMAND_FORMATS.values():
        print('   ', usage)

def check_win_state(player):
    """Checks if the player is in a winning state."""
    if player.place != woz:
        return False

    print()
    player_backpack = player.check_backpack()
    if 'Wallet' in player_backpack and 'Hotdog' in player_backpack:
        return True
    else:
        print()
        print("Looks like you're missing some items. Can't go to the project party yet!")
        return False

########
# REPL #
########

def read_eval_print_loop():
    print(WELCOME_MESSAGE)
    if not isinstance(me, Player):
        print('Oh no! You need to create a player at the bottom of data.py to start the game.')
        return

    help()
    while True:
        if check_win_state(me):
            print(WIN_MESSAGE)
            return
        print()
        try:
            line = input('adventure> ')
            exp = adv_parse(line)
            adv_eval(exp)
        except (KeyboardInterrupt, EOFError, SystemExit): # If you ctrl-c or ctrl-d
            print('\nGood game. Bye!')
            return
        # If the player input was badly formed or if something doesn't exist
        except SyntaxError as e:
            print('ERROR:', e)

#################
# Configuration #
#################

COMMAND_FORMATS = {
    'look': 'look',
    'go': 'go to [place]',
    'take': 'take [thing]',
    'talk': 'talk to [character]',
    'check backpack': 'check backpack',
    'help': 'help',
    'unlock': 'unlock [place]',
}

COMMAND_NUM_ARGS = {
    'look': 0,
    'go_to': 1,
    'take': 1,
    'talk_to': 1,
    'check_backpack': 0,
    'help': 0,
    'unlock': 1,
}

SPECIAL_FORMS = {
    'help': help,
}

WELCOME_MESSAGE = """
Welcome to the adventure game!

It's a bright sunny day.
You are a cute little squirrel named {},
wandering around Berkeley campus looking for food.

Let's go to FSM (Free Speech Movement Cafe)
and see what we can find there!
""".format(me.name if isinstance(me, Player) else '______')

WIN_MESSAGE = """
You arrive at the Wozniak Lounge just in time for the homework party!

John thanks you for finding his wallet.
James devours the hot dog you brought.

Congratulations! You won the adventure game!
"""


if __name__ == '__main__':
    read_eval_print_loop()