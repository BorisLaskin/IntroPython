def quicksortMy(listMy):
    if len(listMy)<=1:
        return listMy
    else:
        pivot=listMy[0]
        less=[i for i in listMy[1:] if i<=pivot]
        greater=[i for i in listMy[1:] if i>pivot]
        return quicksortMy(less)+[pivot]+quicksortMy(greater)
        
def vstavkaMy(arrayMy):
    
    for i in range(1,len(arrayMy)):
        element_to_insert=arrayMy[i]
        j=i-1
        while j>=0 and arrayMy[j]>element_to_insert:
            arrayMy[j+1]=arrayMy[j]
            j-=1
        arrayMy[j+1]=element_to_insert
    return arrayMy

def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1