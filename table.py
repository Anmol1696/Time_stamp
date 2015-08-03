# Table for the time stamping
#        "Time_Clause", Rank, Value, Trigger, Oppration, Index, Importance 
#        m/h/DD/MM/YYYY
word_list = [
	["hour", 1, 1, 'N', 'N', 1, 2],
	["hours", 1, 'N', 'N', 'N', 1, 5],
	["minute", 2, 1, 'N', 'N', 0, 2],
	["minutes", 2, 'N', 'N', 'N', 0, 5],
	["day", 3, 1, 'N', 'N', 2, 2],
	["days", 3, 'N', 'N', 'N', 2, 5],
	["month", 4, 1, 'N', 'N', 3, 5],
	["months", 4, 'N', 'N', 3, 5],
	["year", 5, 1, 'N', 'N', 4, 2],
	["years", 5, 'N', 'N', 'N', 4, 5],
	
	['january', 7, 1, 'N', 'set', 4, 2], 
	['february', 7, 2, 'N', 'set', 4, 2],
	['march', 7, 3, 'N', 'set', 4, 2],
	['april', 7, 4, 'N', 'set', 4, 2],
	['may', 7, 5, 'N', 'set', 4, 2],
	['june', 7, 6, 'N', 'set', 4, 2],
	['july', 7, 7, 'N', 'set', 4, 2],
	['august', 7, 8, 'N', 'set', 4, 2],
	['september', 7, 9, 'N', 'set', 4, 2],
	['october', 7, 10, 'N', 'set', 4, 2],
	['november', 7, 11, 'N', 'set', 4, 2],
	['december', 7, 12, 'N', 'set', 4, 2],
	
	["in", 8, 'N', 'S/P less', 'add/set', 'N', 4],
	["within", 8, 'N', 'P less', 'add/set', 'N', 4],
	["on", 8, 'N', 'S', 'add/sub/set', 'N', 4],
	["before", 8, 'N', 'P less', 'add/set', 'N', 4],
	["after", 8, 'N', 'P more', 'add/set', 'N', 4],
	["last", 8, 'N', 'P less', 'sub', 'N', 4],
	["next", 8, 'N', 'P less', 'add', 'N', 4],
	["past", 8, 'N', 'P less/P more', 'add/sub', 'N', 4]
]

