for i_1 in range(10):
    i_dump = int(input())
    ls_ground = list(map(int, input().split()))
    for i_2 in range(i_dump):
        if max(ls_ground) - min(ls_ground) == 1:
            break
        else:
            ls_ground[ls_ground.index(max(ls_ground))] -= 1
            ls_ground[ls_ground.index(min(ls_ground))] += 1
    print(f'#{i_1 + 1} {max(ls_ground)- min(ls_ground)}')