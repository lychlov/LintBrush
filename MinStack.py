class MinStack:

    def __init__(self):
        # do intialization if necessary
        self.items=[]
        self.mins=[]

    """
    @param: number: An integer
    @return: nothing
    """

    def push(self, number):
        # write your code here
        self.items.append(number)
        if len(self.mins)==0:
            self.mins.append(number)
        else:
            if number<self.mins[-1]:
                self.mins.append(number)
            else:
                self.mins.append(self.mins[-1])


    """
    @return: An integer
    """

    def pop(self):
        # write your code here
        self.mins.pop()
        return self.items.pop()

    """
    @return: An integer
    """

    def min(self):
        # write your code here
        return self.mins[-1]
