# Matthew Landale
# Artificial Personality
# 1 November 2019

def main():

    aiNums = [[3, 5, 5 ,3, 3, 3],
              [0, 0, 0, 3, 3, 3],
              [0, 4, 4, 4, 4, 2],
              [5, 2, 2, 4, 1, 2]]

    ai = [["happy", "surprised", "surprised", "happy", "happy", "happy" ],
          ["angry", "angry", "angry", "happy", "happy", "happy"],
          ["angry", "sad", "sad", "sad", "sad","fearful"],
          ["surprised", "fearful", "fearful", "sad", "disgusted", "fearful"]]

    print("Which interaction?")
    print("reward, punish, threaten, or joke?")
    interaction = input("Enter interaction: ")
    interactionNum = 0
    emotion = 0

    emotions = ["angry", "disgusted", "fearful", "happy", "sad", "surprised"]
    while not(interaction == '', interaction.lower() == 'joke' or interaction.lower() == 'punish' or interaction.lower() == 'threaten' or interaction.lower() == 'reward'):
        print()
        print("Error: invalid interaction selection.")
        print("interactions are reward, punish, threaten, and joke")
        interaction = input("Enter interaction: ")
    while interaction != '':
        if interaction == 'joke':
            emotion = aiNums[1][emotion]
        elif interaction == 'reward':
            emotion = aiNums[0][emotion]
        elif interaction == 'threaten':
            emotion = aiNums[3][emotion]
        elif interaction == 'punish':
            emotion = aiNums[2][emotion]

        print(emotions[emotion])
        print("reward, punish, threaten, or joke?")
        interaction = input("Enter another interaction: ")
main()
