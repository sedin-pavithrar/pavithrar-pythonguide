# Delivery Time Estimator: 
# Take distance (km), weather (clear/rain/storm), and time of day (peak/normal) as input. 
# Calculate estimated delivery time and show a status message like Zomato does. 
# Distance: 4.5 km 
# Weather (clear/rain/storm): rain 
# Time (peak/normal): peak 
# Estimated delivery: 42 mins 
# Status: "Running slightly late due to rain" 

print("=====Delivery Estimator=====")

distance = float(input(" Enter distance in km:"))
weather = input(" Input your weather\n (Clear/Rain/Storm) :").lower()
time_of_day = input(" Enter time (peak/ normal) :").lower()

print(f" Distance :{distance} km ")
print(f" Weather(Clear / Rain / Storm):{weather}")
print(f" Time ( peak / normal):{time_of_day}")

#base delivery time (6 min oer km )
delivery_time = distance * 6 

weather_delay = {
    "clear": 0,
    "rain": 10,
    "storm": 20
}

traffic_delay = {
    "normal": 0,
    "peak": 10
}

delivery_time += weather_delay.get(weather, 0)
delivery_time += traffic_delay.get(time_of_day, 0)

print(f"\n Estimated Delivery : {delivery_time} mins" )


status_messages = {
    "storm":"Delivery delayed due to storm conditions",
    "rain":"Running slightly late due to rain",
    "peak":"Heavy traffic, delivery may take longer"
}

status = (
    status_messages.get(weather)
    or status_messages.get(time_of_day)
    or "Your order is on the way"
)

print(f" Status: {status}")











