#import gradio as gr
import requests
import time
import base64
import pandas as pd
from Continous_Temporal import get_avg_difficulty, get_rolling_avg_difficulty, get_avg_quality, get_rolling_avg_quality, get_avg_would_take_again, get_rolling_avg_would_take_again
from Statistics import get_mean_difficulty, get_mean_quality, get_would_take_again_percentage, get_attendance_mandatory_percentage, get_top_tags, get_comment_length, get_is_online_percentage, get_is_for_credit_percentage
from Discrete_Temporal import get_mandatory_attendance_by_year, get_reviews_by_month_year
from Categorical import get_rating_tags_distribution, get_quality_distribution, get_difficulty_distribution, get_grade_distribution
#delete imports
import matplotlib.pyplot as plt



def get_all_reviews(professor_id):
    headers = {
        'Authorization': 'Basic dGVzdDp0ZXN0',
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    # Encode the professor_id in base64
    encoded_professor_id = base64.b64encode(f"Teacher-{professor_id}".encode()).decode()
    
    rev_list = []
    has_next_page = True
    end_cursor = None
    
    while has_next_page:
        # Add the after parameter if we have an end cursor
        ratings_params = "first: 1000"
        if end_cursor:
            ratings_params += f', after: "{end_cursor}"'
            
        payload = {
            "query": f"""query GetTeacherRatings($id: ID!) {{
                node(id: $id) {{
                    ... on Teacher {{
                        id firstName lastName
                        school {{ name }}
                        ratings({ratings_params}) {{
                            edges {{
                                node {{
                                    comment class difficultyRating qualityRating
                                    createdByUser attendanceMandatory wouldTakeAgain
                                    isForCredit textbookUse date grade ratingTags clarityRating
                                    helpfulRating isForOnlineClass thumbsUpTotal thumbsDownTotal
                                }}
                            }}
                            pageInfo {{
                                hasNextPage
                                endCursor
                            }}
                        }}
                    }}
                }}
            }}""",
            "variables": {
                "id": encoded_professor_id
            }
        }
        
        response = requests.post(
            "https://www.ratemyprofessors.com/graphql",
            json=payload,
            headers=headers
        )
        if response.status_code == 429:
            print("Rate limit exceeded, waiting 10 seconds before retrying...")
            time.sleep(10)
            continue

        if response.status_code == 503:
            print("Rate limit exceeded, waiting 10 seconds before retrying...")
            time.sleep(10)
            continue
        
        if response.status_code != 200:
            print(f"Error: Status code {response.status_code}")
            print(response.text)
            return None
            
        data = response.json()
        
        # Check for errors in the response
        if 'errors' in data:
            print("GraphQL Errors:", data['errors'])
            return None
            
        node_list = data['data']['node']['ratings']['edges']
        page_info = data['data']['node']['ratings']['pageInfo']
        
        # Add professor_id to each review and append to results
        for node in node_list:
            node['node']['pid'] = professor_id
            rev_list.append(node['node'])
            
        # Update pagination info
        has_next_page = page_info['hasNextPage']
        end_cursor = page_info['endCursor']
        
        # Add a small delay between requests
        if has_next_page:
            time.sleep(0.5)
            
    return rev_list

def analyze_reviews(pid: str, params: dict):
    reviews = pd.DataFrame(get_all_reviews(pid))
    reviews['datetime'] = pd.to_datetime(reviews['date'].str.replace('+0000 UTC', 'UTC'), format='%Y-%m-%d %H:%M:%S UTC')
    reviews = reviews.drop(columns=['date'])

    data = {}


    Continous_Temporal = {}
    Continous_Temporal['avg_difficulty'] = get_avg_difficulty(reviews)
    Continous_Temporal['avg_quality'] = get_avg_quality(reviews)
    Continous_Temporal['avg_would_take_again'] = get_avg_would_take_again(reviews)
    if 'Rolling_Window_Year' in params:
        Continous_Temporal['rolling_avg_difficulty'] = get_rolling_avg_difficulty(reviews, params['Rolling_Window_Year'])
        Continous_Temporal['rolling_avg_quality'] = get_rolling_avg_quality(reviews, params['Rolling_Window_Year'])
        Continous_Temporal['rolling_avg_would_take_again'] = get_rolling_avg_would_take_again(reviews, params['Rolling_Window_Year'])
    else:
        Continous_Temporal['rolling_avg_difficulty'] = get_rolling_avg_difficulty(reviews)
        Continous_Temporal['rolling_avg_quality'] = get_rolling_avg_quality(reviews)
        Continous_Temporal['rolling_avg_would_take_again'] = get_rolling_avg_would_take_again(reviews)


    Statistics = {}
    Statistics['mean_difficulty'] = get_mean_difficulty(reviews)
    Statistics['mean_quality'] = get_mean_quality(reviews)
    Statistics['would_take_again_percentage'] = get_would_take_again_percentage(reviews)
    Statistics['attendance_mandatory_percentage'] = get_attendance_mandatory_percentage(reviews)
    Statistics['top_tags'] = get_top_tags(reviews)
    Statistics['comment_length'] = get_comment_length(reviews)
    Statistics['is_online_percentage'] = get_is_online_percentage(reviews)
    Statistics['is_for_credit_percentage'] = get_is_for_credit_percentage(reviews)

    Discrete_Temporal = {}
    
    Discrete_Temporal['attendance_mandatory_percentage'] = get_mandatory_attendance_by_year(reviews)
    Discrete_Temporal['reviews_by_month_year'] = get_reviews_by_month_year(reviews)

    Categorical = {}
    Categorical['rating_tags_distribution'] = get_rating_tags_distribution(reviews)
    Categorical['quality_distribution'] = get_quality_distribution(reviews)
    Categorical['difficulty_distribution'] = get_difficulty_distribution(reviews)

    data['Continous_Temporal'] = Continous_Temporal
    data['Statistics'] = Statistics
    data['Discrete_Temporal'] = Discrete_Temporal
    data['Categorical'] = Categorical
    data['reviews'] = reviews

    return data

def display_V1(result):
    if 'Continous_Temporal' in result:
        for key, value in result['Continous_Temporal'].items():
            plt.figure(figsize=(10, 6))
            plt.plot(value['datetime'], value[key])
            plt.xlabel('Date')
            plt.ylabel(key)
            plt.title(f'{key} Over Time')
            plt.show()

    if 'Statistics' in result:
        for key, value in result['Statistics'].items():
            print(f'{key}: {value}')

    if 'Discrete_Temporal' in result:
        if 'reviews_by_month_year' in result['Discrete_Temporal']:
            monthly_reviews = result['Discrete_Temporal']['reviews_by_month_year']

            plt.figure(figsize=(10, 6))
            plt.plot(range(len(monthly_reviews)), monthly_reviews['count'])

            # Create labels for every third month
            all_months = monthly_reviews['month_year'].astype(str)
            xtick_positions = range(len(all_months))
            xtick_labels = [label if i % 3 == 0 else '' for i, label in enumerate(all_months)]

            plt.xticks(xtick_positions, xtick_labels, rotation=45)
            plt.xlabel('Month-Year')
            plt.ylabel('Number of Reviews')
            plt.title('Reviews by Month')
            plt.tight_layout()
            plt.show()

        if 'attendance_mandatory_percentage' in result['Discrete_Temporal']:
            plt.figure(figsize=(10, 6))
            attendance_mandatory = result['Discrete_Temporal']['attendance_mandatory_percentage']
            plt.bar(attendance_mandatory['datetime'].dt.year, attendance_mandatory['attendance_mandatory_percentage'])
            plt.xlabel('Year')
            plt.ylabel('Attendance Mandatory Percentage')
            plt.title('Distribution of Attendance Mandatory Percentage by Year')
            plt.show()

    if 'Categorical' in result:
        for key, value in result['Categorical'].items():
            plt.figure(figsize=(10, 6))
            plt.bar(value.keys(), value.values())
            plt.xticks(rotation=45, ha='right')
            plt.xlabel('Label')
            plt.ylabel('Count')
            plt.title(f'Distribution of {key}')
            plt.show()


if __name__ == "__main__":
    result = analyze_reviews(1918813, {})
    display_V1(result)