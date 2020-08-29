def solution(p):
    def recur(string):
        if string == '':
            return ''
        u, v = '', ''
        for i in range(len(string)):
            word = string[i]
            u += word
            if u and u.count('(') == u.count(')'):
                break
        v = string[i + 1:]
        tmp = []
        flag = 0
        for ch in u:
            if ch == '(':
                tmp.append(ch)
            elif ch == ')':
                if tmp:
                    tmp.pop()
                else:
                    flag = 1
                    break
        if not flag:
            u += recur(v)
            return u
        else:
            utmp = '('
            utmp += recur(v)
            utmp += ')'
            u = u[1:len(u) - 1]
            for ch in u:
                if ch == '(':
                    utmp += ')'
                else:
                    utmp += '('
            return utmp
    answer = recur(p)
    return answer

solution('()))((()')