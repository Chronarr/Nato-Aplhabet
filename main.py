nato_alph = dict(A='Alfa', B='Bravo', C='Charlie', D='Delta', E='Echo', F='Foxtrot', G='Golf', H='Hotel', I='India',
                 J='Juliet', K='Kilo', L='Lima', M='Mike', N='November', O='Oscar', P='Papa', Q='Quebec', R='Romeo',
                 S='Sierra', T='Tango', U='Uniform', V='Victor', W='Whiskey', X='X-ray', Y='Yankee', Z='Zulu')
answer = [nato_alph[x.upper()] for x in input("Input a word to convert to NATO alphabet - ")]
print(answer)
