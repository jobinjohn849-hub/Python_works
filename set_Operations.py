# 1. Students Enrolled in Courses A training institute offers two courses: 
# • Python course students
#  • Data Analytics course students
#  python_students = {"Arun", "Megha", "Rahul", "Sneha"} 
# analytics_students = {"Sneha", "Rahul", "Aman", "Diya"} 
# Tasks 1. Find students enrolled in both courses.
#  2. Find students enrolled only in Python. 
# 3. Find students enrolled only in Data Analytics. 
# 4. Find all unique students.
#  5. Find students enrolled in exactly one course. 

# ---ans---
# python_students = {"Arun", "Megha", "Rahul", "Sneha"}
# analytics_students = {"Sneha", "Rahul", "Aman", "Diya"}

# # 1. Students in both courses
# print("Both courses:", python_students & analytics_students)

# # 2. Only Python
# print("Only Python:", python_students - analytics_students)

# # 3. Only Data Analytics
# print("Only Data Analytics:", analytics_students - python_students)

# # 4. All unique students
# print("All students:", python_students | analytics_students)

# # 5. Exactly one course
# print("Exactly one course:", python_students ^ analytics_students)

# ---2q--
# 2. Mobile Brands Purchased by Customers Two customers purchased different mobile brands. 
# customer1 = {"Samsung", "Apple", "OnePlus", "Realme"}
# customer2 = {"Apple", "Vivo", "Oppo", "Samsung"} 
# Tasks 
# 1. Find common brands purchased by both customers.
# 2. Find all brands purchased. 
# 3. Find brands purchased only by customer1.
# 4. Find brands purchased by only one customer

# ---2ans--
# customer1 = {"Samsung", "Apple", "OnePlus", "Realme"}
# customer2 = {"Apple", "Vivo", "Oppo", "Samsung"}

# # 1. Common brands
# print("Common brands:", customer1 & customer2)

# # 2. All brands
# print("All brands:", customer1 | customer2)

# # 3. Only customer1
# print("Only customer1:", customer1 - customer2)

# # 4. Only one customer
# print("Only one customer:", customer1 ^ customer2)

# ---3q---
# 3. Employees Using Software Tools
# Employees in two departments use different software tools.
# design_team = {"Figma", "Photoshop", "Canva", "Illustrator"} 
# marketing_team = {"Canva", "Excel", "Photoshop", "PowerBI"} 
# Tasks
# 1. Find tools used by both teams.
# 2. Find tools exclusive to the design team.
# 3. Find all software tools used in the company. 
# 4. Find tools used by only one team.
# ---3ans--

# design_team = {"Figma", "Photoshop", "Canva", "Illustrator"}
# marketing_team = {"Canva", "Excel", "Photoshop", "PowerBI"}

# # 1. Common tools
# print("Common tools:", design_team & marketing_team)

# # 2. Exclusive design tools
# print("Design team only:", design_team - marketing_team)

# # 3. All tools
# print("All tools:", design_team | marketing_team)

# # 4. Tools used by only one team
# print("Only one team:", design_team ^ marketing_team)


# ---4q--
# 4. Cricket and Football Fans
# A survey collected sports preferences of students.
# cricket_fans = {"Ajay", "Kiran", "Rohit", "Nisha"} 
# football_fans = {"Nisha", "Rahul", "Ajay", "David"} 
# Tasks 
# 1. Find students who like both sports. 
# 2. Find students who like only cricket. 
# 3. Find students who like only football.
# 4. Find all sports fans. 

# ---4ans---
# cricket_fans = {"Ajay", "Kiran", "Rohit", "Nisha"}
# football_fans = {"Nisha", "Rahul", "Ajay", "David"}

# # 1. Both sports
# print("Both sports:", cricket_fans & football_fans)

# # 2. Only cricket
# print("Only cricket:", cricket_fans - football_fans)

# # 3. Only football
# print("Only football:", football_fans - cricket_fans)

# # 4. All fans
# print("All fans:", cricket_fans | football_fans)


