'''
Assignment 1
Noah Pouliot
Student ID: 261282564
By submitting this file, I declare that I did the assignment on
my own according to the rules specified in the assignment PDF
'''
def get_user_details():
    average_sleep_time = float(input("Enter your average sleep time per night in hours: "))
    sleep_interruptions = int(input("Enter the number of times you wake up during the night: "))
    sleep_environment_quality = int(input("Rate your sleep environment quality on a scale from 1 (poor) to 10 (excellent): "))
    caffeine_consumption = int(input("Enter the average number of cups of coffee or caffeinated drinks you consume per day (0-10): "))
    exercise_duration = int(input("Enter the average number of minutes of exercise per day (0-200): "))
    stress_level = int(input("Rate your stress level on a scale from 1 (low) to 10 (high): "))
    return  average_sleep_time, sleep_interruptions, sleep_environment_quality, caffeine_consumption, exercise_duration, stress_level

def calculate_sleep_quality_score(avg_sleep, sleep_interruptions):
    sleep_score = (avg_sleep - sleep_interruptions)/8 * 100 #given formula
    return max(0, sleep_score) #if score is under 0, i.e its negative, then score is 0

def calculate_weighted_sleep_quality_index(sleep_quality_score, sleep_environment_quality, caffeine_consumption, exercise_duration, stress_level):
    wsqi = 0
    if sleep_quality_score > 0:
        wsqi= 0.5*sleep_quality_score +0.3*sleep_environment_quality +0.2*(10-caffeine_consumption) +0.1*(exercise_duration/15) -0.1*stress_level 
        wsqi =round(wsqi)
    return wsqi

def get_sleep_quality_group(wsqi):
    if wsqi > 70:
        return "Excellent"
    elif wsqi > 50:
        return "Good"
    elif wsqi > 30:
        return "Fair"
    elif wsqi >= 0:
        return "Poor"   

def main():
    average_sleep_time, sleep_interruptions, sleep_environment_quality, \
        caffeine_consumption, exercise_duration, stress_level = get_user_details()

    sleep_quality_score = calculate_sleep_quality_score(average_sleep_time, sleep_interruptions)
    wsqi = calculate_weighted_sleep_quality_index(sleep_quality_score,\
        sleep_environment_quality, caffeine_consumption, exercise_duration, stress_level)
    sleep_quality_group = get_sleep_quality_group(wsqi)

    print("Your Weighted Sleep Quality Index (WSQI) is"+str(wsqi)+"and is considered " +str(sleep_quality_group)+".")
    if sleep_quality_group == "Poor":
        print("Please consider the following recommendations:")
        if average_sleep_time < 7:
            print("Increase nightly sleep by", (8-average_sleep_time), "hour(s) to reach 8 hours.")
        if sleep_interruptions > 0:
            print("Reduce nighttime awakenings by optimizing your bedroom (make it darker, cooler, and quieter) and limiting fluids/alcohol before bed.")
        if caffeine_consumption > 2:
            print("Reduce caffeine by",(caffeine_consumption-2),"cup(s) to get below 3 cups/day, and avoid caffeine after mid-afternoon.")
        if exercise_duration < 15:
            print("Increase daily exercise by",(15-exercise_duration),"minute(s) (ideally earlier in the day) to reach or exceed 15 minutes.")


#main()









