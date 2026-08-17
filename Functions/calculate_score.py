"""
Write a function calculate_score(base_score=0, *bonus_points, **penalties)
that computes a final score after adding bonuses and subtracting penalties.
"""

def calculate_score(base_score=0,*bonus_points,**penalties):
    total_score = base_score
    for point in bonus_points:
        total_score += point
    for penality,value in penalties.items():
        total_score -= value
    print("Final score :" ,total_score)

calculate_score(50,10,15,25,foul = 20,yellow_card = 15)
