# leeds +246 26% or -113 for the tie 49%
# sevilla -114 48%
# atalanta -315 70%
# Sheffield +181 .35
# Sassoulo *115 .43
probs = [.35,.48,.49,.70,.43]
payout = 1044
stake = 50
wins = 5
import numpy as np
all_5 = np.prod(probs)
any_4 = sum([all_5 / probs[i] for i in range(len(probs))])
print(all_5)
print(any_4)
win = all_5 + any_4
loss = 1-win
print(win * 600 - loss * 50)