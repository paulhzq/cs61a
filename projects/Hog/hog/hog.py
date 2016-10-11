"""CS 61A Presents The Game of Hog."""

from dice import four_sided, six_sided, make_test_dice
from ucb import main, trace, log_current_line, interact

GOAL_SCORE = 100  # The goal of Hog is to score 100 points.


######################
# Phase 1: Simulator #
######################

def roll_dice(num_rolls, dice=six_sided):
    """Simulate rolling the DICE exactly NUM_ROLLS>0 times. Return the sum of
    the outcomes unless any of the outcomes is 1. In that case, return the
    number of 1's rolled.
    """
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    # BEGIN PROBLEM 1
    
    times_dice_1,result_dice,total=0,0,0#times_dice_1 records the number of 1's rolled,result_dice record each time the outcomes,Total record the sum of the outcome.
    while num_rolls>0:
        result_dice = dice()
        num_rolls-=1
        if result_dice ==1:
            times_dice_1+=1
        else:
            total+=result_dice

    if times_dice_1>0:
        return times_dice_1#Pig Out
    else:
        return total


    # END PROBLEM 1


def free_bacon(opponent_score):
    """Return the points scored from rolling 0 dice (Free Bacon)."""
    # BEGIN PROBLEM 2
    if opponent_score>=10:
        return 1+max(opponent_score%10,(opponent_score//10)%10)
    else:
        return 1+opponent_score

    # END PROBLEM 2


# Write your prime functions here!
def is_prime(score):
    """Check the score is prime number or not 

    >>> is_prime(1)
    False
    >>> is_prime(2)
    True
    >>> is_prime(4)
    False

    """
    if score == 1:
        return False
    n =2
    while n<score:
        if score %n ==0:
            return False
        n+=1
    return True

def next_prime(score):
    next =score+1
    while not is_prime(next):
        next +=1
    return next 


def take_turn(num_rolls, opponent_score, dice=six_sided):
    """Simulate a turn rolling NUM_ROLLS dice, which may be 0 (Free Bacon).
    Return the points scored for the turn by the current player. Also
    implements the Hogtimus Prime and When Pigs Fly rules.

    num_rolls:       The number of dice rolls that will be made.
    opponent_score:  The total score of the opponent.
    dice:            A function of no args that returns an integer outcome.
    """
    # Leave these assert statements here; they help check for errors.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice in take_turn.'
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
    assert opponent_score < 100, 'The game should be over.'
    # BEGIN PROBLEM 2
    
    final_score = 0
    if num_rolls == 0:
        final_score = free_bacon(opponent_score)
    else:
        final_score = roll_dice(num_rolls,dice)
    if is_prime(final_score): #Hogtimus Prime.
        final_score = next_prime(final_score)
    if final_score>(25-num_rolls):# When Pigs Fly.
        final_score = 25-num_rolls
    return final_score

    # END PROBLEM 2


def reroll(dice):
    """Return dice that return even outcomes and re-roll odd outcomes of DICE."""
    def rerolled():
        # BEGIN PROBLEM 3
        outcome = dice()
        if outcome % 2 ==0:
            return outcome
        else:
            outcome =dice()
            return outcome 
        # END PROBLEM 3
    return rerolled


def select_dice(score, opponent_score, dice_swapped):
    """Return the dice used for a turn, which may be re-rolled (Hog Wild) and/or
    swapped for four-sided dice (Pork Chop).

    DICE_SWAPPED is True if and only if four-sided dice are being used.
    """
    # BEGIN PROBLEM 4
    
    if dice_swapped:
        dice = four_sided
    else:
        dice = six_sided  # Replace this statement
    # END PROBLEM 4
    if (score + opponent_score) % 7 == 0:
        dice = reroll(dice)
    return dice


def other(player):
    """Return the other player, for a player PLAYER numbered 0 or 1.

    >>> other(0)
    1
    >>> other(1)
    0
    """
    return 1 - player


def play(strategy0, strategy1, score0=0, score1=0, goal=GOAL_SCORE):
    """Simulate a game and return the final scores of both players, with
    Player 0's score first, and Player 1's score second.

    A strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    strategy0:  The strategy function for Player 0, who plays first
    strategy1:  The strategy function for Player 1, who plays second
    score0   :  The starting score for Player 0
    score1   :  The starting score for Player 1
    """
    #assert score0<goal,'Game over'
    #assert score1<goal,'Game over'

    player = 0  # Which player is about to take a turn, 0 (first) or 1 (second)
    dice_swapped = False  # Whether 4-sided dice have been swapped for 6-sided
    # BEGIN PROBLEM 5
    "*** REPLACE THIS LINE ***"
    while score0<goal and score1<goal:
        if player == 0:#first player's turn
            num_rolls=strategy0(score0,score1)# Player 0's strategy function,return the number of dice that player want to roll
            if num_rolls ==-1:# Pork Chop 
                score0+=1 
                dice_swapped = not dice_swapped # swap the dice
            else:
                score0+=take_turn(num_rolls,score1,select_dice(score0,score1,dice_swapped)) #update the palyer 0 's scores.
            
        else:#1 second player's turn
            num_rolls= strategy1(score1,score0)
            if num_rolls ==-1:
                score1+=1
                dice_swapped = not dice_swapped
            else:
                score1+= take_turn(num_rolls,score0,select_dice(score1,score0,dice_swapped))
            #if (score0+score1)//7 ==0:
                #score1 = select_dice(score1,score0,dice_swapped)
        
        if 2*score0 == score1 or 2*score1==score0: #Swine Swap,one of the scores is double the other,swip the score.
            score0,score1=score1,score0
        player = other(player)


    # END PROBLEM 5
    return score0, score1


#######################
# Phase 2: Strategies #
#######################

def always_roll(n):
    """Return a strategy that always rolls N dice.

    A strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    >>> strategy = always_roll(5)
    >>> strategy(0, 0)
    5
    >>> strategy(99, 99)
    5
    """
    def strategy(score, opponent_score):
        return n
    return strategy


def check_strategy_roll(score, opponent_score, num_rolls):
    """Raises an error with a helpful message if NUM_ROLLS is an invalid
    strategy output. All strategy outputs must be integers from -1 to 10.

    >>> check_strategy_roll(10, 20, num_rolls=100)
    Traceback (most recent call last):
     ...
    AssertionError: strategy(10, 20) returned 100 (invalid number of rolls)

    >>> check_strategy_roll(20, 10, num_rolls=0.1)
    Traceback (most recent call last):
     ...
    AssertionError: strategy(20, 10) returned 0.1 (not an integer)

    >>> check_strategy_roll(0, 0, num_rolls=None)
    Traceback (most recent call last):
     ...
    AssertionError: strategy(0, 0) returned None (not an integer)
    """
    msg = 'strategy({}, {}) returned {}'.format(
        score, opponent_score, num_rolls)
    assert type(num_rolls) == int, msg + ' (not an integer)'
    assert -1 <= num_rolls <= 10, msg + ' (invalid number of rolls)'


def check_strategy(strategy, goal=GOAL_SCORE):
    """Checks the strategy with all valid inputs and verifies that the
    strategy returns a valid input. Use `check_strategy_roll` to raise
    an error with a helpful message if the strategy returns an invalid
    output.

    >>> def fail_15_20(score, opponent_score):
    ...     if score != 15 or opponent_score != 20:
    ...         return 5
    ...
    >>> check_strategy(fail_15_20)
    Traceback (most recent call last):
     ...
    AssertionError: strategy(15, 20) returned None (not an integer)
    >>> def fail_102_115(score, opponent_score):
    ...     if score == 102 and opponent_score == 115:
    ...         return 100
    ...     return 5
    ...
    >>> check_strategy(fail_102_115)
    >>> fail_102_115 == check_strategy(fail_102_115, 120)
    Traceback (most recent call last):
     ...
    AssertionError: strategy(102, 115) returned 100 (invalid number of rolls)
    """
    # BEGIN PROBLEM 6
    "*** REPLACE THIS LINE ***"
    for score in range(0,goal):
        for opponent_score in range(0,goal):
            check_strategy_roll(score,opponent_score,strategy(score,opponent_score))
    # END PROBLEM 6


# Experiments

def make_averaged(fn, num_samples=1000):
    """Return a function that returns the average_value of FN when called.

    To implement this function, you will have to use *args syntax, a new Python
    feature introduced in this project.  See the project description.

    >>> dice = make_test_dice(3, 1, 5, 6)
    >>> averaged_dice = make_averaged(dice, 1000)
    >>> averaged_dice()
    3.75
    """
    # BEGIN PROBLEM 7
    "*** REPLACE THIS LINE ***"
    def average(*args):
        total,ave =0,0
        for i in range(0,num_samples):
            total+=fn(*args)# fn(*args) in this example could be roll_dice()
        ave = total/num_samples
        return ave
    return average
    # END PROBLEM 7


def max_scoring_num_rolls(dice=six_sided, num_samples=1000):
    """Return the number of dice (1 to 10) that gives the highest average turn
    score by calling roll_dice with the provided DICE over NUM_SAMPLES times.
    Assume that the dice always return positive outcomes.

    >>> dice = make_test_dice(3)
    >>> max_scoring_num_rolls(dice)
    10
    """
    # BEGIN PROBLEM 8
    "*** REPLACE THIS LINE ***"
    max_num,prev_max_score= 0,0
    i =1
    while i <=10:
        current_score=make_averaged(roll_dice,num_samples)(i,dice)
        if current_score > prev_max_score:
            max_num,prev_max_score=i,current_score
        i+=1
    return max_num

   
    # END PROBLEM 8


def winner(strategy0, strategy1):
    """Return 0 if strategy0 wins against strategy1, and 1 otherwise."""
    score0, score1 = play(strategy0, strategy1)
    if score0 > score1:
        return 0
    else:
        return 1


def average_win_rate(strategy, baseline=always_roll(4)):
    """Return the average win rate of STRATEGY against BASELINE. Averages the
    winrate when starting the game as player 0 and as player 1.
    """
    win_rate_as_player_0 = 1 - make_averaged(winner)(strategy, baseline)
    win_rate_as_player_1 = make_averaged(winner)(baseline, strategy)

    return (win_rate_as_player_0 + win_rate_as_player_1) / 2


def run_experiments():
    """Run a series of strategy experiments and report results."""
    if True:  # Change to False when done finding max_scoring_num_rolls
        six_sided_max = max_scoring_num_rolls(six_sided)
        print('Max scoring num rolls for six-sided dice:', six_sided_max)
        rerolled_max = max_scoring_num_rolls(reroll(six_sided))
        print('Max scoring num rolls for re-rolled dice:', rerolled_max)

    if False:  # Change to True to test always_roll(8)
        print('always_roll(8) win rate:', average_win_rate(always_roll(8)))

    if False:  # Change to True to test bacon_strategy
        print('bacon_strategy win rate:', average_win_rate(bacon_strategy))

    if False:  # Change to True to test swap_strategy
        print('swap_strategy win rate:', average_win_rate(swap_strategy))

    "*** You may add additional experiments as you wish ***"


# Strategies

def bacon_strategy(score, opponent_score, margin=8, num_rolls=4):
    """This strategy rolls 0 dice if that gives at least MARGIN points,
    and rolls NUM_ROLLS otherwise.
    """
    # BEGIN PROBLEM 9
    "*** REPLACE THIS LINE ***"
    if take_turn(0,opponent_score)>=margin:
        return 0
    else:
        return num_rolls  # Replace this statement
    # END PROBLEM 9
check_strategy(bacon_strategy)


def swap_strategy(score, opponent_score, margin=8, num_rolls=4):
    """This strategy rolls 0 dice when it triggers a beneficial swap. It also
    rolls 0 dice if it gives at least MARGIN points. Otherwise, it rolls
    NUM_ROLLS.
    """
    # BEGIN PROBLEM 10
    "*** REPLACE THIS LINE ***"
    if take_turn(0,opponent_score)>=margin or 2*(score+take_turn(0,opponent_score))==opponent_score or 2*opponent_score==(score+take_turn(0,opponent_score)):
        return 0
    else:
        return num_rolls  # Replace this statement
    # END PROBLEM 10
check_strategy(swap_strategy)


def final_strategy(score, opponent_score):
    """Write a brief description of your final strategy.

    *** YOUR DESCRIPTION HERE ***
    The program starts out by rolling -1 dice and taking advantage of the
    pork chop roll. By rolling -1 and converting the dice to 4 sided, the
    strategy limits the maximum and average amount of points the opponent could
    potentially receive. The always_roll strategy also does not have the
    ability to swap the dice settings back.


    The next segment of code deals with edge cases and attempts to force
    favorable rolls. The reason for optimal roll is due to the following:

    (When Pigs Fly)
    Rolls       Maximum Possible Score          Average Dice Value Needed
    10          25 - 10 = 15                    1.5
    7           25 - 7 = 18                     2.57
    4           25 - 4 = 21                     5.25


    Four rolls seems to be optimal b/c while the game is mostly played using
    the four sided dice and therefore cannot achieve the average dice value, the
    risk of rolling a one is minimized while eliminating any possibility of the
    maximum score rule cutting off the raw roll value.
    
    rollZero is a temporary variable that represents the points you'd receive
    if you rolled a zero that turn. The first conditional checks if score is
    free bacon points away from winning, and then uses free bacon to ensure a
    win. The following conditionals test for swine swap and hog wild, and the
    conditionals are meant to either force favorable and avoid unfavorable
    swaps.

    The last set of conditionals deal with general strategy, in the case that
    none of the edge case opportunities are presented. If I am currently in the
    lead, if my score is greater than 75, I try to hinder the opponent by
    changing up the type of dice that is used if I cannot acheve a score
    higher than 2. Otherwise, I return a swap strategy that determines whether
    I'm rolling the defaultRoll value unless I can achieve a value of 7, which
    is a more conservative value than the same default swap strategy in the
    case I'm behind (margin is 11 instead of 7). Finally, the last return
    statement is only called if the scores are equal, in which I roll 4
    in an attempt to break the tie.

    """
    # BEGIN PROBLEM 11
    if score == 0:
        return -1

    defaultRoll = 4
    rollZero = take_turn(0, opponent_score)
    #Conditional that tries to close out game efficiently with hog wild
    if score + rollZero >= 100:
        return 0
    #following conditionals check if hog wild and swine swap strategies are
    #available and whether I'm on the favorable or unfavorable end of the deal
    if (score + rollZero) * 2 == opponent_score:
        return 0
    if opponent_score * 2 == score - 1:
        if rollZero > 1:
            return 0
    if (score + opponent_score)%7 == 0:
        return defaultRoll + 2
    if rollZero > defaultRoll + 2:
        return 0

    #If I am currently in the lead
    if score > opponent_score:
        if score > 75:
            #If the game is almost ending because scores are high
            return swap_strategy(score, opponent_score, 2, -1)
        else:
            #default strategy
            return swap_strategy(score, opponent_score, 7, defaultRoll)
    #If I am currently behind
    if score < opponent_score:
        #margin is greater than lead default strategy for more aggressive approach
        return swap_strategy(score, opponent_score, 11, defaultRoll)
    return defaultRoll
    # END PROBLEM 11
check_strategy(final_strategy)


##########################
# Command Line Interface #
##########################

# NOTE: Functions in this section do not need to be changed. They use features
# of Python not yet covered in the course.

@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions.

    This function uses Python syntax/techniques not yet covered in this course.
    """
    import argparse
    parser = argparse.ArgumentParser(description="Play Hog")
    parser.add_argument('--run_experiments', '-r', action='store_true',
                        help='Runs strategy experiments')

    args = parser.parse_args()

    if args.run_experiments:
        run_experiments()