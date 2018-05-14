
place=['new york', 'brazil', 'hawaii', 'swiss', 'israle']

print ("\nprint original list")
print (place)

print ("\nprint sorted list")
print (sorted(place))

print ("\nprint original list")
print (place)

print ("\nprint reverse sorted list")
print (sorted(place, reverse=True))

print ("\nprint list after method reverse")
place.reverse()
print (place)

print ("\nprint list after method reverse")
place.reverse()
print (place)

print ("\nprint list after method sort")
place.sort()
print (place)

print ("\nprint list after method sort with reverse")
place.sort(reverse=True)
print (place)

print ("\nTotal places")
print (len(place))

place.append(1)
print (place)
