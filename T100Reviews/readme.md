# RateMyProfessors Top 100 Universities Dataset

## Dataset Description
This dataset contains professor reviews and metadata from the top 100 universities in the United States, collected from RateMyProfessors.com. The data includes detailed professor information, student reviews, and university metadata spanning from 1999 to 2025.

## File Structure

### 1. Universities Directory (`/Universities/{University_Name}/`)
Each university has its own directory containing:
- `professors.csv`: Professor information specific to that university
- `reviews.csv`: All reviews for professors at that university

### 2. Combined Directory (`/combined/`)
- `professors_index.csv`: Master list of all professors across universities
- `universities_metadata.csv`: Metadata for all universities in the dataset

## Schema Details

### professors.csv (Individual University Files)
| Column | Type | Description |
|--------|------|-------------|
| id | string | Unique identifier for the professor |
| name | string | Full name of the professor |
| department | string | Academic department of the professor |

### reviews.csv
| Column | Type | Description | Unique Values |
|--------|------|-------------|---------------|
| attendance_mandatory | string | Whether attendance is required | ['non mandatory', null, 'mandatory', 'Y', 'N', 'obrigatório'] |
| clarity_rating | float | Rating for professor's clarity (1-5) | [1.0, 2.0, 3.0, 4.0, 5.0] |
| class | string | Course code/identifier | varies |
| comment | string | Student's written review | varies |
| created_by_user | boolean | Whether review was created by a registered user | [False] |
| date | datetime | Date and time of review submission | varies |
| difficulty_rating | float | Rating for course difficulty (1-5) | [1.0, 2.0, 3.0, 4.0, 5.0] |
| grade | string | Grade received in the course | varies |
| helpful_rating | float | Rating for professor's helpfulness (1-5) | [1.0, 2.0, 3.0, 4.0, 5.0, -1.0] |
| is_for_credit | boolean | Whether course was taken for credit | [True, False] |
| is_for_online_class | boolean | Whether course was taken online | [True, False] |
| quality_rating | float | Overall quality rating (1-5) | [1.0, 2.0, 3.0, 4.0, 5.0] |
| textbook_use | float | Rating for textbook usage (-1 to 5) | [-1.0, 0.0, 1.0, 2.0, 3.0, 4.0, 5.0, null] |
| would_take_again | float | Whether student would take professor again | [0.0, 1.0, null] |
| pid | string | Professor ID (links to professors.csv) | varies |

### professors_index.csv
| Column | Type | Description |
|--------|------|-------------|
| id | string | Unique identifier for the professor |
| name | string | Full name of the professor |
| University | string | University name |
| University_ID | string | Unique identifier for the university |
| file_location | string | Path to professor's university directory |
| department | string | Academic department |
| first_review_date | datetime | Date of professor's first review |
| last_review_date | datetime | Date of professor's most recent review |

### universities_metadata.csv
| Column | Type | Description |
|--------|------|-------------|
| name | string | University name |
| id | string | Unique identifier for the university |
| base64 | string | Base64 encoded university ID |
| undergraduate_enrollment | float | Number of undergraduate students |
| location | string | City, State location |
| total_professors | float | Total number of professors |
| total_reviews | float | Total number of reviews |
| first_review_date | datetime | Date of university's first review |
| last_review_date | datetime | Date of university's most recent review |
| file_location | string | Path to university directory |

## Rating Scales
- **Quality, Clarity, Difficulty, Helpful Ratings**: 1 (lowest) to 5 (highest)
- **Textbook Use**: -1 (not used) to 5 (heavily used)
- **Would Take Again**: 0 (no), 1 (yes), null (not specified)

## Notes
- All timestamps are in UTC
- Some text fields may contain HTML entities
- Missing values are represented as null/NaN