def find_missing(array1,array2):
	x = set(array1)
	y = set(array2)
   

    if len(x) == len(y):

        return 0
    elif len(x) == 0 and len(y) == 0:
    	return 0

    elif len(x) != len(y):

        x = set(array1)

        y = set(array2)

        z = x^y

return list(z)[0]