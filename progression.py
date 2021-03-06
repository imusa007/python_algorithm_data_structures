from nbformat import current_nbformat


class Progression:
    def __init__(self, start=0):
        self._current=start

    def _advance(self):

        self._current+=1
    
    def __next__(self):

        if self._current is None:
            raise StopIteration()
        answer=self._current
        self._advance()
        return answer
    
    def __iter__(self):

        return self
    
    def print_progression(self,n):
        print(' '.join(str(next(self)) for j in range(n)))


    
class ArithmaticProgression(Progression):
    def __init__(self,increment=1,start=0):
        super().__init__(start)
        self._increment=increment
    
    def _advance(self):

        self._current+=self._increment

    

if __name__=='__main__':
    s1=Progression()
    s1.print_progression(10)
    a1=ArithmaticProgression(increment=2)
    a1.print_progression(10)