pizza = (["onion","pepper","olive"], ['mushroom', 'tomato', 'basil'], ['chicken','mushroom','pepper'], ['tomato','mushroom','basil'], ["chicken", "basil"])

# print(pizza[0])

random_string = input() 
num = [x for x in random_string.split(" ") if x.isnumeric()]
# print(num)

num_of_pizza = int(num[0])
num_of_team_of_2 = int(num[1])
num_of_team_of_3 = int(num[2])
num_of_team_of_4 = int(num[3])

input_list = []

for i in range(num_of_pizza):
    random_string = input()
    values = [x for x in random_string.split(" ")]
    input_list.append(values)

for i in range(num_of_pizza):
    for j in range(5):
        if pizza[j] == input_list[i][1::]:
            print("There's",input_list[i][0],"Pizza ", j)
        

