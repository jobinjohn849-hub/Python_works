# 1.College Event Registration

# age = int(input("Enter your age: "))
# student = input("Are you a student? (yes/no): ")

# if age >= 18 and age <= 25 and student == "yes":
#     print("Eligible for registration")
# else:
#     print("Not eligible for registration")

# 2. Online Shopping Discount

# amount = float(input("Enter order amount: "))
# membership = input("Are you a premium member? (yes/no): ")

# if amount >= 3000 or membership == "yes":
#     print("Customer qualifies for discount")
# else:
#     print("Customer does not qualify for discount")

# 3. Airport check-in 

# ticket = input("Is your ticket confirmed? (yes/no): ")
# passport = input("Is your passport valid? (yes/no): ")
# hours = float(input("Hours remaining until departure: "))

# if ticket == "yes" and passport == "yes" and hours > 2:
#     print("Online check-in is available")
# else:
#     print("Online check-in is not available")

# 4.Movie Ticket Booking

# age = int(input("enter your age:"))
# if age < 12 or age >= 60:
#     print("Qualified for Special Tickets")
# else:
#     print("Not Qualified for Special Tickets")

# 5. Bank Loan Pre - Eligiblity

# income = float(input("Enter monthly income: "))
# credit_score = int(input("Enter credit score: "))
# default = input("Do you have an existing loan default? (yes/no): ")

# if income >= 40000 and credit_score >= 700 and default == "no":
#     print("Eligible for loan")
# else:
#     print("Not eligible for loan")

# 6.Food Delivery Free Shipping

# amount = float(input("Enter order amount: "))
# premium = input("Premium membership? (yes/no): ")
# disabled = input("Is delivery temporarily disabled? (yes/no): ")

# if (amount >= 500 or premium == "yes") and disabled == "no":
#     print("Free delivery available")
# else:
#     print("Free delivery not available")

# 7.Employee Work from Home

# months =int(input("Enter months worked in company:" ))
# remote = input("Does the project allow remote work?(yes/no):")

# if months >=6 and remote == "yes":
#     print("Eligible to Work from Home")
# else:
#     print("Not Eligible to Work from Home")

#8.Hotel Room Booking

# available = input("Is the room available? (yes/no): ")
# payment = input("Is the payment method valid? (yes/no): ")
# stopped = input("Has the hotel stopped reservations? (yes/no): ")

# if available == "yes" and payment == "yes" and stopped == "no":
#     print("Booking can proceed")
# else:
#     print("Booking cannot proceed")

# 9. Online Access Exam

# logged = input("Is the student logged in? (yes/no): ")
# registered = input("Is exam registration confirmed? (yes/no): ")
# active = input("Is the exam active? (yes/no): ")
# blocked = input("Is the account blocked? (yes/no): ")

# if logged == "yes" and registered == "yes" and active == "yes" and blocked == "no":
#     print("Student can access the exam")
# else:
#     print("Student cannot access the exam")

# # 10. Gym Membership plan 

# years = float(input("Enter membership duration in years:"))
# active =input("Is Membership Active?(yes/no):")
# yearly = input("Has the member purchased a yearly plan?(yes/no):")

# if (years >=1 and active == "yes") or yearly == "yes":
#     print("Eligible for premium upgrade")
# else:
#     print("Not eligible for premium upgrade")

# 11. Ride Booking Application

# service = input("Is pickup within the service area? (yes/no): ")
# driver = input("Is a driver available? (yes/no): ")
# scheduled = input("Are scheduled rides enabled? (yes/no): ")

# if (service == "yes" and driver == "yes") or scheduled == "yes":
#     print("Booking is available")
# else:
#     print("Booking is not available")

# 12. E-Commerce Product Return

# days = int(input("Days since purchase: "))
# unused = input("Is the product unused? (yes/no): ")
# eligible = input("Is the product eligible for return? (yes/no): ")

# if days <= 7 and unused == "yes" and eligible == "yes" and days >= 0:
#     print("Return request accepted")
# else:
#     print("Return request rejected")

# 13. Library Book Borrowing

# overdue = input("Do you have overdue books? (yes/no): ")
# active = input("Is library membership active? (yes/no): ")
# available = input("Is the requested book available? (yes/no): ")

# if overdue == "no" and active == "yes" and available == "yes":
#     print("Student can borrow the book")
# else:
#     print("Student cannot borrow the book")

# 13. Library Book Borrowing
overdue = input("Do you have overdue books? (yes/no): ")
active = input("Is library membership active? (yes/no): ")
available = input("Is the requested book available? (yes/no): ")
if overdue == "no" and active == "yes" and available == "yes":   
    print("Student can borrow the book")
else:   
    print("Student cannot borrow the book")



# 14. Job Application Screening
experience = float(input("Enter Python experience in years: "))
django = input("Do you know Django? (yes/no): ")
fastapi = input("Do you know FastAPI? (yes/no): ")
if experience >= 3 or (experience >= 1 and (django == "yes" or fastapi == "yes")):   
     print("Candidate qualifies for the next stage")
else:    
    print("Candidate does not qualify for the next stage")



# 15. Mobile Data Usage Alert
usage = float(input("Enter data usage percentage: "))
remaining = float(input("Enter remaining data in GB: "))
unlimited = input("Is the data plan unlimited? (yes/no): ")
if (usage >= 90 or remaining < 1) and unlimited == "no":    
    print("Warning: Data usage is high")
else:    
    print("No warning")



# 16. Parking Lot Entry
pass_valid = input("Do you have a valid parking pass? (yes/no): ")
visitor = input("Are you paying for visitor parking? (yes/no): ")
full = input("Is the parking lot full? (yes/no): ")
if (pass_valid == "yes" or visitor == "yes") and full == "no":
    print("Vehicle can enter")
else:    
    print("Vehicle cannot enter")



# 17. Scholarship Eligibility
score = float(input("Enter academic score: "))
attendance = float(input("Enter attendance percentage: "))
if (score >= 85 and attendance >= 75) or score >= 95:    
    print("Student is eligible for scholarship")
else:    
    print("Student is not eligible for scholarship")



# 18. Food Ordering – Restaurant Availability
opened = input("Is the restaurant open? (yes/no): ")
delivery = input("Does it deliver to your location? (yes/no): ")
orders = input("Is it accepting online orders? (yes/no): ")
if opened == "yes" and delivery == "yes" and orders == "yes":    
    print("Order can be placed")
else:    
    print("Order cannot be placed")



# 19. Smart Home Security
motion = input("Is motion detected? (yes/no): ")
door = input("Is the main door open? (yes/no): ")
armed = input("Is the security system armed? (yes/no): ")
if armed == "yes" and (motion == "yes" or door == "yes"):    
    print("Security alert triggered")
else:    
    print("Security alert not triggered")



# 20. Travel Insurance Eligibility
age = int(input("Enter age: "))
days = int(input("Enter trip duration in days: "))
covered = input("Is the country covered by insurance? (yes/no): ")
excluded = input("Is the destination excluded from coverage? (yes/no): ")
if age >= 18 and age <= 65 and days > 0 and days <= 30 and covered == "yes" and excluded == "no":    
    print("Eligible for travel insurance")
else:    
    print("Not eligible for travel insurance")