'''Sorts input into a neat new list

   prompts for input twice turns both into list,
   combines, and sorts them to return a new neat list'''
print(__doc__)


f = list(input('Enter some numbers no commas no spaces: '))
d = list(input('Enter some more numbers no commas no spaces: '))
c = f+d
# prompted for input twice both were turned into a list
# then those lists were combined

list.sort(c)
# we sorted our new combined list

print(c)
# this displays our output for us









