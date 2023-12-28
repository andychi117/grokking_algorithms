def countdown(times):
    print(times)
    if times < 0:
        return
    else:
        countdown(times - 1)

countdown(10)
