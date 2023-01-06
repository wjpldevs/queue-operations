from time import sleep
from helpers import makeBeep


class CircularQueue:

    Start = -1
    End = -1

    def __int__(self):
        self.Start = -1
        self.End = -1

    def add(self, data, queue) -> None:
        if self.is_full(queue):
            print("Circular queue is full.")
        else:
            if self.End == len(queue) - 1:
                self.End = 0
            else:
                self.End = self.End + 1

            queue[self.End] = data

            # Verify if exists at least one element inside the queue
            if self.Start == - 1:
                self.Start = 0


    def delete(self, queue) -> None:
        if self.is_empty(queue):
            print("Circular queue is empty.")
        else:
            
            # Only one item
            if self.Start == self.End:
                queue[self.Start] = "*"
                self.Start = -1
                self.End = -1
            else:
                if self.Start == len(queue) -1:
                    queue[self.Start] = "*"
                    self.Start = 0
                else:
                    queue[self.Start] = "*"
                    self.Start = self.Start + 1

    def show(self, queue) -> None:
        for index, value in enumerate(queue):
            if queue[index] == "":
                print("*\t ", end="")
                makeBeep()
                sleep(0.5)
            else:
                print(f"{value}\t ", end="")
                makeBeep()
                sleep(0.5)

    def is_full(self, queue) -> bool:
        if (self.End == len(queue) - 1 and self.Start == 0) or (self.End + 1 == self.Start):
            return True
        else:
            return False

    def is_empty(self, queue) -> bool:
        if self.Start == -1:
            return True
        else:
            return False

    def get_start(self) -> int:
        return self.Start

    def get_end(self) -> int:
        return self.End
