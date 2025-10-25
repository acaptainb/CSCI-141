print(hash('Hi'))
states = {}
def put(htable, key, value):
    index = hash(key) % len(htable)
    htable[index] = (key, value)
# put(states, "PA", 1878)

ritirl = {"brick","fedora","tiger","brick"}
print(ritirl)

presidents = {}
presidents[ "munson"] = 2017
presidents[ " d e s t l e r " ] = 2007
presidents[ " simone " ] = 1992
presidents[ "r o s e "] = 1979

print(2007 in presidents)
print(presidents["munson"] )
print(list(presidents.keys()))
for president in presidents:
    if presidents[president] > 2000:
        print(president+":"+str(presidents[ president]))

