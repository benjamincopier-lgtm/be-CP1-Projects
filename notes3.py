scores= [85, 90, 78, 92, 88]

running_total=0
highest=0

for score in scores:
    running_total+= score
#far right is stop button
    if score > highest:
        highest=score

