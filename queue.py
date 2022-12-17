from time import sleep
from helpers import makeBeep


class Queue:

    Start = -1
    End = -1

    def __int__(self):
        self.Start = -1
        self.End = -1

    def add(self, data, queue) -> None:
        if self.is_full(queue):
            print("Queue is full.")
        else:
            self.End = self.End + 1
            queue[self.End] = data
            if self.End == 0:
                self.Start = 0

    def delete(self, queue) -> None:
        if self.is_empty(queue):
            print("Queue is empty.")
        else:
            if self.Start == self.End:
                queue[self.End] = "*"
                self.Start = -1
                self.End = -1
            else:
                queue[self.Start] = "*"  # This is a way to delete the data
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
        if self.End == len(queue) - 1:
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
