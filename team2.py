team_name = 'Phang'
strategy_name = 'Copy'
strategy_description = 'Collude first round. Take their play from last round and use that move'
    
def move(my_history, their_history, my_score, their_score):
    if len(my_history)==0: # It's the first round; collude.
        return 'c'
    elif their_history[-1]=='b':
        return 'b'
    elif their_history[-1]=='c':
        return 'c' #If their last move was collude, then collude
    else:
        return 'b' # otherwise betray.

