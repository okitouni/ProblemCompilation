# this implementation sucks
def median(arr1, arr2):
    # these two arrays are sorted
    if len(arr1) < len(arr2):
        arr1, arr2 = arr2, arr1
    n = len(arr1)
    m = len(arr2)    
    mid = (n + m + 1) // 2

    def search_idx(idx):
        check = checker(idx)
        if check == 0:
            return idx
        elif check < 0:
            idx = (idx + mid + 1) // 2
            search_idx(idx)
        elif check > 0:
            if idx == 0:
                # a cannot appear in the first half of the merged array
                return -1 
            idx //= 2
            search_idx(idx)
    
    def checker(idx):
        # check that idx is the last item in a
        # that appears in the first half of the merged array
        if (arr1[idx] <= arr2[mid-idx]):
            if  (arr2[mid-idx-1]<=arr1[idx+1]):
                return 0 # guess is just right
            else:
                return -1 # guess is too small, increase it
        return 1 # guess is too large, decrease it
    
    arr1_idx = search_idx(mid)
    if arr1_idx == -1:
        pass # do something here 
    low_mid = max(arr1[arr1_idx], arr2[mid - arr1_idx-1])
    if n + m % 2 == 1:
        return low_mid
    else:
        high_mid = min(max(arr1[arr1_idx+1], arr2[mid - arr1_idx]))
        return (low_mid + high_mid)/2
    



arr1 = [2,3,5]
# arr1 = [0,1,1]
arr2 = [2,4,6]

mid = 3

idx_arr1 = 1



    


    