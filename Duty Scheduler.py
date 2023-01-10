import calendar as module

###############################################
#
# Faux Global Variables
#
###############################################
dow_dict = {
    0:"Monday",
    1:"Tuesday",
    2:"Wednesday",
    3:"Thursday",
    4:"Friday",
    5:"Saturday",
    6:"Sunday"
    }

ra_dict = dict()

###############################################
#
# RA Object Class
#
###############################################
class RA():
    def __init__(self, first_name, last_name):
        # RA Information
        self.first_name = first_name
        self.last_name = last_name
        self.duty_days = []

        # Day Preferences
        self.blocked_days = []
        self.prefered_dow = []
        self.backup_dow = []

    def set_all_day_types(self, data):
        """Sets up blocked, prefered, and backup days all at once."""
        self.set_blocked_days(data[0])
        self.set_prefered_dow(data[1])
        self.set_backup_dow(data[2])

    def set_blocked_days(self, blocked):
        """Days the RA is unable to work.  (M, D)"""
        self.blocked_days = blocked

    def set_prefered_dow(self, prefered):
        """List of days of the week RA prefers to work.  
        Dow must be Integers between 0-6"""
        self.prefered_dow = prefered

    def set_backup_dow(self, backup):
        """List of days of the week RA prefers to work if primary unavaialbe.
            Dow must be Integers between 0-6"""
        self.backup_dow = backup

###############################################
#
# Single Duty Day Object Class
#
###############################################
class DutyDay():
    def __init__(self, month, day, dow):
        self.special_day = False
        self.month = month
        self.day = day      # Day of the month
        self.dow = dow      # Day of the week
        self.primary_ra = None
        self.secondary_ra = None

    def set_special(self, boolean:bool):
        self.special_day = boolean

    def get_dow(self):
        """Convert numerical day or week into its ascii equivalent."""
        return dow_dict[self.dow]

    def get_details(self):
        """Delivery duty day information in a readable format."""
        print(f" {self.month}/{self.day} {self.get_dow()}")
        print(f" Primary: {self.primary_ra}")
        print(f" Secondary: {self.secondary_ra}")
        print("")
        
###############################################
#
# Calendar Class
#
###############################################
class DutyCalendar():
    def __init__(self, year:int, start_month:int, end_month:int):
        # Assign by input 
        self.start_month = start_month
        self.end_month =  end_month
        self.year = year

        # Each list in this object is a collection of unassigned DutyDays for that day of week.
        self.available_dow = [[] for dow in range(7)]
        self.monthly_cal = self.generate_blank_calendar()


    ###############################################
    #
    #   INITIALIZATION ONLY
    #   Construct Calendar 
    #
    ###############################################
    def generate_month(self, month):
        """Create an ordered list of day objects based on the specified month"""
        # Prepare Variables
        month_info = module.monthrange(self.year, month)    # Returns (weekday, number of days in month)
        dow = month_info[0]                                 # Current day of week
        total_days = month_info[1]                          # Number of days in month
        generated_month = []
        # Add Days
        for day in range(total_days):
            duty_day = DutyDay(month, day+1, dow)
            generated_month.append(duty_day)
            self.available_dow[dow].append(duty_day)                
            dow += 1
            # Reset day of week
            if dow == 7:
                dow = 0
        return generated_month
    
    def generate_blank_calendar(self):
        """Creates a dictionary.  The key is the month.  The entry
        The entry is an ordered list of day objects."""
        duty_dict = dict()
        cur_month = self.start_month
        while cur_month < self.end_month:
            duty_dict[cur_month] = self.generate_month(cur_month)
            cur_month += 1
        return duty_dict


    ###############################################
    #
    # User Functions
    #
    ###############################################
    def get_month(self, target_month = None):
        """Displays information about the specified month.
        If no month given, gives the entire calendar."""
        # Determine target range
        key = self.start_month
        if not target_month:
            target_month = self.end_month
        for day in self.monthly_cal[1]:
            day.get_details()
       

    ###############################################
    #
    # Calculate Available Days
    #
    ###############################################

    # Note that Monday is 0 and Sunday is 6.
    #self.days_remaining = [0 for amount in range(0,7)]

    ###############################################
    #
    # Add RAs
    #
    ###############################################

    # Note that Monday is 0 and Sunday is 6.
    #self.days_remaining = [0 for amount in range(0,7)]  



    ###############################################
    #
    # Assign Duty Functions
    #
    ###############################################

    def generate_duty_days(manual, blocked, preference):
        """Uses multiple different lists to assign duty days to the RAs.
        Blocked are days that someone has indicated they cannot do.
        Static that have been manually assigned.
        Preference includes which days people would prefer to have."""
        
        self.assign_manual(manual)
        self.assign_blocked(blocked)
        self.assign_preference(preference)
        
###############################################
#
# Misc Functions
#
###############################################

def get_weekday(month, day):
    """Returns day of week of specified day.  0 = Monday"""
    return module.weekday(self.year, month, day)




Duty = DutyCalendar(2022, 1, 5)
Duty.get_month()
#Duty.set_start((1,3))
#Duty.set_end((5,7))


ra_dict['Michael'] = RA('Michael', 'Scott')
ra_dict['Jim'] = RA('Jim', 'Halpert')
ra_dict['Pam'] = RA('Pam', 'Halpert')
ra_dict['Creed'] = RA('Creed', 'Bratton')
ra_dict['Dwight'] = RA('Dwight', 'Schrute')


manually_assigned_days = [('Michael', (2, 2)), ('Michael', (2, 3)), ('Michael', (2, 4)), ('Michael', (2, 5))]
blocked_


"""
# Hard Coded Days = [(name, (month, date)]

# Soft Coded Days = [(name, [no day list], [-prefered day of week 1, prefered day of week 2...], [secondary day 1, secondary day 2...])
prefered_days = [
    ('Michael', [0, 1], [2]),
    ('Jim', [0,2], []),
    ('Pam', [4,2], [2]),
    ('Creed', [], []),
    ('Dwight', [0,2], [3])
    ]
"""

# If special dates aren't hard coded they're assigned as regular days


