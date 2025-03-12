def get_avg_difficulty(df):
    df = df.sort_values('datetime')
    df['avg_difficulty'] = df['difficultyRating'].expanding().mean().astype(float)
    df['datetime'] = df['datetime'].dt.strftime('%Y-%m-%d %H:%M:%S')
    return df[['datetime', 'avg_difficulty']]

def get_rolling_avg_difficulty(df, window_years=3):
    window_days = f"{365 * window_years}D"
    df = df.sort_values('datetime')
    df = df.set_index('datetime')
    df['rolling_avg_difficulty'] = df['difficultyRating'].rolling(window=window_days, min_periods=1).mean().astype(float)
    df = df.reset_index()
    df['datetime'] = df['datetime'].dt.strftime('%Y-%m-%d %H:%M:%S')
    return df[['datetime', 'rolling_avg_difficulty']]
    
def get_avg_quality(df):
    df = df.sort_values('datetime')
    df['avg_quality'] = df['qualityRating'].expanding().mean().astype(float)
    df['datetime'] = df['datetime'].dt.strftime('%Y-%m-%d %H:%M:%S')
    return df[['datetime', 'avg_quality']]

def get_rolling_avg_quality(df, window_years=3):
    window_days = f"{365 * window_years}D"
    df = df.sort_values('datetime')
    df = df.set_index('datetime')
    df['rolling_avg_quality'] = df['qualityRating'].rolling(window=window_days, min_periods=1).mean().astype(float)
    df = df.reset_index()
    df['datetime'] = df['datetime'].dt.strftime('%Y-%m-%d %H:%M:%S')
    return df[['datetime', 'rolling_avg_quality']]

def get_avg_would_take_again(df):
    df = df.dropna(subset=['wouldTakeAgain'])
    df = df.sort_values('datetime')
    df['avg_would_take_again'] = df['wouldTakeAgain'].expanding().mean().astype(float)
    df['datetime'] = df['datetime'].dt.strftime('%Y-%m-%d %H:%M:%S')
    return df[['datetime', 'avg_would_take_again']]

def get_rolling_avg_would_take_again(df, window_years=3):
    window_days = f"{365 * window_years}D"
    df = df.dropna(subset=['wouldTakeAgain'])
    df = df.sort_values('datetime')
    df = df.set_index('datetime')
    df['rolling_avg_would_take_again'] = df['wouldTakeAgain'].rolling(window=window_days, min_periods=1).mean().astype(float)
    df = df.reset_index()
    df['datetime'] = df['datetime'].dt.strftime('%Y-%m-%d %H:%M:%S')
    return df[['datetime', 'rolling_avg_would_take_again']]
