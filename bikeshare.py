import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ['chicago', 'new york city', 'washington']
    city = input('city you whould like to filter?\n').lower()
    while not city in cities:
        city = input('Error try angain')
    


    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    month = input('month you whould like to filter?\n').lower()
    while not month in  months:
        month = input('Not Correct')
   

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'all']
    day = input('day you whould like you filter?\n')
    while not day in days:
        month = input('Not Correct try angain')

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = month.index(month) +1
        
    if day != 'all':
        df =df[df['day_of_week'] == day.title()]
        

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print ('The Most Common Month is: ', most_common_month) 

    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print ('The Most Common Day is: ', most_common_day) 

    # TO DO: display the most common start hour
    Most_common_hour = df['hour'].mode()[0]
    print ('The Most Common Hour Is: ', Most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    Most_Common_ST = df['Start Station'].mode()[0]
    print ('The Most Common Start Station is: ', Most_Common_ST)


    # TO DO: display most commonly used end station
    Most_Common_ET = df['Start Station'].mode()[0]
    print ('The Most Common End Station is: ', Most_Common_ET)



    # TO DO: display most frequent combination of start station and end station trip
    print (Most_Common_ST + ' ' + Most_Common_ET)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    Total_Travel_Time = df['Trip Duration'].sum()
    print ('The Total Travel Time is: ', Total_Travel_Time)
    
    # TO DO: display mean travel time
    Mean_Travel_Time = df['Trip Duration'].mean()
    print ('The Mean Of all Travel time is: ', Mean_Travel_Time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    Count_UT = df['User Type'].value_counts()
    print ('The counts of user types is: ', Count_UT)

    # TO DO: Display counts of gender
    if 'Gender' in df:
        Counts_Genders = df['Gender'].value_counts()
        print ('The Count of Genders is: ', Counts_Genders) 
    else:
        print ('Washington no information for gender')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_Birth_Year = df['Birth Year'].min()
        print ('The Count of Birth Year is: ', earliest_Birth_Year) 
        most_recent_Birth_Year = df['Birth Year'].max()
        print ('The Count of Birth Year is: ', most_recent_Birth_Year) 
        common_Birth_Year = df['Birth Year'].mode()[0]
        print ('The Count of Birth Year is: ', common_Birth_Year)
    else:
        print ('Washington no information for Birth Year')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    #if user need to index 5 rows
    Ask_User1 = input('whould you like to view 5 rows?\n').lower()
    Number = 0
    if Ask_User1 == 'yes':
        Number += 5
        print (df[:Number])
    #if user need another 5 rows
    Ask_User2 = input('whould like to view another 5 rows?\n').lower()
    while Ask_User2 == 'yes':
        Number += 5
        print (df[:Number])
        Ask_User2 =input('whould like to view another 5 rows?\n').lower()
        if Ask_User2 == 'no':
            print ('Thank You \n Shehab Sallam')
    
         
        
    


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
