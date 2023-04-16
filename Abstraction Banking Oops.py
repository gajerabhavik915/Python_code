# from abc import ABC, abstractmethod
#
#
# class Bank(ABC):
#
#     def strings(self):
#         print('This is calling from abstract class to provide string')
#
#     @abstractmethod
#     def total_AMt(self):
#         pass
#
#     @abstractmethod
#     def deposite(self, deposite_amt):
#         pass
#
#     @abstractmethod
#     def withdraw(self, withdraw_amt):
#         pass
#
#
#
# #
# class Candidate_name(Bank):
#
#     def __init__(self, name, start_amt):
#         self.name = name
#         self.start_amt = start_amt
#         self.total_Amt = start_amt
#         self.trans_list = []
#
#     def total_AMt(self):
#         # self.total_Amt = self.start_amt
#         return self.total_Amt
#
#     def deposite(self, deposite_amt):
#         self.deposite_amt = deposite_amt
#         if deposite_amt > 0:
#             self.total_Amt = self.total_Amt + self.deposite_amt
#             self.trans_list.append(('deposited', self.deposite_amt))
#             return self.total_Amt
#         else:
#             return 'Please provide proper digit'
#
#     def withdraw(self, withdraw_amt):
#         # self.withdraw = withdraw_amt
#         if withdraw_amt < self.total_Amt:
#             self.withdraw_amt = withdraw_amt
#             self.total_Amt = self.total_Amt - self.withdraw_amt
#             self.trans_list.append(('withdrew', self.withdraw_amt))
#             return self.total_Amt
#
#         else:
#             return 'this is out of bound'
#
#
#
#
#
# lists = [Candidate_name('Bhavik', 1000), Candidate_name('Pritesh', 2000), Candidate_name('Geetaben', 3000), Candidate_name('Sureshbhai', 5000)]
# Bank_amt = 0
#
# lists[0].deposite(100)
# lists[0].withdraw(200)
# lists[1].withdraw(200)
# lists[2].withdraw(400)
#
#
# for candidate in lists:
#     Bank_amt = Bank_amt + candidate.total_AMt()
#     if len(candidate.trans_list) != 0:
#         print(f'Candidate {candidate.name} has done transaction {candidate.trans_list} and total balance left is {candidate.total_AMt()}')
#     else:
#         print(f'Candidate {candidate.name} has well maintained account and total balance left is {candidate.total_AMt()}')
#
# print(Bank_amt)
#
from abc import ABC, abstractmethod


class Bank(ABC):

    def __init__(self, name, start_amt):
        self.name = name
        self.start_amt = start_amt
        self.total_Amt = start_amt
        self.trans_list = []

    def strings(self):
        print('This is calling from abstract class to provide string')

    @abstractmethod
    def total_AMt(self):
        pass

    @abstractmethod
    def deposite(self, deposite_amt):
        pass

    @abstractmethod
    def withdraw(self, withdraw_amt):
        pass



#
class Candidate_name(Bank):


    def total_AMt(self):
        # self.total_Amt = self.start_amt
        return self.total_Amt

    def deposite(self, deposite_amt):
        self.deposite_amt = deposite_amt
        if deposite_amt > 0:
            self.total_Amt = self.total_Amt + self.deposite_amt
            self.trans_list.append(('deposited', self.deposite_amt))
            return self.total_Amt
        else:
            return 'Please provide proper digit'

    def withdraw(self, withdraw_amt):
        # self.withdraw = withdraw_amt
        if withdraw_amt < self.total_Amt:
            self.withdraw_amt = withdraw_amt
            self.total_Amt = self.total_Amt - self.withdraw_amt
            self.trans_list.append(('withdrew', self.withdraw_amt))
            return self.total_Amt

        else:
            return 'this is out of bound'




lists = [Candidate_name('Bhavik', 1000), Candidate_name('Pritesh', 2000), Candidate_name('Geetaben', 3000), Candidate_name('Sureshbhai', 5000)]
Bank_amt = 0

lists[0].deposite(100)
lists[0].withdraw(200)
lists[1].withdraw(200)
lists[2].withdraw(400)


for candidate in lists:
    Bank_amt = Bank_amt + candidate.total_AMt()
    if len(candidate.trans_list) != 0:
        print(f'Candidate {candidate.name} has done transaction {candidate.trans_list} and total balance left is {candidate.total_AMt()}')
    else:
        print(f'Candidate {candidate.name} has well maintained account and total balance left is {candidate.total_AMt()}')

print(Bank_amt)

