"""
NOTE: This file is a part of the Billboard Project. It contains utility functions for visualizing the data.
Refer to the docstrings and `visualization_demo.ipynb` for detailed explanations and examples.
"""


import pandas as pd
import matplotlib.pyplot as plt

THEMES = [
 'Adventure',
 'Celebration',
 'Community',
 'Family',
 'Fantasy',
 'Feminism',
 'Friendship',
 'Heartbreak',
 'Individuality',
 'Love',
 'Nature',
 'Nostalgia',
 'Politics',
 'Religion',
 'Sexuality',
 'Struggle',
 'Violence',
 'Wealth'
 ]


def filter_long_lasting_songs(df, k):
    """
    Filters the DataFrame to include only those songs that lasted more than k weeks on the billboard.

    Parameters:
    - df: DataFrame containing the billboard data.
    - k: Minimum number of weeks a song must last on the billboard to be included in the returned DataFrame.

    Returns:
    - A DataFrame containing only the songs that lasted more than k weeks on the billboard.
    """
    # Group by 'song' and 'artist', filter groups by size, and get the indices
    lasting_songs_indices = df.groupby(['song', 'artist']).filter(lambda x: len(x) > k).index

    # Filter the original DataFrame to include only the lasting songs
    filtered_df = df.loc[lasting_songs_indices]

    return filtered_df

def plot_sentiment_scores_over_time(df, sentiments, start_date, end_date, grouping='monthly', events=None):
    """
    Plots the average sentiment scores over a given time range with specified grouping,
    and adds vertical lines for significant events.

    Parameters:
    - df: DataFrame containing the billboard data with date, rank, sentiment score columns.
    - sentiments: list of sentiment score column names to plot.
    - start_date: start date of the time range (inclusive).
    - end_date: end date of the time range (inclusive).
    - grouping: 'weekly', 'monthly', or 'yearly' to specify how to group dates.
    - events: Optional; list of tuples with (date, label) for significant events to mark on the plot.
    """
    
    # Filter the DataFrame for the given time range
    mask = (df['date'] >= start_date) & (df['date'] <= end_date)
    filtered_df = df.loc[mask]

    # Set the figure size
    plt.figure(figsize=(14, 7))

    # Determine the grouping frequency
    if grouping == 'weekly':
        freq = 'W'
    elif grouping == 'monthly':
        freq = 'M'
    elif grouping == 'yearly':
        freq = 'Y'
    else:
        raise ValueError("Grouping must be 'weekly', 'monthly', or 'yearly'.")

    # Loop through each sentiment score column and plot
    for sentiment in sentiments:
        # Group by the specified frequency and calculate the average sentiment score for the current column
        sentiment_avg = filtered_df.resample(freq, on='date').apply(lambda x: x[sentiment].mean())

        # Plot
        plt.plot(sentiment_avg, label=f'Average {sentiment} Score')

    # Adding vertical lines for specified events
    if events:
        for event_date, event_label in events: # event label is not used -- thinking about way to show properly
            plt.axvline(pd.to_datetime(event_date), linestyle='--', color='red')
        # Add a generic line to the legend for events
        plt.axvline(pd.to_datetime(events[0][0]), linestyle='--', color='red', label='Significant Events')

    # Setting the title, labels, and legend
    plt.title(f'Average Sentiment Scores ({grouping.capitalize()}) with Significant Events')
    plt.xlabel('Date')
    plt.ylabel('Average Sentiment Score')

    # Improve legend
    # Get handles and labels, then add a custom legend
    handles, labels = plt.gca().get_legend_handles_labels()
    by_label = dict(zip(labels, handles))  # Remove duplicate labels/handles
    plt.legend(by_label.values(), by_label.keys())
    
    plt.grid(True)

    # Show plot
    plt.show()


def plot_theme_percentage_over_time(df, themes, start_date, end_date, grouping='monthly', events=None):
    """
    Plots the percentage of songs with specified themes over a given time range with specified grouping,
    and adds vertical lines for significant events. Improves legend to distinguish between theme lines and event lines.

    Parameters:
    - df: DataFrame containing the billboard data with date, rank, and theme columns.
    - themes: list of theme column names to plot.
    - start_date: start date of the time range (inclusive).
    - end_date: end date of the time range (inclusive).
    - grouping: 'weekly', 'monthly', or 'yearly' to specify how to group dates.
    - events: Optional; list of tuples with (date, label) for significant events to mark on the plot.
    
    Note: use df read from song_sentiments_themes.csv
    """
    
    # Filter the DataFrame for the given time range
    mask = (df['date'] >= start_date) & (df['date'] <= end_date)
    filtered_df = df.loc[mask]

    # Set the figure size
    plt.figure(figsize=(14, 7))

    # Determine the grouping frequency
    if grouping == 'weekly':
        freq = 'W'
    elif grouping == 'monthly':
        freq = 'M'
    elif grouping == 'yearly':
        freq = 'Y'
    else:
        raise ValueError("Grouping must be 'weekly', 'monthly', or 'yearly'.")

    # Loop through each theme and plot
    for theme in themes:
        # Group by the specified frequency and calculate the percentage for the current theme
        theme_percentage = filtered_df.resample(freq, on='date').apply(lambda x: (x[theme].sum() / x[theme].count()) * 100 if x[theme].count() > 0 else 0)

        # Plot
        plt.plot(theme_percentage.index, theme_percentage, label=f'Percentage of "{theme}" Theme')

    # Adding vertical lines for specified events
    if events:
        for event_date, event_label in events: # event label is not used -- thinking about way to show properly
            plt.axvline(pd.to_datetime(event_date), linestyle='--', color='red')
        # Add a generic line to the legend for events
        plt.axvline(pd.to_datetime(events[0][0]), linestyle='--', color='red', label='Significant Events')

    # Setting the title, labels, and legend
    plt.title(f'Percentage of Songs with Specified Themes ({grouping.capitalize()}) with Significant Events')
    plt.xlabel('Date')
    plt.ylabel('Percentage of Songs')

    # Improve legend
    # Get handles and labels, then add a custom legend
    handles, labels = plt.gca().get_legend_handles_labels()
    by_label = dict(zip(labels, handles))  # Remove duplicate labels/handles
    plt.legend(by_label.values(), by_label.keys())

    plt.grid(True)

    # Show plot
    plt.show()

