
import matplotlib.pyplot as plt
import pandas as pd

data = [
    ("Nov 1 at 12:36 PM", 100.0),
    ("Nov 1 at 12:33 PM", 100.0),
    ("Nov 1 at 12:22 PM", 92.5),
    ("Nov 1 at 12:19 PM", 85.0),
    ("Nov 1 at 12:18 PM", 80.0),
    ("Nov 1 at 12:17 PM", 80.0),
    ("Nov 1 at 12:08 PM", 80.0),
    ("Nov 1 at 12:04 PM", 40.0),
    ("Nov 1 at 11:58 AM", 40.0),
    ("Nov 1 at 11:47 AM", 40.0),
    ("Oct 30 at 1:40 PM", 20.0),
    ("Oct 30 at 1:31 PM", 20.0),
    ("Oct 30 at 1:29 PM", 0.0),
    ("Oct 30 at 1:14 PM", 0.0),
    ("Oct 28 at 11:51 PM", 0.0),
    ("Oct 28 at 9:54 PM", 0.0),
    ("Oct 28 at 9:52 PM", 0.0),
    ("Oct 28 at 9:48 PM", 0.0),
    ("Oct 28 at 9:47 PM", 0.0),
    ("Oct 28 at 9:44 PM", 0.0),
    ("Oct 28 at 9:38 PM", 0.0),
    ("Oct 28 at 9:37 PM", 0.0),
    ("Oct 28 at 9:36 PM", 0.0),
    ("Oct 28 at 9:35 PM", 0.0),
    ("Oct 28 at 9:30 PM", 0.0),
    ("Oct 28 at 9:29 PM", 0.0),
    ("Oct 28 at 9:27 PM", 0.0),
    ("Oct 28 at 9:25 PM", 0.0),
    ("Oct 28 at 9:18 PM", 0.0),
    ("Oct 28 at 9:16 PM", 0.0),
    ("Oct 28 at 9:09 PM", 0.0),
    ("Oct 28 at 8:47 PM", 0.0),
    ("Oct 28 at 8:23 PM", 0.0),
    ("Oct 28 at 8:13 PM", 0.0),
    ("Oct 28 at 8:12 PM", 0.0),
    ("Oct 28 at 8:08 PM", 0.0),
    ("Oct 28 at 8:06 PM", 0.0),
    ("Oct 28 at 8:02 PM", 0.0),
]

# Saving to a file
with open('gradescope_data.txt', 'w') as file:
    for entry in data:
        file.write(f"{entry[0]}\t{entry[1]}\n")

# Or using a list directly
timestamps = [entry[0] for entry in data]
grades = [entry[1] for entry in data]

# Then, proceed with the plotting code using timestamps and grades lists.
timestamps = pd.to_datetime(timestamps, format='%b %d at %I:%M %p')

# Plotting the data
plt.figure(figsize=(10, 6))
plt.plot(timestamps, grades, marker='o', linestyle='-', color='b')
plt.title('Gradescope Submissions Over Time')
plt.xlabel('Timestamp')
plt.ylabel('Grade')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()