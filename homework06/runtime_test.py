# Проверка времени выполнения кода в наносекундах
# (В данном скрипте проверка f"" и  "".format())
import time

ITER_COUNT = 8_000_000

start = 0
finish = 0

# ------- переменные для теста --------
string = "TEST string 123 !@#"
text1 = ""
text2 = ""
# -------------------------------------

start = time.thread_time()
# ------------- 1 вариант -------------
for i in range(ITER_COUNT):
    text1 = "{} my concat".format(string)
# -------------------------------------
finish = time.thread_time()
print("1 вариант: " + str(finish - start))

start = time.thread_time()
# ------------- 2 вариант -------------
for i in range(ITER_COUNT):
    text2 = f"{string} my concat"
# -------------------------------------
finish = time.thread_time()
print("2 вариант: " + str(finish - start))

