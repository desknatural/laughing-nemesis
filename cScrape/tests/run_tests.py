from . import tests

Bools = []

bool, string = tests.getPage_Test1()
Bools.append(bool)
print string

bool, string = tests.getPage_Test2()
Bools.append(bool)
print string

bool, string = tests.pageParse_Test1()
Bools.append(bool)
print string

sum = 0
for bool in Bools:
	if bool:
		sum += 1
		
print str(sum) + " tests have passed."