# ----5q---
# 5. Online Shopping Categories
# A customer purchased products from two categories.
# electronics = {"Laptop", "Headphones", "Mouse", "Keyboard"} 
# accessories = {"Keyboard", "Mouse Pad", "Laptop Stand", "Headphones"} 
# Tasks 
# 1. Find common purchased products.
# 2. Find products only in electronics.
# 3. Find all purchased items.
# 4. Find products available in only one category. 

# ---5ans---
# electronics = {"Laptop", "Headphones", "Mouse", "Keyboard"}
# accessories = {"Keyboard", "Mouse Pad", "Laptop Stand", "Headphones"}

# # 1. Common products
# print("Common products:", electronics & accessories)

# # 2. Only electronics
# print("Only electronics:", electronics - accessories)

# # 3. All products
# print("All products:", electronics | accessories)

# # 4. Products in only one category
# print("Only one category:", electronics ^ accessories)

# ---6q---
# 6. Languages Known by Employees

# ---6ans---
# employee1 = {"Python", "Java", "SQL", "C"}
# employee2 = {"Python", "JavaScript", "SQL", "Go"}

# # 1. Common languages
# print("Common languages:", employee1 & employee2)

# # 2. Only employee1
# print("Only employee1:", employee1 - employee2)

# # 3. All unique languages
# print("All languages:", employee1 | employee2)

# # 4. Languages known by only one employee
# print("Only one employee:", employee1 ^ employee2)


# ----7q---

# 7. OTT Platform Subscriptions
# ----7ans---
# friend1 = {"Netflix", "Prime", "Hotstar", "SonyLiv"}
# friend2 = {"Netflix", "Zee5", "Prime", "JioCinema"}

# # 1. Common subscriptions
# print("Common subscriptions:", friend1 & friend2)

# # 2. Unique to friend1
# print("Only friend1:", friend1 - friend2)

# # 3. All platforms
# print("All platforms:", friend1 | friend2)

# # 4. Platforms subscribed by only one friend
# print("Only one friend:", friend1 ^ friend2)

# ----8q---
# 8. Available and Sold Products
# ----8ans---
# available_products = {"Laptop", "Mouse", "Keyboard", "Monitor"}
# sold_products = {"Mouse", "Monitor"}

# # 1. Remaining available products
# print("Remaining products:", available_products - sold_products)

# # 2. Sold products
# print("Sold products:", sold_products)

# # 3. Add Printer
# available_products.add("Printer")
# print("After adding Printer:", available_products)

# # 4. Remove Keyboard
# available_products.remove("Keyboard")
# print("After removing Keyboard:", available_products)

# ----9q---
# 9. College Event Participation

# ----9ans---
# music_event = {"Anu", "David", "Riya", "Sam"}
# dance_event = {"Riya", "Sam", "Karthik", "John"}

# # 1. Both events
# print("Both events:", music_event & dance_event)

# # 2. Only music
# print("Only music:", music_event - dance_event)

# # 3. Only dance
# print("Only dance:", dance_event - music_event)

# # 4. All participants
# print("All participants:", music_event | dance_event)

# ----10q---
# 10. Website Visitors
# ----10ans---
# campaign_A = {"user101", "user102", "user103", "user104"}
# campaign_B = {"user103", "user104", "user105", "user106"}

# # 1. Common visitors
# print("Common visitors:", campaign_A & campaign_B)

# # 2. Unique to campaign A
# print("Only campaign A:", campaign_A - campaign_B)

# # 3. Total unique visitors
# print("Total visitors:", campaign_A | campaign_B)

# # 4. Visitors from only one campaign
# print("Only one campaign:", campaign_A ^ campaign_B)

# ---11q---
# Mini Challenge – Food Delivery App
# ----11ans---
# restaurant1 = {"Burger", "Pizza", "Fries", "Pasta"}
# restaurant2 = {"Pizza", "Sandwich", "Pasta", "Momos"}

# # 1. Common food items
# print("Common items:", restaurant1 & restaurant2)

# # 2. Exclusive items of restaurant1
# print("Restaurant 1 only:", restaurant1 - restaurant2)

# # 3. Exclusive items of restaurant2
# print("Restaurant 2 only:", restaurant2 - restaurant1)

# # 4. All available food items
# print("All food items:", restaurant1 | restaurant2)

# # 5. Items available in only one restaurant
# print("Only one restaurant:", restaurant1 ^ restaurant2)