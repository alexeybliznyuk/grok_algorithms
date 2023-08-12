class Searcher:
    def binarysearch(list, answer):
        low = 0
        high = len(list) - 1
        
        mid = (low + high) / 2
        while high >= low:
            mid = (low + high) /2
            mid = round(mid)
            guess = list[mid]
            if guess > answer:
                high = mid - 1
            elif guess < answer: 
                low = mid + 1
            elif guess == answer: 
                return guess
        

mylist = [1,3,5,8,9]
key = 0
srch = Searcher
print(srch.binarysearch(mylist, key))
            
