import pandas as pd
import matplotlib.pyplot as plt

import pandas as pd
import matplotlib.pyplot as plt

def plot_stock_data(df, date_column='date', stock_value_column='stock_value', title='Stock Value Over Time'):
    """
    Plots stock value over time from a CSV file.

    Args:
    - file_path (str): Path to the CSV file.
    - date_column (str): The name of the date column in the CSV file (default is 'date').
    - stock_value_column (str): The name of the stock value column in the CSV file (default is 'stock_value').
    - title (str): Title for the plot (default is 'Stock Value Over Time').
    """

    df[date_column] = pd.to_datetime(df[date_column], errors='coerce', format='%Y-%m-%d %H:%M:%S')

    df.dropna(subset=[date_column], inplace=True)

    plt.figure(figsize=(10, 6))
    plt.plot(df[date_column], df[stock_value_column], label=stock_value_column, color='b')

    plt.xlabel('Date')
    plt.ylabel('Stock Value')
    plt.title(title)

    plt.xticks(rotation=45)

    plt.grid(True)
    plt.legend()

    plt.tight_layout()
    plt.show()
def plot_publication_frequency(df, date_column='date'):
    """
    Plots the publication frequency of articles over time.
    
    Args:
        df (pd.DataFrame): The input DataFrame containing headlines and their dates.
        date_column (str): The column name for the date information.
    """
    # Ensure the date column is in datetime format
    df[date_column] = pd.to_datetime(df[date_column])
    
    # Count the number of articles published per day
    publication_counts = df.groupby(df[date_column].dt.date).size()
    
    # Plot the publication frequency over time
    plt.figure(figsize=(12, 6))
    plt.plot(publication_counts.index, publication_counts.values, marker='o', color='green', label="Publications per Day")
    plt.title("Publication Frequency Over Time")
    plt.xlabel("Date")
    plt.ylabel("Number of Articles")
    plt.xticks(rotation=45)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    plt.tight_layout()
    plt.show()


def plot_top_publishers(publisher_counts, top_n=10):
    
    top_publishers = publisher_counts.head(top_n)
    
    # Plot
    plt.figure(figsize=(10, 6))
    top_publishers.plot(kind='bar', color='skyblue')
    plt.title(f'Top {top_n} Publishers by Number of Articles')
    plt.xlabel('Publisher')
    plt.ylabel('Number of Articles')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def plot_sentiment_by_publisher(df, publisher_column, sentiment_column, top_n=10):
    """
    Plots the distribution of sentiment for the top publishers.

    Args:
        df (pd.DataFrame): The DataFrame containing the data.
        publisher_column (str): The name of the column containing publishers.
        sentiment_column (str): The name of the column containing sentiment labels (e.g., 'positive', 'negative', 'neutral').
        top_n (int): The number of top publishers to analyze. Default is 10.
    """
    # Get the top publishers
    top_publishers = df[publisher_column].value_counts().head(top_n).index

    # Filter the DataFrame for only the top publishers
    top_publishers_df = df[df[publisher_column].isin(top_publishers)]

    # Create a pivot table for sentiment counts by publisher
    sentiment_counts = top_publishers_df.pivot_table(
        index=publisher_column,
        columns=sentiment_column,
        aggfunc='size',
        fill_value=0
    )

    # Normalize sentiment counts to percentages
    sentiment_percentages = sentiment_counts.div(sentiment_counts.sum(axis=1), axis=0)

    # Plot
    sentiment_percentages.plot(
        kind='bar',
        stacked=True,
        figsize=(12, 6),
        colormap='tab10'
    )
    plt.title(f"Sentiment Distribution for Top {top_n} Publishers")
    plt.xlabel("Publisher")
    plt.ylabel("Percentage")
    plt.xticks(rotation=45)
    plt.legend(title="Sentiment")
    plt.tight_layout()
    plt.show()