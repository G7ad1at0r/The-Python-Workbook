savings_account = float(input("Account Ballance:\n>>> "))

year_one_ballance = savings_account * .04 + savings_account

year_two_ballance = year_one_ballance * .04 + year_one_ballance

year_three_ballance = year_two_ballance * .04 + year_two_ballance

print("After one full year your ballance will be :\n$ %.2f" % year_one_ballance)

print("After two full years your ballance will be :\n$ %.2f" % year_two_ballance)

print("After three full years your ballance will be :\n$ %.2f" % year_three_ballance)