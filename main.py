from arrangement import Arrangement
from mothersday import MothersDay
from valentinesday import ValentinesDay
from flower_collection.alstroemeria import Alstroemeria
from flower_collection.babysBreath import BabysBreath
from flower_collection.daisy import Daisy
from flower_collection.lily import Lily
from flower_collection.poppy import Poppy
from flower_collection.rose import Rose
red_rose = Rose(7, False)
yellow_daisy = Daisy(4, True)
lavender_lily = Lily(7, False)
purple_poppy = Poppy(4, True)
babys_breath = BabysBreath(4, True)
alstroemeria = Alstroemeria(7, False)

for_beth = ValentinesDay()
for_beth.enhance(red_rose)
for_beth.enhance(lavender_lily)
for_beth.enhance(alstroemeria)

for_mattk = MothersDay()
for_mattk.enhance(purple_poppy)









