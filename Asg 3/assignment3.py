'''
Assignment 3
Noah Pouliot
Student ID: 261282564
By submitting this file, I declare that I did the assignment on
my own according to the rules specified in the assignment PDF
'''
def smartwatch_analyzer(filename: str):
    week_data = read_raw_data(filename)
    best_hours=get_best_hour(week_data)
    morning_evening_winners=compare_morning_evening(week_data)
    hourly_avgs=hourly_averages(week_data)
    centered_sequence=extract_centered_subsequence(week_data)  
    
    daily_analysis_list = []
    for day in range(7):
        daily_dict = {
            'day': day,
            'best_hour': best_hours[day],
            'morning_evening': morning_evening_winners[day],
            'hourly_avgs': hourly_avgs[day]
        }
        daily_analysis_list.append(daily_dict)
    
    analysis_dict = { 
        'daily_analysis': daily_analysis_list,
        'peak_activity': (centered_sequence[0], centered_sequence[1], centered_sequence[2][7], \
            centered_sequence[2])
                        #(day, minute, biggest step count, subsequence)
        }
    return analysis_dict

def read_raw_data(filename: str):
    with open(filename, 'r') as file:
        data = file.readlines()

    officially_parsed_data = []  
    for line in data:
        line=line.strip().split(',')
        
        for i in range(len(line)):
            line[i] = int(line[i])
        officially_parsed_data.append(line)
        
    return officially_parsed_data

def get_best_hour(week_data: list):
    best_hours = []
    for index, day_data in enumerate(week_data):
        total_steps = 0
        start_minute = 0
        for minute in range(1440-59): #all minutes with following hour that do not span over midnight
            step_in_following_hour = sum(day_data[minute:minute+60])
            if step_in_following_hour > total_steps:
                total_steps = step_in_following_hour
                start_minute = minute
        if index<6: #every day before the last day of the week
            for minute in range (1440-59, 1440): #all minutes with following hour that span over midnight
                step_in_following_hour = sum(day_data[minute:])+\
                    sum(week_data[index+1][:60-(1440-minute)])
                if step_in_following_hour > total_steps:
                    total_steps = step_in_following_hour
                    start_minute = minute
        best_hours.append((start_minute, total_steps))
    
    return best_hours

def compare_morning_evening(week_data: list):
    morning_evening_winners = []
    for day_data in week_data:
        morning_total = sum(day_data[360:720]) 
        evening_total = sum(day_data[1020:1320]) 
        
        winner =''
        if morning_total > evening_total:
            winner= "morning"
        elif evening_total > morning_total:
            winner= "evening"
        else:
            winner= "equal"
        
        morning_evening_winners.append((morning_total, evening_total, winner))
    
    return morning_evening_winners

def extract_centered_subsequence(week_data: int):
    week_max=0
    day_index= -1
    peak_minute= -1
    for i in range(len(week_data)):
        day_max = max(week_data[i])
        if day_max > week_max:
            week_max = day_max
            day_index = i
            peak_minute = week_data[i].index(day_max)
    
    subsequence=[]
    if peak_minute < 7:
        for j in range(7-peak_minute):
            subsequence.append(0)
        subsequence+=week_data[day_index][0:peak_minute+8]
    elif peak_minute > 1432:
        subsequence.extend(week_data[day_index][peak_minute-7:])
        for j in range(7-(1439-peak_minute)):
            subsequence.append(0)
    else:
        subsequence.extend(week_data[day_index][peak_minute-7:peak_minute+8])
    return (day_index, peak_minute, subsequence)


def hourly_averages(week_data: list):
    all_hourly_averages = []
    for day_data in week_data:
        hourly_averages=[]
        for hour in range (24):
            hourly_averages.append(sum(day_data[hour*60:(hour+1)*60])/60)
        all_hourly_averages.append(hourly_averages)
    return all_hourly_averages
        
def write_analysis_csv(analysis_dict: dict):
    with open("analysis_report.csv", 'w') as file:
        file.write("daily analysis\n")
        #headers
        file.write("day,best_hour_start,best_hour_steps,morning_total,\
            evening_total,winner,")
        file.write(",".join([f"hour_{i}_avg" for i in range(24)]))
        file.write("\n")
        #values
        for day_dict in analysis_dict['daily_analysis']:
            file.write(f"{day_dict['day']},{day_dict['best_hour'][0]},\
                {day_dict['best_hour'][1]},")
            file.write(f"{day_dict['morning_evening'][0]},{day_dict['morning_evening'][1]},\
                {day_dict['morning_evening'][2]},")
            file.write(",".join([str(round(avg,1)) for avg in day_dict['hourly_avgs']]))
            file.write("\n")
        
        file.write("\npeak activity\n")
        #heaeders
        file.write("day,minute,steps,")
        file.write(",".join([f"subseq_{i}" for i in range(15)]))
        file.write("\n")
        #values
        file.write(f"{analysis_dict['peak_activity'][0]},{analysis_dict['peak_activity'][1]},\
            {analysis_dict['peak_activity'][2]},")
        file.write(",".join([str(step) for step in analysis_dict['peak_activity'][3]]))


def filter_high_activity_data(week_data: list, threshold: int):
    filtered_data = []
    for day_data in week_data:
        filtered_day = [steps if steps >= threshold else 0 for steps in day_data]
        filtered_data.append(filtered_day)
    return filtered_data

    
# analysis_dict = smartwatch_analyzer("step_data.csv")
# write_analysis_csv(analysis_dict)