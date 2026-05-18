runs = int(input("Enter the runs:"))
overPlayed = int(input("Enter the over played:"))
targetScore = int(input("Enter the target score:"))

run_rate = runs / overPlayed if overPlayed > 0 else 0
print(f"run rate: {run_rate}")

target_achieved = runs >= targetScore
print(f"Target achieved: {target_achieved}")

runs_needed = targetScore - runs
print(f"Runs needed: {runs_needed}")


rate_above= run_rate > 8
print(f"Rate above 8: {rate_above}")