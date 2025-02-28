"""
Project 5: Fair districting, Gerrymandering, Wasted Votes and Efficiency Gap.
Filename: VoteAndEfficiency.py
Author: Anh Tran
Date: March 1, 2024
"""


class Election:
    """
    Function creates three instances.
    parameters: (self, district number, democratic votes, republicant votes)
    return: district number, democratic votes, republicant votes.
    """

    def __init__(self, district_number, dem_votes, rep_votes):
        self.district_number = district_number
        self.dem_votes = dem_votes
        self.rep_votes = rep_votes


def read_data(filename: str):
    """
    Function going through file and organize the information.
    parameters: (filename: str)
    return: A dictionary with year, state, and called class to loop through democratic and republicant vote.
    """
    election_results = {}
    with open(filename, "r") as file:
        for line in file:
            parts = line.strip().split(",")
            year = parts[0]
            state = parts[1]
            districts = []
            # skip the first 2 values because it the year, and state index (0,1).
            # jump every three items since it count as one district.
            for i in range(2, len(parts), 3):
                district_number = parts[i]
                dem_votes = int(parts[i + 1])  # convert string to int
                rep_votes = int(parts[i + 2])
                # append the memory address to the dictionary list which allow looping to called class
                districts.append(Election(district_number, dem_votes, rep_votes))
            # append every year to dictionary
            if year not in election_results:
                election_results[year] = {}
            # add state as key, and append districts list that have been seperate every three item.
            election_results[year][state] = districts
    return election_results


def report_efficiency_gap(districts):
    """
    Function calculate wasted vote, and gap efficient for democrats and republicants.
    parameters: (districts: list of items in district)
    return: print the calculation, favor votes, and includes efficiency gap return in absolute value.
    """
    total_votes = 0
    half_votes = 0
    dem_wasted = 0
    rep_wasted = 0
    total_dem_votes = 0
    total_rep_votes = 0
    for d in districts:
        # for values in district, loop through and add items dem_votes and rep_votes called in class.
        total_votes = d.dem_votes + d.rep_votes
        total_dem_votes += d.dem_votes
        total_rep_votes += d.rep_votes
        # This help to determine state only need half to win.
        half_votes = total_votes / 2

        # if democratic win
        if d.dem_votes > d.rep_votes:
            # minutes the vote that unescessary to win
            dem_wasted += d.dem_votes - half_votes
            rep_wasted += d.rep_votes
        else:
            # if republicant win, vice versa to take total vote minus unnessesary use vote.
            rep_wasted += d.rep_votes - half_votes
            dem_wasted += d.dem_votes

    favor = "Democrats" if rep_wasted > dem_wasted else "Republicans"

    # this calculate given by (differences in waste btw democratic and republican) / (total_votes) * 100 for percentage
    gap = ((dem_wasted - rep_wasted) / (total_dem_votes + total_rep_votes)) * 100

    print(f"Wasted Democratic votes: {dem_wasted}")
    print(f"Wasted Republican votes: {rep_wasted}")
    # return absolute, positive value as percentage.
    print(f"Efficiency gap: {abs(gap):.1f}%, in favor of {favor}.")


def main():
    """
    Function keep function organize to know when a function being run, and when a function stop executing.
    parameters: None
    return: gap efficiency, wasted vote in democrats and republicants. Question to repeat program over.
    - Answer base on condition, if user doesn't answer question in correct format, a certain answer execute to assist user.
    """
    filename = "1976-2020votes.txt"
    election_results = read_data(filename)
    # starting sentence of the program
    print(
        "This program evaluates districting fairness for US House elections from 1976-2020."
    )
    stop = True  # Initialize stop to True to enter the loop
    while stop:
        year = input("What election year would you like to evaluate? ")
        # convert year string to int and check if condition if met, year in range and is even
        if int(year) % 2 == 0 and 1976 <= int(year) <= 2020:
            state_valid = False
            # this keep question being ask if 'state' enter is not valid.
            while not state_valid:
                state = input("What state would you like to evaluate? ").upper()
                # then if it exist in next answer start process checking validity in district valid.
                if state in election_results.get(year, {}):
                    state_valid = True
                else:
                    print(f"{state} is not a valid state for the year {year}.")

            # checking if district more than one district is be able calculate gap efficient.
            districts = election_results[year][state]

            if len(districts) == 1:
                print(
                    "Efficiency gap cannot be computed for states with only one district."
                )
            else:
                print(f"{len(districts)} districts.")
                report_efficiency_gap(districts)
                # this process is similar to while loop 'state' to not restart question untill receive yes/no answer.
                continue_prompt = input("Would you like to continue? (yes/no) ").lower()
                while continue_prompt not in ["yes", "no"]:
                    continue_prompt = input(
                        "Invalid input. Please enter 'yes' or 'no': "
                    ).lower()

                if continue_prompt == "no":
                    stop = False
        else:
            print("Sorry, valid election years are even years from 1976-2020.")


if __name__ == "__main__":
    main()
