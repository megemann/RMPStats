import pandas as pd

def get_mandatory_attendance_by_year(df):
    df = df.dropna(subset=['attendanceMandatory'])
    df['attendanceMandatory'] = df['attendanceMandatory'].map({'mandatory': 1, 'non mandatory': 0, 'Y': 1, 'N': 0})
    df = df[df['attendanceMandatory'].isin([0,1])]
    df = df.sort_values('datetime')
    df['year'] = df['datetime'].dt.year
    yearly_means = df.groupby('year')['attendanceMandatory'].mean().reset_index()
    yearly_means['datetime'] = pd.to_datetime(yearly_means['year'].astype(str) + '-01-01')
    yearly_means['datetime'] = yearly_means['datetime'].dt.strftime('%Y-%m-%d %H:%M:%S')
    yearly_means['attendanceMandatory'] = yearly_means['attendanceMandatory'].astype(float)
    return yearly_means[['datetime', 'attendanceMandatory']].rename(columns={'attendanceMandatory': 'attendance_mandatory_percentage'})

def get_reviews_by_month_year(df):
    # Get min and max dates
    min_date = df['datetime'].min()
    max_date = df['datetime'].max()
    
    # Create date range for all months between min and max
    date_range = pd.date_range(start=min_date, end=max_date, freq='ME')
    
    # Create monthly counts
    monthly_counts = df.groupby(df['datetime'].dt.to_period('M')).size().reset_index()
    monthly_counts.columns = ['month_year', 'count']
    
    # Create full date range DataFrame
    result = pd.DataFrame({
        'month_year': date_range.to_period('M'),
        'count': 0
    })
    
    # Update counts where data exists
    for idx, row in monthly_counts.iterrows():
        mask = result['month_year'] == row['month_year']
        result.loc[mask, 'count'] = int(row['count'])  # Convert to int for JSON serialization
    
    # Convert month_year to datetime string format
    result['month_year'] = result['month_year'].astype(str) + '-01'
    result['month_year'] = pd.to_datetime(result['month_year']).dt.strftime('%Y-%m-%d %H:%M:%S')
    
    return result
