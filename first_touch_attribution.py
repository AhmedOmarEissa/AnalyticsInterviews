#https://www.interviewquery.com/questions/first-touch-attribution

# The schema below is for a retail online shopping company consisting of two tables, attribution and user_sessions.
# The attribution table logs a session visit for each row.
# If conversion is true, then the user converted to buying on that session.
# The channel column represents which advertising platform the user was attributed to for that specific session.
# Lastly the user_sessions table maps many to one session visits back to one user.
# First touch attribution is defined as the channel with which the converted user was associated when they first discovered the website.
# Calculate the first touch attribution for each user_id that converted.

# Example:
import pandas as pd

attribution = {
    'session_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'channel': ['facebook', 'facebook', 'email', 'facebook', 'email', 'organic', 'organic', 'facebook', 'email', 'email'],
    'conversion': [0, 1, 0, 0, 1, 0, 0, 1, 0, 1]
}
user_sessions = {
    'session_id': [1, 2, 3, 4, 5, 6, 7, 8],
    'user_id': [86, 67, 86, 16, 66, 15, 5, 99],
    'created_at': ["2020-09-28 00:00:00", "2019-09-12 00:00:00", "2020-08-28 00:00:00", "2019-11-16 00:00:00", "2020-10-24 00:00:00", "2020-04-06 00:00:00", "2020-01-28 00:00:00", "2020-02-28 00:00:00"]
}
attribution = pd.DataFrame(attribution)

user_sessions = pd.DataFrame(user_sessions)


def first_touch_attribution(
    attribution: pd.DataFrame,
     user_sessions: pd.DataFrame
     ):
    user_sessions['created_at'] = pd.to_datetime(user_sessions['created_at'])

    merged_dataset = user_sessions.merge(attribution).sort_values(by = 'created_at').reset_index(drop= True)
    user_summary = merged_dataset.groupby('user_id').agg(
        converted=('conversion', 'max'),
        first_sign_date=('created_at', 'min'),
        first_sign_index=('created_at', 'idxmin')
        )

    user_summary = merged_dataset.merge(user_summary,left_index= True , right_on=['first_sign_index'])
    user_summary = user_summary[user_summary.converted == 1 ]
    return user_summary[["channel","user_id"]]



if __name__ == "__main__":
    print(first_touch_attribution(attribution,user_sessions))
