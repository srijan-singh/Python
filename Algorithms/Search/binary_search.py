def binary_search(objects, object, high=0, low=0, mid=0):
    # If user doesn't provide number of objects (high)
    if high == low:
        high = len(objects)
        return binary_search(objects, object, high)
    else:
        mid = (high+low)//2
        # Whether the object falls within the range
        if object >= objects[low] and object <= objects[high-1]:
            # When the object is found
            if object == objects[mid]:
                return True
            # When object is bigger than the middle element
            elif object > objects[mid]:
                return binary_search(objects, object, high, mid, (high+mid)//2)
            # When object is smaller than the middle element
            elif object < objects[mid]:
                return binary_search(objects, object, mid, low, (mid+low)//2)
        # Object isn't in the range
        else:
            return False

print(binary_search(["Anita",'Bianca','Kristen','Ritika','Rehana',"Selena"],'Ritika'))

