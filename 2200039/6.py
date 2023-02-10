def flatten(dump_times,box_list):
    if dump_times > 0:
        find_max_height = max(box_list)
        max_index = box_list.index(find_max_height)
        find_min_height = min(box_list)
        min_index = box_list.index(find_min_height)
        if find_max_height - find_min_height == 0 or find_max_height - find_min_height == 1:
            return box_list
        else:
            box_list[max_index] = find_max_height-1
            box_list[min_index] = find_min_height+1
            return flatten(dump_times-1,box_list)
    else: return box_list

for _ in range(10):
    dump_times = int(input()); result = []
    box = list(map(int,input().split()))
    flatten(dump_times,box)
    print("#{} {}".format(_+1,max(box)-min(box)))