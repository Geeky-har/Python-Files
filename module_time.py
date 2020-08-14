import time

curr_time = time.localtime()  # it helps to get the current local time
curr_clock = time.strftime("%H:%M:%S", curr_time)  # it determines the foramt of the time

print(curr_clock)

# init = time.time()
#
# i = 1
# while i <= 1000:
#     print(i)
#     i += 1
# print(time.time() - init)

lt = time.asctime(time.localtime(time.time()))      # returns date, time and day

print(lt)
