'''Write a function 'traffic_light_action(color)' that simulates a simple traffic light system with three colors: 'red', 'yellow', and 'green'.

The function should print the corresponding action for each color:

 "red": Print "Stop"
"yellow": Print "Prepare to stop"
"green": Print "Go"
If the input color is invalid, print "Invalid color".


Input Format:

A single string `color` that represents the traffic light color. The color must be one of the following: "red", "yellow", or "green".

Output Format:

The function should print the corresponding action for the color provided.



Constraints:

The input `color` is a string and must be one of the following format: "red", "yellow", or "green", and in lowercase.

'''


# Taking input
color = input()
a = "red", "yellow", "green"
def traffic_light_action(color):
    # Write your code
    if color=="red":
        print ("Stop")
    elif color=="yellow":
        print ("Prepare to stop")
    elif color=="green":
        print("Go")
    else:
        print ("Invalid color")

# Print the output
traffic_light_action(color)