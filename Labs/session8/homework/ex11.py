def is_inside(point, rec):
    if (rec[0]< point[0] <rec[0] + rec[2]) and (rec[1] < point[1] < rec[1]+rec[3]):
            return True 
    else:
        return False


print(is_inside([100, 120], [140, 60, 100, 200]))
print(is_inside([200, 120], [140, 60, 100, 200]))