class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        r = []
        for a in range(1,n+1):
            if a % 3 == 0 and a % 5 == 0: r.append( "FizzBuzz")
            elif a % 3 == 0: r.append("Fizz")
            elif a % 5 == 0: r.append("Buzz")
            else: r.append(str(a))
        return r