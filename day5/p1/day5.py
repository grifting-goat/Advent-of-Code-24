

fileName = "input.txt"

rules = []
updates = []
valid = []

flag = 1

def isValid(update,rules):
    #check everthing over and over again
    for i,j in rules:
        if i in update and j in update:
            if update.index(i) > update.index(j):
                return False
    return True

#main
with open(fileName, "r") as file:
    for line in file:
        line = line.strip()  
        if "|" in line:
            #i am terrible at python syntax, i have to phanoodle this stuff off the internets #genuinely who makes this stuff
            x, y = map(int, line.split("|"))
            rules.append((x, y))
        elif line:
            updates.append(list(map(int, line.split(","))))

ans = 0

#check if the updates are cool
for up in updates:
    if isValid(up, rules):
        #add middle value if its cool
        ans += up[int(len(up)/2)]

print(ans)