import pandas as pd

def transform(df):
    # Handling Missing Values: Fill or drop null values
    df = df.dropna()  # Alternatively, use df.fillna(method='ffill') for forward fill

    # Data Normalization: Example of min-max scaling (if applicable)
    if 'player_rating' in df.columns:
        df['player_rating'] = (df['player_rating'] - df['player_rating'].min()) / (df['player_rating'].max() - df['player_rating'].min())

    # Feature Engineering: Creating new columns
    df['goal_difference'] = df['home_score'] - df['away_score']
    df['match_outcome'] = df.apply(lambda x: 'Home Win' if x['goal_difference'] > 0 else ('Away Win' if x['goal_difference'] < 0 else 'Draw'), axis=1)

    # Data Aggregation: Grouping data for insights
    df['season'] = pd.to_datetime(df['date']).dt.year
    team_performance = df.groupby(['season', 'home_team'])['goal_difference'].sum().reset_index()

    # Data Formatting: Standardizing date format and renaming columns
    df['date'] = pd.to_datetime(df['date'])
    df = df.rename(columns={"home_team": "home", "away_team": "away", "home_score": "home_goals", "away_score": "away_goals"})

    print("✅ Data transformed successfully!")
    return df
