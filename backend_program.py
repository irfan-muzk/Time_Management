class TimeManagement:
    def __init__(self, user):
        self.user = user
        self.day = 24
        self.skills = ""
        self.priority = 0
        self.priority_in_a_weeks = 0
        self.priority_in_a_month = 0
        self.eat = 0
        self.bath = 0
        self.sleep = 0
        self.necessary_activity_hour = 0
        self.commuting_hour = 0
        self.weekly_commuting_hour = 0
        self.free_hour = 0

    def user_priority(self):
        print("Do you have any skills that you want to have? "
              "how many hours you want to spend"
              " practicing that skill every day")
        skills = input("insert the type of skill that you want to master: ")
        self.skills = skills
        self.priority = int(input("how many hour do you want to practice in a day? "
                             "insert a number like '2' "
                             "or type '0' if you dont: "))

        if self.priority > 0 and self.priority <= self.day: 
            while True:
                print("Do you want to take a break on saturday?")
                saturday = input("Type 'y' or 'n': ")
                print("Do you want to take a break on sunday?")
                sunday = input("Type 'y' or 'n': ")

                if saturday == "y" and sunday == "n" or saturday == "n" and sunday == "y":
                    self.priority_in_a_weeks += int(self.priority)*6
                    self.weekly_hour()
                    self.priority_in_a_month += int(self.priority)*26
                    self.monthly_hour()
                    break

                elif saturday == "n" and sunday == "n":
                    self.priority_in_a_weeks += int(self.priority)*7
                    self.weekly_hour()
                    self.priority_in_a_month += int(self.priority)*30
                    self.monthly_hour()
                    break

                elif saturday == "y" and sunday == "y":
                    self.priority_in_a_weeks += int(self.priority)*5
                    self.weekly_hour()
                    self.priority_in_a_month += int(self.priority)*22
                    self.monthly_hour()
                    break

                else:
                    print("Please enter 'y' or 'n'!")
                    continue 
                
        elif self.priority == 0:
            pass

    def weekly_hour(self):
        #part of taking a break function
        print(f"you will spend {self.priority_in_a_weeks} hours "
                                f"practicing {self.skills} in a week")
    def monthly_hour(self):
        #part of taking a break function
        print(f"you will spend {self.priority_in_a_month} hours "
                                f"practicing {self.skills} in a month")
         
    def necessary_activity(self):
        # in minute
        print("\nplease input how many 'minute' do you spend doing this activity.")
        print("only enter a number between 0 - 1440!")
        while True:
            self.eat = int(input("eating and preparing for foods: "))
            if self.eat > 0 or self.eat <= 1440:
                self.bath = int(input("taking a bath: "))
            else:
                continue
            if self.bath > 0 or self.bath <= 1440:
                self.sleep = int(input("\nhow many hour do you sleep in a day? "))
                if self.sleep > 0 or self.sleep <= 24:
                    break

        #convert minute to hour
        total_necessary_activity = self.eat + self.bath
        convert_minute_hour = total_necessary_activity/60
        self.necessary_activity_hour = int(convert_minute_hour + self.sleep)

    def commuting(self):
        #in minute
        print("\nplease input how many 'minute' do you spend commuting everyday.")
        print("only enter a number between 0 - 1440!")
        while True:
            commuting_minute = int(input("commuting everyday = "))
            if commuting_minute > 0 or self.eat <= 1440:
                weekly_commuting_days = int(input("for how many days in a week? "))
                if weekly_commuting_days > 0 or weekly_commuting_days <= 7:
                    break
                elif weekly_commuting_days < 0 or weekly_commuting_days > 7:
                    print("Please enter a number between 1 - 7")
                    continue
            else:
                print("Please enter a number between 0 - 1440")
                continue

        #convert minute to hour
        self.commuting_hour = commuting_minute/60
        weekly_commuting_minute = commuting_minute * weekly_commuting_days
        self.weekly_commuting_hour = weekly_commuting_minute/60

        #counting how much time left do the user have in a day
        self.free_hour += self.day - self.priority - self.necessary_activity_hour - self.commuting_hour

    def display_plan(self):
        report = (f"\nthis is your plan {self.user}: \n"
              f"- skill = {self.skills}\n"
              f"- priority = {self.priority} Hour\n"
              f"- priority in a week = {self.priority_in_a_weeks} Hour\n"
              f"- priority in a month = {self.priority_in_a_month} Hour\n"
              f"- commuting hour = {self.commuting_hour} Hour\n"
              f"- weekly commuting hour = {self.weekly_commuting_hour} Hour\n"
              f"\nnecessary activity: \n"
              f"- eat = {self.eat} Minute\n"
              f"- bath = {self.bath} Minute\n"
              f"- sleep = {self.sleep} Hour\n"
              f"Total necessary hour = {self.necessary_activity_hour} Hour\n"
              f"Free hours in a day = {self.free_hour} Hour\n")
        print(report)
        return report

    def save_plan(self):
        with open ("saving_data.txt", "a") as sp:
            sp.write(self.display_plan())