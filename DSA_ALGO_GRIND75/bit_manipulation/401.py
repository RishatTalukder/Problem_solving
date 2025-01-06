class Solution:
    """
    A class used to represent the solution for reading a binary watch.

    Methods
    -------
    readBinaryWatch(turnedOn: int) -> List[str]:
        Given a number of LEDs that are turned on, returns all possible times the binary watch could represent.

    Pseudocode:
    1. Initialize an empty list `res` to store the possible times.
    2. Iterate over the range of hours (0 to 11):
        a. Count the number of 1s in the binary representation of the hour.
    3. Iterate over the range of minutes (0 to 59):
        a. Count the number of 1s in the binary representation of the minute.
        b. If the sum of the counts of 1s in the hour and minute equals `turnedOn`:
            i. Format the time as "h:mm" and append it to `res`.
    4. Return the list `res` containing all possible times.
    """
    def readBinaryWatch(self, turned_on: int) -> List[str]:
        possible_times = []
        
        # Iterate over all possible hours (0 to 11)
        for hour in range(12):
            hour_leds_on = bin(hour).count("1")
            
            # Iterate over all possible minutes (0 to 59)
            for minute in range(60):
                minute_leds_on = bin(minute).count("1")
                
                # Check if the total number of LEDs on matches the given number
                if hour_leds_on + minute_leds_on == turned_on:
                    # Format the time as "h:mm" and add to the result list
                    possible_times.append(f"{hour}:{minute:02d}")
        
        return possible_times