def plot_theme_distribution(df, themes=THEMES, title='Distribution of Themes Among Unique Songs'):
    """
    Creates a horizontal bar plot showing the distribution of themes among unique songs.
    
    Parameters:
    - df: DataFrame containing song data.
    - themes: List of theme column names.
    """
    # Drop duplicates based on 'song' and 'artist' to consider each unique song only once
    unique_songs_df = df.drop_duplicates(subset=['song', 'artist'])
    
    # Drop rows with NaN in any of the theme columns
    unique_songs_df = unique_songs_df.dropna(subset=themes)
    
    # Sum the theme columns and sort the values
    theme_distribution = unique_songs_df[themes].sum().sort_values()
    
    # Plotting
    theme_distribution.plot(kind='barh', figsize=(10, 6), color='skyblue', edgecolor='black')
    plt.title(title)
    plt.xlabel('Number of Songs')
    plt.ylabel('Themes')
    plt.grid(axis='x')
    plt.show()

def plot_weeks_on_chart(df, title = 'Distribution of Weeks on Billboard Chart'):
    
    """
    Plots the distribution of the number of weeks on the Billboard chart for each song.

    Parameters:
    - df: DataFrame containing the billboard data. 
     (You can filter the data to get the songs you are interested in beforehand)
    - title (optional): Title of the plot

    """
    
    weeks_on_chart = df.groupby(['song', 'artist']).size()

    plt.figure(figsize=(10, 6))
    weeks_on_chart.hist(bins=range(weeks_on_chart.min(), weeks_on_chart.max() + 1), edgecolor='black')
    plt.title(title)
    plt.xlabel('Number of Weeks')
    plt.ylabel('Number of Songs')
    plt.grid(axis='y')
    plt.show()

def plot_long_lasting_songs(df, n):
    """
    Plots the number of songs that lasted more than n weeks on the Billboard chart each year.

    Parameters:
    - df: DataFrame containing the billboard data with date, song, artist columns.
    - n: Minimum number of weeks a song must last to be considered.
    """

    # Convert 'date' to datetime and extract year
    df['date'] = pd.to_datetime(df['date'])
    df['year'] = df['date'].dt.year

    # Identify unique songs and calculate their total duration on the chart
    song_durations = df.groupby(['song', 'artist']).size().reset_index(name='duration')

    # Filter songs that lasted more than n weeks
    long_lasting_songs = song_durations[song_durations['duration'] > n]

    # Merge back with original df to get the years each song appeared in
    merged_df = pd.merge(df, long_lasting_songs[['song', 'artist']], on=['song', 'artist'])

    # Count the number of unique songs per year that lasted more than n weeks
    songs_per_year = merged_df.drop_duplicates(subset=['song', 'artist', 'year']).groupby('year').size()

    # Plotting
    plt.figure(figsize=(12, 6))
    songs_per_year.plot(kind='line', color='purple', marker='x')
    plt.title(f'Songs Lasting More Than {n} Weeks on Billboard Chart per Year')
    plt.xlabel('Year')
    plt.ylabel(f'Number of Songs (> {n} Weeks)')
    plt.axvline(x=1991, color='grey', linestyle='--', label='1991 Music Industry Change')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.legend()
    plt.tight_layout()
    plt.show()

def plot_weeks_on_chart_stats(df):
    """
    Plots the average and median number of weeks that unique songs stayed on the Billboard chart each year.

    Parameters:
    - df: *FULL* DataFrame containing the billboard data with date, song, artist, and weeks on chart columns.
    """

    # Extract year from the 'date' column
    df['year'] = pd.DatetimeIndex(df['date']).year

    # Group by year, song, and artist, then count the number of weeks each song was on the chart
    weeks_on_chart_per_song = df.groupby(['year', 'song', 'artist']).size()

    # Reset index to turn the grouped data back into a DataFrame
    weeks_on_chart_per_song = weeks_on_chart_per_song.reset_index(name='weeks_on_chart')

    # Calculate the average and median weeks on chart per year
    avg_weeks_per_year = weeks_on_chart_per_song.groupby('year')['weeks_on_chart'].mean()
    median_weeks_per_year = weeks_on_chart_per_song.groupby('year')['weeks_on_chart'].median()

    # Plotting
    plt.figure(figsize=(12, 6))
    plt.plot(avg_weeks_per_year.index, avg_weeks_per_year, label='Average Weeks on Chart', color='blue')
    plt.plot(median_weeks_per_year.index, median_weeks_per_year, label='Median Weeks on Chart', color='green', linestyle='--')
    plt.title('Average and Median Weeks on Billboard Chart per Year')
    plt.xlabel('Year')
    plt.ylabel('Weeks on Chart')
    plt.legend()
    plt.grid(True)
    plt.show()
