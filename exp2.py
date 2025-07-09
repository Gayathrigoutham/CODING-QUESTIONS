def get_finger_for_day(N):
    fingers = [
        "Thumb",
        "Index Finger",
        "Middle Finger",
        "Ring Finger",
        "Pinky Finger"
    ]
    return fingers[(N - 1) % 5]

# Read input from user
N = int(input("Enter the day number: "))
print(get_finger_for_day(N))
