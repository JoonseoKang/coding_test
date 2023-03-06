import math

def solution(fees, records):
    answer = []
    parking = {}
    fee = {}
    for i in records:
        time, number, inout = i.split()
        if number in parking.keys():
            t = 0
            intime_hour, intime_min = map(int, parking[number].split(':'))
            outtime_hour, outtime_min = map(int, time.split(':'))
            if outtime_min > intime_min:
                outtime_hour -= 1
                outtime_min += 60
            
            tmp = outtime_hour - intime_hour
            t = outtime_min - intime_min
            t += 60 * tmp
            
            if number in fee.keys():
                fee[number] = fee[number] + t
            else:
                fee[number] = t
            # print(number, time, parking[number], t)
            del parking[number]
            
        else:
            parking[number] = time
    

    for number, time in parking.items():
        outtime_hour, outtime_min = 23, 59
        if outtime_min > int(time.split(':')[1]):
            outtime_hour -= 1
            outtime_min += 60
                    
        tmp = outtime_hour - int(time.split(':')[0])
        t = outtime_min - int(time.split(':')[1])
        t += 60 * tmp
        
        if number in fee.keys():
            fee[number] = fee[number] + t
        else:
            fee[number] = t
    
    
    for i in sorted(fee.keys()):
        pay = fees[1]
        cum_time = fee[i]
        if cum_time > fees[0]:
            pay += math.ceil((cum_time - fees[0]) / fees[2]) * fees[3]
            
        answer.append(pay)

    return answer