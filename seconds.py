seconds = int(input('seconds: '))
hours = seconds // 3600
remaining_sec = seconds % 3600
mins = remaining_sec // 60
secs = seconds % 60
print(f"{hours} : {mins} : {secs}")