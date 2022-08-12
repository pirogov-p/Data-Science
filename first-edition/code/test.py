users = [
    { "id": 0, "name": "Hero" },
    { "id": 1, "name": "Dunn" },
    { "id": 2, "name": "Sue" },
    { "id": 3, "name": "Chi" },
    { "id": 4, "name": "Thor" },
    { "id": 5, "name": "Clive" },
    { "id": 6, "name": "Hicks" },
    { "id": 7, "name": "Devin" },
    { "id": 8, "name": "Kate" },
    { "id": 9, "name": "Klein" },
    { "id": 10, "name": "Jen" }
]

friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
               (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]


# first give each user an empty list
for a in users:

    a["friends_id"] = []



for i, j in friendships:
        # this works because users[i] is the user whose id is i
    users[i]["friends_id"].append(users[j]['id'])  # add i as a friend of j
    users[j]["friends_id"].append(users[i]['id'])  # add j as a friend of i

def number_of_friends(user):
    return len(user["friends_id"])  # length of friend_ids list

for user in users:
    user["num_of_friends"] = number_of_friends(user)

for user in users:
    print (user)
