import time

start_time = time.time()

time.sleep(1)

end_time = time.time()
result = end_time - start_time

print("Время выполнения операции =", result, "секунд")

local_time = time.localtime()
print(local_time)

year = local_time.tm_year
month = local_time.tm_mon
day = local_time.tm_mday
hour = local_time.tm_hour
minute = local_time.tm_min
second = local_time.tm_sec

print(f"Локальная дата и время: {day}-{month}-{hour}-{minute}-{second}-{year}")

utc_time = time.gmtime()
print("Текущее время в формате UTC:", utc_time)