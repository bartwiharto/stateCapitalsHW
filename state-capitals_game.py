import random
from random import randint

state_capitals = [
{'state': 'Alabama', 'capital': 'Montgomery'}, 
{'state': 'Alaska', 'capital': 'Juneau'},
{'state': 'Arizona', 'capital': 'Phoenix'},
{'state': 'Arkansas', 'capital': 'Little Rock'},
{'state': 'California', 'capital': 'Sacramento'},
{'state': 'Colorado', 'capital': 'Denver'},
{'state': 'Connecticut', 'capital': 'Hartford'},
{'state': 'Delaware', 'capital': 'Dover'},
{'state': 'Florida', 'capital': 'Tallahassee'},
{'state': 'Georgia', 'capital': 'Atlanta'},
{'state': 'Hawaii', 'capital': 'Honolulu'},
{'state': 'Idaho', 'capital': 'Boise'},
{'state': 'Illinois', 'capital': 'Springfield'},
{'state': 'Indiana', 'capital': 'Indianapolis'},
{'state': 'Iowa', 'capital': 'Des Moines'},
{'state': 'Kansas', 'capital': 'Topeka'},
{'state': 'Kentucky', 'capital': 'Frankfort'},
{'state': 'Louisiana', 'capital': 'Baton Rouge'},
{'state': 'Maine', 'capital': 'Augusta'},
{'state': 'Maryland', 'capital': 'Annapolis'},
{'state': 'Massachusetts', 'capital': 'Boston'},
{'state': 'Michigan', 'capital': 'Lansing'},
{'state': 'Minnesota', 'capital': 'Saint Paul'},
{'state': 'Mississippi', 'capital': 'Jackson'},
{'state': 'Missouri', 'capital': 'Jefferson City'},
{'state': 'Montana', 'capital': 'Helena'},
{'state': 'Nebraska', 'capital': 'Lincoln'},
{'state': 'Nevada', 'capital': 'Carson City'},
{'state': 'New Hampshire', 'capital': 'Concord'},
{'state': 'New Jersey', 'capital': 'Trenton'},
{'state': 'New Mexico', 'capital': 'Santa Fe'},
{'state': 'New York', 'capital': 'Albany'},
{'state': 'North Carolina', 'capital': 'Raleigh'},
{'state': 'North Dakota', 'capital': 'Bismarck'},
{'state': 'Ohio', 'capital': 'Columbus'},
{'state': 'Oklahoma', 'capital': 'Oklahoma City'},
{'state': 'Oregon', 'capital': 'Salem'},
{'state': 'Pennsylvania', 'capital': 'Harrisburg'},
{'state': 'Rhode Island', 'capital': 'Providence'},
{'state': 'South Carolina', 'capital': 'Columbia'},
{'state': 'South Dakota', 'capital': 'Pierre'},
{'state': 'Texas', 'capital': 'Austin'},
{'state': 'Utah', 'capital': 'Salt Lake City'},
{'state': 'Vermont', 'capital': 'Montpelier'},
{'state': 'Virginia', 'capital': 'Richmond'},
{'state': 'Washington', 'capital': 'Olympia'},
{'state': 'West Virginia', 'capital': 'Charleston'},
{'state': 'Wisconsin', 'capital': 'Madison'},
{'state': 'Wyoming', 'capital': 'Cheyenne'},
{'state': 'American Samoa', 'capital': 'Pago Pago'},
{'state': 'Guam', 'capital': 'Hagatna'},
{'state': 'Northern Mariana Islands', 'capital': 'Saipan'},
{'state': 'Puerto Rico', 'capital': 'San Juan'},
{'state': 'US Virgin Islands', 'capital': 'Charlotte Amalie'}
]
state_random = state_capitals[randint(0, len(state_capitals) - 1)]


state_capital_answer =  input('What is the capital of ' + state_random['state'] + '? (Please put your answer in quotes')
if state_capital_answer == state_random['capital']:
	print('You got it, Buddy!')
else:
	print('You are NOT smarter than a 5th Grader.')

# Not sure why the code breaks when we don't answer in quotes, so I have to give a specific instruction to put their answers inside quote signs.
# This code is unfortunately case sensitive, but that can be avoided by changing user's answer using .upper(), but I ran out of time to try this method.




