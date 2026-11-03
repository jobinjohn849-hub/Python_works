# 1.student grade calculator
# mark = int(input("Enter student mark: "))

# if mark >= 90 and mark <= 100:
#     print("Grade: A+")
# elif mark >= 80:
#     print("Grade: A")
# elif mark >= 70:
#     print("Grade: B")
# elif mark >= 60:
#     print("Grade: C")
# elif mark >= 50:
#     print("Grade: D")
# elif mark >= 0:
#     print("Fail")
# else:
#     print("Invalid mark")


# 2. atm withdrawal system
# balance = int(input("Enter account balance: "))
# amount = int(input("Enter withdrawal amount: "))

# if amount > balance:
#     print("Insufficient Balance")
# elif amount % 100 != 0:
#     print("Enter an amount in multiples of 100")
# else:
#     print("Withdrawal Successful")
#     print("Remaining Balance:", balance - amount)

# 3.online shoping delivery 

# amount = int(input("Enter order amount: "))

# if amount >= 5000:
#     delivery = 0
# elif amount >= 2000:
#     delivery = 50
# else:
#     delivery = 100

# print("Delivery Charge:", delivery)
# print("Final Amount:", amount + delivery)

# 4.employee performance rating
# score = int(input("Enter performance score: "))

# if score >= 90:
#     print("Excellent")
# elif score >= 75:
#     print("Very Good")
# elif score >= 60:
#     print("Good")
# elif score >= 40:
#     print("Needs Improvement")
# else:
#     print("Poor")

# 5.electricity bill calculation

# units = int(input("Enter units consumed: "))

# if units <= 100:
#     bill = units * 2
# elif units <= 200:
#     bill = (100 * 2) + (units - 100) * 3
# elif units <= 400:
#     bill = (100 * 2) + (100 * 3) + (units - 200) * 5
# else:
#     bill = (100 * 2) + (100 * 3) + (200 * 5) + (units - 400) * 7

# print("Electricity Bill:", bill)


# 6.movie ticket pricing
# age = int(input("Enter your age: "))

# if age < 5:
#     price = 0
# elif age <= 12:
#     price = 100
# elif age <= 59:
#     price = 200
# else:
#     price = 120

# print("Ticket Price:", price)

# 7 . traffic fine system

# speed = int(input("Enter vehicle speed: "))

# if speed <= 60:
#     print("No Fine")
# elif speed <= 80:
#     print("Fine: Rs.500")
# elif speed <= 100:
#     print("Fine: Rs.1000")
# else:
#     print("Fine: Rs.2000")
#     print("License Review")

# 8. resturant billing systeam
# bill = int(input("Enter total bill: "))

# if bill >= 5000:
#     discount = bill * 20 / 100
# elif bill >= 3000:
#     discount = bill * 15 / 100
# elif bill >= 1000:
    # discount = bill * 10 / 100
# else:
    # discount = 0

# final_bill = bill - discount

# print("Discount:", discount)
# print("Final Bill:", final_bill)

# 9. college admission decision
# score = int(input("Enter entrance exam score: "))

# if score >= 90:
#     print("Direct Admission")
# elif score >= 75:
#     print("Admission + Interview")
# elif score >= 60:
#     print("Waitlisted")
# else:
#     print("Not Eligible")

# 10.bank loan risk category
# score = int(input("Enter credit score: "))
# default = input("Existing loan default (yes/no): ")

# if default == "yes":
#     print("Loan Approval Requires Manual Review")
# else:
#     if score >= 750:
#         print("Low Risk")
#     elif score >= 650:
#         print("Medium Risk")
#     elif score >= 550:
#         print("High Risk")
#     else:
#         print("Very High Risk")

# 11.hotel room pricing

# room = input("Enter room type: ")
# nights = int(input("Enter number of nights: "))

# if room == "Standard":
#     price = 2000
# elif room == "Deluxe":
#     price = 3500
# elif room == "Suite":
#     price = 5000
# else:
#     price = 0
#     print("Invalid Room Type")

