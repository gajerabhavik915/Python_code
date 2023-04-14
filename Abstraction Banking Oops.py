from abc import ABC, abstractmethod


class Bank(ABC):

    def strings(self):
        print('This is calling from abstract class to provide string')

    @abstractmethod
    def total_AMt(self):
        pass

#
class Candidate_name(Bank):

    def __init__(self, name, start_amt):
        self.name = name
        self.start_amt = start_amt
        self.total_Amt = start_amt

    def total_AMt(self):
        # self.total_Amt = self.start_amt
        return self.total_Amt

    def deposite(self, deposite_amt):
        self.deposite_amt = deposite_amt
        if deposite_amt > 0:
            self.total_Amt = self.total_Amt + self.deposite_amt
            return self.total_Amt
        else:
            return 'Please provide proper digit'

    def withdraw(self, withdraw_amt):
        self.withdraw = withdraw_amt
        if withdraw_amt > self.total_Amt:
            return 'this is out of bound'

        else:
            self.withdraw = withdraw_amt
            self.total_Amt = self.total_Amt - self.withdraw
            return self.total_Amt




lists = [Candidate_name('Bhavik', 10), Candidate_name('Pritesh', 20), Candidate_name('Geetaben', 30), Candidate_name('Sureshbhai', 50)]
Bank_amt = 0
for candidate in lists:
    Bank_amt = Bank_amt + candidate.total_AMt()

print(Bank_amt)