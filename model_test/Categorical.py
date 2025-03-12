def get_rating_tags_distribution(df):
    Overall_tags = {}
    for tag in df['ratingTags']:
        if not isinstance(tag, str):
            continue
        for t in tag.split('--'):
            if t == '':
                continue
            t = str(t[:-1].replace(' ', '_') + t[-1] if t.endswith(' ') else t.replace(' ', '_').lower())
            if t not in Overall_tags:
                Overall_tags[str(t)] = int(1)  # Ensure integer type
            else:
                Overall_tags[str(t)] = int(Overall_tags[str(t)] + 1)  # Ensure integer type
    return Overall_tags

def get_quality_distribution(df):
    counts = df['qualityRating'].value_counts()
    return {str(k): int(v) for k, v in counts.items()}  # Convert numpy.int64 to int

def get_difficulty_distribution(df):
    counts = df['difficultyRating'].value_counts()
    return {str(k): int(v) for k, v in counts.items()}  # Convert numpy.int64 to int

def get_grade_distribution(df):
    grade_mapping = {
        'Not_Sure_Yet': 'Currently Enrolled',
        'Not sure yet': 'Currently Enrolled', 
        'Incomplete': 'Other',
        'Audit/No Grade': 'Other',
        'Drop/Withdraw': 'Other',
        'Rather_NOT_Say': 'User Withheld',
        'Rather not say': 'User Withheld',
        'Pass': 'Other',
        'Fail': 'Other',
        'wombo combo': 'Other',
        'A': 'A',
        'A-': 'A', 
        'B+': 'B',
        'B': 'B',
        'B-': 'B',
        'C+': 'C',
        'C': 'C',
        'C-': 'C',
        'D+': 'D',
        'D': 'D',
        'D-': 'D',
        'F': 'F',
        'F-': 'F',
        'F+': 'F',
    }
    mapped = df['grade'].map(grade_mapping)
    counts = mapped.value_counts()
    return {str(k): int(v) for k, v in counts.items()}  # Convert numpy.int64 to int
