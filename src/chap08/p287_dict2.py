# 항목 방문 하기

# 1
capitals ={"Korea":"Seoul","USA":"Washington","UK":"London"} 
for key in capitals :
        print( key, end=" ")
print("\n")

# 2
capitals ={"Korea":"Seoul","USA":"Washington","UK":"London"} 
for key in capitals :
        print( key,":", capitals[key])
print()

# 3        
capitals ={"Korea":"Seoul","USA":"Washington","UK":"London"} 
for key, value in capitals.items() :
        print( key,":", value)       
print()
        
# 4
capitals ={"Korea":"Seoul","USA":"Washington","UK":"London"} 
print(capitals.keys())
print(capitals.values())
print()

# 5
capitals ={"Korea":"Seoul","USA":"Washington","UK":"London"} 
for key in sorted(capitals.keys()):
    print(key, end=" ")
print()
