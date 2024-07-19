"""doc"""

class Chicken:
    """doc"""
    def __init__(self):
        """doc"""
        self.chicken_count = 0
        self.main1()
        self.main2()
        print(self.chicken_count)

    def chicken_pass(self):
        """doc"""
        chicken_weigh = float(input())
        if 50 <= chicken_weigh <= 70:
            self.chicken_count += 1
    def main1(self):
        """doc"""
        self.chicken_pass()
        self.chicken_pass()
        self.chicken_pass()
        self.chicken_pass()
        self.chicken_pass()
        self.chicken_pass()
        self.chicken_pass()
        self.chicken_pass()
        self.chicken_pass()
        self.chicken_pass()
        self.chicken_pass()
        self.chicken_pass()

    def main2(self):
        """doc"""
        self.chicken_pass()
        self.chicken_pass()
        self.chicken_pass()
        self.chicken_pass()
        self.chicken_pass()
        self.chicken_pass()
        self.chicken_pass()
        self.chicken_pass()
        self.chicken_pass()
        self.chicken_pass()
        self.chicken_pass()
        self.chicken_pass()
Chicken()
