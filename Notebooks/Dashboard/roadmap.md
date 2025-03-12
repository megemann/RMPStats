## **Features in the DataFrame**  
**(with Notes on Usefulness)**

- **attendanceMandatory** - ➖ Maybe useful, but lots of nulls  
- **clarityRating** - ❌ Outdated  
- **class** - ➖ Useful for class analysis (maybe in v2 or v3 of the dashboard)  
- **comment** - ✅ Useful  
- **createdByUser** - ❌ Useless  
- **date** - ✅ Time series data  
- **difficultyRating** - ✅ Useful  
- **grade** - ✅ Useful  
- **helpfulRating** - ❌ Outdated, specific to review  
- **isForCredit** - ➖ Maybe useful  
- **isForOnlineClass** - ➖ Maybe useful  
- **qualityRating** - ✅ Useful  
- **ratingTags** - ✅➖ Maybe useful, can show trends because they're standardized  
- **textbookUse** - ➖ Maybe useful  
- **thumbsDownTotal** - Only useful for specific reviews  
- **thumbsUpTotal** - Only useful for specific reviews  
- **wouldTakeAgain** - ✅ Useful  
- **pid** - ❌ Implied data  

---

## **Professor Page Features**

### **V1 (Basic)**
- **Quality rating over time**  
  - (1) Rolling window average  
  - (2) Overall average regardless of date  
- **Difficulty rating over time**  
  - (1) Rolling window average  
  - (2) Overall average regardless of date  
- **Would take again percentage**  
  - (1) Time series  
  - (2) Overall percentage  
- **Attendance mandatory percentage**  
  - (1) Overall percentage  
- **Rating tags distribution**  
  - (1) Overall distribution  
- **Is online**  
  - (1) Overall percentage  
- **Is for credit**  
  - (1) Overall percentage  
- **Comment**  
  - (1) Average comment length  
  - (2) Sentiment analysis  
- **Filter by class** (No analysis, just filter)  
- **Date span and heatmap/bar graph of reviews by date**
- **Rating tags distribution**  
  - (1) Make into categories (all options listed on RMP website)  
  - (2) Display over time  

### **V2 (Intermediate)**
- **Interaction score**  
  - (Display score) - Something with thumbs ups, thumbs downs, and number of comments  
- **Extractive summary of comments**  
- **Filter by class** (with overall class analysis)  
- **Average grade in class** (Note: may be skewed as reviewers are more likely to be those who did well or terribly)  
- **Review volume trends** (Are reviews increasing or decreasing over time?)  DOne in V1
- **Red flags analysis**  
  - Combination of low ratings + specific tags  
- **Tag Score**
- **Sentiment Analysis**
  

### **V3 (Advanced)**
- **Topic summarization**  
  - Use LDA (Latent Dirichlet Allocation) to identify topics  
  - Display topics and the comments associated with them  
- **Seasonal patterns in ratings** (e.g., Fall vs Spring semester comparisons)  
- **Best professors for classes**  
- **AI-generated teaching style summary**
- **Interaction score IMPROVEMENT** + Interaction score over time (based on school size std deviation and mean)
- **Allow users to assign positive and negative weights to certain tags**

### **V4 (Advanced ML)**
- **Predictive graph of difficulty rating**  
- **Cluster professors by rating and department** (if in top 100 US universities)  
- **Predict school size, rating, etc., from reviews**  
- **Course matching**  
  - Top 100 US universities, combine similar courses  
- **Review authenticity analysis**  
- **Time series prediction**  
- **Recommendation system** (Top 100 US universities)

---

## **Overall Stats - Home Page for Top 100 US Universities** (with Disclaimer)

### **V1 (Basic)**
- **Overall average quality rating**  
- **Overall average difficulty rating**  
- **Overall would take again percentage**  
- **Overall attendance mandatory percentage**  
- **Overall rating tags distribution**  
- **Ratings over time**  
- **Help the user better understand the data they’re viewing**  
- **Look at Preprocess & EDA for more ideas**

### **V2 (Intermediate)**
- **Interaction score** - Distribution
- **Department-level comparisons across universities**  
- **Gender analysis in ratings** (Generate by guess of first name)  
- **Course level distribution** (Intro vs advanced courses)  
- **Online vs In-person teaching effectiveness**  
- **University ranking correlation with ratings**  
- **Seasonal trends across universities**
- **Apply original overall to university page**


### **V3 (Advanced)**
- **Geographic analysis of rating patterns**  
- **Class size impact on ratings**  
- **Teaching experience correlation with ratings**  
- **Department-specific rating patterns**  
- **Rank universities by overall rating and other factors**

### **V4 (Advanced ML)**
- **Predictive graph of difficulty rating**  
- **Cluster professors by rating and department** (if in top 100 US universities)  
- **Predict school size, rating, etc., from reviews**  
- **Course matching**  
  - Top 100 US universities, combine similar courses  
- **Review authenticity analysis**  
- **Time series prediction**  
- **Recommendation system** (Top 100 US universities)