# total = price * nights

# if nights > 5:
#     total = total - (total * 10 / 100)

# print("Final Bill:", total)

# 12.employe bonus calculator

# salary = int(input("Enter annual salary: "))
# performance = int(input("Enter performance score: "))

# if performance >= 90:
#     bonus = salary * 20 / 100
# elif performance >= 75:
#     bonus = salary * 15 / 100
# elif performance >= 60:
#     bonus = salary * 10 / 100
# else:
#     bonus = 0

# print("Annual Bonus:", bonus)

# 13.mobile data plan
# data = int(input("Enter monthly data usage in GB: "))

# if data < 5:
#     print("Basic Plan - Rs.199")
# elif data <= 20:
#     print("Standard Plan - Rs.399")
# elif data <= 50:
#     print("Premium Plan - Rs.699")
# else:
#     print("Unlimited Plan - Rs.999")

# 14.parking fee calculator
# hours = int(input("Enter parking hours: "))
# vehicle = input("Is it an electric vehicle? (yes/no): ")

# if hours <= 2:
#     fee = 30
# elif hours <= 5:
#     fee = 50
# elif hours <= 10:
#     fee = 100
# else:
#     fee = 150

# if vehicle == "yes":
#     fee = fee - (fee * 20 / 100)

# print("Final Parking Fee:", fee)

# 15.online exam result
# theory = int(input("Enter theory mark: "))
# practical = int(input("Enter practical mark: "))

# if theory >= 40 and practical >= 40:
#     average = (theory + practical) / 2

#     if average >= 75:
#         print("Distinction")
#     elif average >= 60:
#         print("First Class")
#     elif average >= 50:
#         print("Second Class")
#     else:
#         print("Pass")
# else:
#     print("Fail")

# 16.fligthing bagging fee

# weight = int(input("Enter baggage weight: "))
# travel = input("Enter class (Economy/Business): ")

# if travel == "Business":
#     limit = 25
# else:
#     limit = 15

# if weight <= limit:
#     charge = 0
# elif weight <= 20:
#     charge = 500
# elif weight <= 30:
#     charge = 1000
# else:
#     charge = 2000

# print("Baggage Charge:", charge)

# 17.e commerce return eligibility
# days = int(input("Enter days since purchase: "))
# unused = input("Is the product unused? (yes/no): ")
# returnable = input("Is the product returnable? (yes/no): ")

# if days > 7:
#     print("Return Rejected: Purchase is older than 7 days")
# elif unused != "yes":
#     print("Return Rejected: Product is used")
# elif returnable != "yes":
#     print("Return Rejected: Product is not returnable")
# else:
#     print("Return Approved")

# 18.salary tax calculator

# salary = int(input("Enter annual salary: "))

# if salary <= 300000:
#     tax = 0
# elif salary <= 600000:
#     tax = salary * 5 / 100
# elif salary <= 1000000:
#     tax = salary * 10 / 100
# else:
#     tax = salary * 20 / 100

# final_salary = salary - tax

# print("Tax Amount:", tax)
# print("Salary After Tax:", final_salary)

# 19.ride fare calculator
# distance = int(input("Enter distance in km: "))
# peak = input("Is it peak hour? (yes/no): ")

# if distance <= 5:
#     fare = 100
# elif distance <= 15:
#     fare = 100 + (distance - 5) * 15
# elif distance <= 30:
#     fare = 100 + (10 * 15) + (distance - 15) * 12
# else:
#     fare = 100 + (10 * 15) + (15 * 12) + (distance - 30) * 10

# if peak == "yes":
#     fare = fare + (fare * 20 / 100)

# print("Final Ride Fare:", fare)

# 20.employee leave approval system
# available = int(input("Enter available leave days: "))
# requested = int(input("Enter requested leave days: "))

# if requested > available:
#     print("Leave Rejected")
# elif requested <= 3:
#     print("Leave Automatically Approved")
# elif requested <= 7:
#     print("Manager Approval Required")
# else:
#     print("HR Approval Required")