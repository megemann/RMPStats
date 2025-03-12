from Categorical import get_rating_tags_distribution

def get_mean_difficulty(df):
    return float(df['difficultyRating'].mean())

def get_mean_quality(df):
    return float(df['qualityRating'].mean())

def get_would_take_again_percentage(df):
    df = df.dropna(subset=['wouldTakeAgain'])
    return float(df['wouldTakeAgain'].mean())

def get_attendance_mandatory_percentage(df):
    df = df.dropna(subset=['attendanceMandatory'])
    df['attendanceMandatory'] = df['attendanceMandatory'].map({'mandatory': 1, 'non mandatory': 0, 'Y': 1, 'N': 0})
    df = df[df['attendanceMandatory'].isin([0,1])]
    return float(df['attendanceMandatory'].mean())

def get_top_tags(df):
    tags = get_rating_tags_distribution(df)
    # Convert tuples to lists for JSON serialization
    return [list(x) for x in sorted(tags.items(), key=lambda x: x[1], reverse=True)[:5]]

def get_comment_length(df):
    return float(df['comment'].apply(len).mean())

def get_is_online_percentage(df):
    df = df.dropna(subset=['isForOnlineClass'])
    df['isForOnlineClass'] = df['isForOnlineClass'].map({True: 1, False: 0})
    return float(df['isForOnlineClass'].mean())

def get_is_for_credit_percentage(df):
    df = df.dropna(subset=['isForCredit'])
    df['isForCredit'] = df['isForCredit'].map({True: 1, False: 0})
    return float(df['isForCredit'].mean())
