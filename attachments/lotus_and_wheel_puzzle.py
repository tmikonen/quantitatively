def create_deck(deck_size, p_lotus):
    deck = np.random.uniform(size=deck_size)
    deck = 1 + np.floor(deck-p_lotus)
    return deck

def draw(hand, deck, n):
    hand = np.append(hand,deck[range(n)])
    deck = np.delete(deck,range(n))
    return (hand, deck)

def play_lotuses(hand, n_loti):
    ind = np.where(hand == 0)[0]
    n_loti += len(ind)
    hand = np.delete(hand,ind)
    return (hand, n_loti)

def can_play_wheel(hand, n_loti):
    ind = np.where(hand == 1)[0]
    if len(ind) > 0 and n_loti > 0:
        return True
    else:
        return False
    
def play_wheel(hand, deck, n_loti):
    n_loti -= 1
    hand = np.empty(0)
    (hand,deck) = draw(hand, deck, 7)
    return (hand, deck, n_loti)

def opponent_has_lost(deck, deck_size):
    if deck_size - len(deck) > 40:
        return True
    else:
        return False

def play_games(n_iter, p_lotus, deck_size, is_on_the_draw):
    winning_turn = np.zeros(n_iter)
    for i in range(n_iter):
        n_lotuses_in_play = 0
        n_turns = 0
        
        game_ended = False

        deck = create_deck(deck_size,p_lotus)
        hand = np.empty(0)
        #starting hand
        (hand, deck) = draw(hand,deck,7)
        # mulligan logic would go here if it was allowed

        #start taking turns
        while not game_ended:
            n_turns += 1
            #if is_on_the_draw or n_turns > 1:
            (hand, deck) = draw(hand,deck,1)
            if opponent_has_lost(deck, deck_size):
                winning_turn[i] = n_turns
                game_ended = True
            elif (len(deck)<7):
                winning_turn[i] = -n_turns
                game_ended = True

            (hand, n_lotuses_in_play) = play_lotuses(hand, n_lotuses_in_play)
            while can_play_wheel(hand, n_lotuses_in_play) and not game_ended:
                (hand, deck, n_lotuses_in_play) = play_wheel(hand, deck, n_lotuses_in_play)
                (hand, n_lotuses_in_play) = play_lotuses(hand, n_lotuses_in_play)
                
                if opponent_has_lost(deck, deck_size):
                    winning_turn[i] = n_turns
                    game_ended = True
                elif (len(deck)<7):
                    winning_turn[i] = -n_turns
                    game_ended = True
    return winning_turn

