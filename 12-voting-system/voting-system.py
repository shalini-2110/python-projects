import random

candidates = {"A": 0, "B": 0, "C": 0}
voted_names = []

num_voters = int(input("How many people will vote? "))

for i in range(num_voters):
    print(f"\n--- Voter {i+1} ---")
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))

    if age < 18:
        print("Not eligible to vote (must be 18+).")
        continue

    if name.lower() in [v.lower() for v in voted_names]:
        print("You have already voted.")
        continue

    voter_id = "VOT" + str(random.randint(1000, 9999))
    choice = input("Vote for candidate (A/B/C): ")

    if choice.upper() in candidates:
        candidates[choice.upper()] += 1
        voted_names.append(name)
        print("Vote recorded. Voter ID:", voter_id)
    else:
        print("Invalid candidate choice.")

print("\n===== ELECTION RESULTS =====")
for candidate in candidates:
    print("Candidate", candidate, ":", candidates[candidate], "votes")

winner = max(candidates, key=candidates.get)
print("\nWinner: Candidate", winner)