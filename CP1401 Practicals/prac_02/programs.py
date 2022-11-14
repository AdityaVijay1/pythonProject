# 1.Discount Price
DISCOUNT_RATE = 0.2
Original_Price = float(input("Enter the original price"))
discount_price = Original_Price * DISCOUNT_RATE
New_Price = Original_Price - discount_price
print("The new price is", New_Price)

# 2.Kilometres to Miles #Conversion Rate is good to use constant
MILE = 0.621371
distance_in_kilometre = float(input("Enter the distance to be converted"))
Kilometre_to_Mile = distance_in_kilometre * MILE
print("The distance in miles is", Kilometre_to_Mile)

# 3.Holiday Cost
'''#Algorithm 
get daily_food_cost,daily_activities_cost,number_of_days
Total_Cost=(daily_food_cost+daily_activities_cost+75)*number_of_days
display Total_Cost'''

HOTEL_COST = 75
Daily_Food_Cost = float(input("Daily Food Cost:"))
Daily_Activities_Cost = float(input("Daily Activities Cost:"))
Number_Of_Days = int(input("Number of days:"))
Total_Cost = (Daily_Food_Cost + Daily_Activities_Cost + HOTEL_COST) * Number_Of_Days
print("The trip will cost", Total_Cost)

# 4. Deep Sleep Calculation (Percentage)
''' #Algorithm 
get total_sleep,deep_sleep
deep_sleep_in_minutes=deep_sleep//60
deep_sleep_in_seconds=deep_sleep%60
totalsleep_in_minutes=total_sleep//60
totalsleep_in_seconds=total_sleep%60
Percentage_of_deep_sleep=(deep_sleep/total_sleep)*100
display deep_sleep_in_minute, deep_sleep_in_second
display totalsleep_in_minutes,totalsleep_in_seconds
display Percentage_of_deep_sleep
'''
PERCENTAGE_RATE = 100
MINUTES_IN_SECONDS = 60
Total_Sleep = int(input("Total sleep in seconds: "))
Deep_Sleep = int(input("Deep sleep in seconds : "))
Deep_Sleep_in_minutes = Deep_Sleep // MINUTES_IN_SECONDS
Deep_Sleep_in_seconds = Deep_Sleep % MINUTES_IN_SECONDS
Total_Sleep_in_minutes = Total_Sleep // MINUTES_IN_SECONDS
Total_Sleep_in_seconds = Total_Sleep % MINUTES_IN_SECONDS
Percentage_of_Deep_Sleep = (Deep_Sleep / Total_Sleep) * PERCENTAGE_RATE
print(" ")
print("Deep sleep :", Deep_Sleep_in_minutes, "m", Deep_Sleep_in_seconds, "s")
print("Total sleep :", Total_Sleep_in_minutes, "m", Total_Sleep_in_seconds, "s")
print(" ")
print("Percentage : ", Percentage_of_Deep_Sleep, "%")
