import time

def start_focus_timer(minutes):
    seconds = minutes * 60
    start_time = time.time()
    end_time = start_time + seconds

    while time.time() < end_time:
        remaining_time = int(end_time - time.time())
        minutes_remaining = remaining_time // 60
        seconds_remaining = remaining_time % 60
        time_remaining = "{:02d}:{:02d}".format(minutes_remaining, seconds_remaining)
        print("Time remaining: {}".format(time_remaining), end="\r")
        time.sleep(1)

    print("Focus time is over!")

# 设置专注时钟的时间（以分钟为单位）
focus_minutes = 25

start_focus_timer(focus_minutes)
