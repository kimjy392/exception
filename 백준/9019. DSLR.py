from collections import deque

T = int(input())

for _ in range(T):
    A, B = input().split()
    stack = deque([(A, '')])
    visit = [0] * 10000
    visit[int(A)] = True
    while stack:
        Astring, res = stack.popleft()
        Anum = int(Astring)
        if Anum == int(B):
            print(res)
            break
        for command in 'DSLR':
            tmp = None
            if command == 'D':
                tmp = (Anum * 2) % 10000
                if 0 <= tmp < 10000 and not visit[tmp]:
                    visit[tmp] = True
                    stack.append((str(tmp), res+command))
            elif command == 'S':
                if Anum == 0:
                    tmp = 9999
                else:
                    tmp = Anum - 1
                if 0 <= tmp < 10000 and not visit[tmp]:
                    visit[tmp] = True
                    stack.append((str(tmp), res+command))
            elif command == 'L':
                tstring = Astring[1:] + Astring[0]
                if 0 < int(tstring) < 10000 and not visit[int(tstring)]:
                    visit[int(tstring)] = True
                    stack.append((tstring, res+command))
            else:
                tstring = Astring[-1] + Astring[:-1]
                if 0 < int(tstring) < 10000 and not visit[int(tstring)]:
                    visit[int(tstring)] = True
                    stack.append((tstring, res+command))

