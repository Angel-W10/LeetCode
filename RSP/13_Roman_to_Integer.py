def romanToInt(self, s: str) -> int:
        '''
        create a dictinoary of the symbol and its value

        go though the list and check current and next value (while loop):
            if next > curr:
                val = next - curr
                i+=2
            else
                val = cur
                i+=1

        O(n)
        '''

        # values = collections.defaultdict(set)
        values = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
            }

        out = 0
        n = len(s)
        i = 0
        while i != n:
            cur = s[i]
            if i+1 < n and values[s[i+1]] > values[cur]:
                out += (values[s[i+1]] - values[cur])
                i+=2 
            else:
                out+=values[cur]
                i+=1
            # print(s[i], out)
            

        return out

