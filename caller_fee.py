def fee_charge(S):
    fee = 0
    calls = S.split()
    d = {}

    for call in calls:

        duration, number = call.split(",")
        hours, minutes, seconds = duration.split(":")
        total_seconds = int(hours)*60*60 + int(minutes)*60 + int(seconds)
        running_fee = 0
        if total_seconds < 5*60:
            running_fee += 3*total_seconds
        else:
            running_fee += 150*(int(hours)*60 + int(minutes))
            if int(seconds) > 0:
                running_fee += 150

        if number not in d:
            d[number] = (total_seconds, running_fee)
        else:
            ts, r = d[number]
            d[number] = (ts+total_seconds, r+running_fee)
        fee += running_fee

    max_caller_fee = 0
    max_caller_duration = 0
    max_caller_number = None
    for key, value in d.iteritems():
        ts, r = value
        if max_caller_duration < ts:
            max_caller_duration = ts
            max_caller_fee = r
            max_caller_number = key 
        if max_caller_duration == ts:
            # import pdb; pdb.set_trace()
            if int("".join(max_caller_number.split("-"))) > int("".join(key.split("-"))):
                max_caller_fee = r
                max_caller_duration = ts
                max_caller_number = key

    return fee - max_caller_fee

print fee_charge('00:02:30,201-742-2104\n00:05:00,201-742-2103\n00:02:30,201-742-2104\n')