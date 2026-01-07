SQL #1 (Easy) — Daily Active Users by Platform (JOINs + GROUP BY)
Problem statement
Compute Daily Active Users (DAU) for Instagram by event_date and platform. A user is “active” on a day if they generated at least one event that day.
Table schema(s)
events
•	event_id STRING
•	user_id BIGINT
•	event_time TIMESTAMP
•	event_name STRING
•	platform STRING -- e.g., 'ios','android','web'
•	app_id STRING
Required output columns
•	event_date (DATE)
•	platform (STRING)
•	dau (BIGINT)
Clarifying assumptions (pick 1–2)
•	Consider only app_id = 'instagram'.
•	Count distinct user_id per (event_date, platform).

  SELECT
  DATE(event_time) AS event_date,
  platform,
  COUNT(DISTINCT user_id) AS dau
FROM events
WHERE app_id = 'instagram'
GROUP BY DATE(event_time), platform;

________________________________________
SQL #2 (Easy→Medium) — Top Posts by Engagement Rate (JOINs + aggregation)
Problem statement
For posts created in the last 7 days, find the top 10 posts by engagement rate = (likes + comments) / impressions. Return ties by higher impressions, then newest post.
Table schema(s)
posts
•	post_id BIGINT
•	user_id BIGINT
•	created_time TIMESTAMP
post_daily_metrics
•	post_id BIGINT
•	metric_date DATE
•	impressions BIGINT
•	likes BIGINT
•	comments BIGINT
Required output columns
•	post_id
•	post_creator_user_id (from posts.user_id)
•	impressions_7d
•	likes_7d
•	comments_7d
•	engagement_rate_7d
Clarifying assumptions (pick 1–2)
•	Use metric_date for the 7-day window; include only rows where metric_date >= current_date - 7.
•	Exclude posts with impressions_7d = 0 from ranking (or treat rate as 0—choose one).

  SELECT
  p.post_id,
  p.user_id AS post_creator_user_id,
  SUM(m.impressions) AS impressions_7d,
  SUM(m.likes) AS likes_7d,
  SUM(m.comments) AS comments_7d,
  (SUM(m.likes) + SUM(m.comments)) * 1.0 / SUM(m.impressions) AS engagement_rate_7d
FROM posts p
JOIN post_daily_metrics m
  ON m.post_id = p.post_id
WHERE p.created_time >= CURRENT_DATE - 7
  AND m.metric_date >= CURRENT_DATE - 7
GROUP BY p.post_id, p.user_id
HAVING SUM(m.impressions) > 0
ORDER BY engagement_rate_7d DESC, impressions_7d DESC, MAX(p.created_time) DESC
LIMIT 10;
________________________________________
SQL #3 (Medium) — Day-1 Retention for New Users (retention + JOINs + GROUP BY)
Problem statement
Compute D1 retention by signup date for new Instagram users: among users who signed up on a day, what % returned and had any event the next day.
Table schema(s)
users
•	user_id BIGINT
•	signup_time TIMESTAMP
•	country STRING
events
•	event_id STRING
•	user_id BIGINT
•	event_time TIMESTAMP
•	event_name STRING
•	app_id STRING
Required output columns
•	signup_date (DATE)
•	new_users
•	returned_d1_users
•	d1_retention_rate (returned_d1_users / new_users)
Clarifying assumptions (pick 1–2)
•	Use app_id = 'instagram' for events.
•	“Returned D1” means an event on signup_date + 1 (calendar day), not within 24 hours.

WITH new_users AS (
  SELECT
    user_id,
    DATE(signup_time) AS signup_date
  FROM users
),
d1_returns AS (
  SELECT DISTINCT
    u.user_id,
    u.signup_date
  FROM new_users u
  JOIN events e
    ON e.user_id = u.user_id
   AND e.app_id = 'instagram'
   AND DATE(e.event_time) = u.signup_date + 1
)
SELECT
  u.signup_date,
  COUNT(*) AS new_users,
  COUNT(r.user_id) AS returned_d1_users,
  COUNT(r.user_id) * 1.0 / COUNT(*) AS d1_retention_rate
FROM new_users u
LEFT JOIN d1_returns r
  ON r.user_id = u.user_id
 AND r.signup_date = u.signup_date
GROUP BY u.signup_date
ORDER BY u.signup_date;
________________________________________
SQL #4 (Medium) — Signup → First Session → First Post Funnel (funnel + window functions)
Problem statement
Build a daily funnel for users who signed up each day:
1.	signed up
2.	had their first session start within 7 days
3.	created their first post within 7 days
Return counts at each step and conversion rates from signup.
Table schema(s)
users
•	user_id BIGINT
•	signup_time TIMESTAMP
sessions
•	session_id STRING
•	user_id BIGINT
•	session_start TIMESTAMP
•	platform STRING
posts
•	post_id BIGINT
•	user_id BIGINT
•	created_time TIMESTAMP
Required output columns
•	signup_date
•	signup_users
•	users_with_session_7d
•	users_with_post_7d
•	session_conv_rate
•	post_conv_rate
Clarifying assumptions (pick 1–2)
•	A user is counted in “session” if any session_start occurs within 7 days after signup (inclusive).
•	A user is counted in “post” if any post is created within 7 days after signup (inclusive), regardless of session.

  WITH signups AS (
  SELECT
    user_id,
    signup_time,
    DATE(signup_time) AS signup_date
  FROM users
),
first_session AS (
  SELECT
    s.user_id,
    MIN(se.session_start) AS first_session_start
  FROM signups s
  JOIN sessions se
    ON se.user_id = s.user_id
  GROUP BY s.user_id
),
first_post AS (
  SELECT
    s.user_id,
    MIN(p.created_time) AS first_post_time
  FROM signups s
  JOIN posts p
    ON p.user_id = s.user_id
  GROUP BY s.user_id
),
flags AS (
  SELECT
    s.signup_date,
    s.user_id,
    CASE
      WHEN fs.first_session_start IS NOT NULL
       AND fs.first_session_start <= s.signup_time + INTERVAL '7' DAY
      THEN 1 ELSE 0
    END AS has_session_7d,
    CASE
      WHEN fp.first_post_time IS NOT NULL
       AND fp.first_post_time <= s.signup_time + INTERVAL '7' DAY
      THEN 1 ELSE 0
    END AS has_post_7d
  FROM signups s
  LEFT JOIN first_session fs ON fs.user_id = s.user_id
  LEFT JOIN first_post fp ON fp.user_id = s.user_id
)
SELECT
  signup_date,
  COUNT(*) AS signup_users,
  SUM(has_session_7d) AS users_with_session_7d,
  SUM(has_post_7d) AS users_with_post_7d,
  SUM(has_session_7d) * 1.0 / COUNT(*) AS session_conv_rate,
  SUM(has_post_7d) * 1.0 / COUNT(*) AS post_conv_rate
FROM flags
GROUP BY signup_date
ORDER BY signup_date;

________________________________________
SQL #5 (Medium) — Conversation Reply Time (window functions + messages)
Problem statement
For each 1:1 conversation, compute the median reply time (in seconds) from one user’s message to the other user’s next message. Only consider reply gaps up to 24 hours.
Table schema(s)
messages
•	message_id STRING
•	conversation_id STRING
•	sender_user_id BIGINT
•	sent_time TIMESTAMP
•	message_type STRING -- 'text','image', etc.
conversations
•	conversation_id STRING
•	user_a_id BIGINT
•	user_b_id BIGINT
•	is_group BOOLEAN
Required output columns
•	conversation_id
•	median_reply_time_seconds
Clarifying assumptions (pick 1–2)
•	Filter to is_group = false.
•	A “reply” is defined as the next message in time where sender_user_id is different from the previous sender; ignore same-sender streaks when measuring reply time 
  (or measure from the last message in the streak—choose one).

  WITH base AS (
  SELECT
    message_id,
    conversation_id,
    sender_user_id,
    sent_time,
    DATE(sent_time) AS sent_date,
    message_text,
    LAG(sent_time) OVER (
      PARTITION BY conversation_id, sender_user_id, message_text
      ORDER BY sent_time
    ) AS prev_sent_time
  FROM messages
  WHERE message_text IS NOT NULL
    AND TRIM(message_text) <> ''
),
dupes AS (
  SELECT
    sent_date,
    conversation_id,
    sender_user_id,
    CASE
      WHEN prev_sent_time IS NOT NULL
       AND EXTRACT(EPOCH FROM (sent_time - prev_sent_time)) <= 10
      THEN 1 ELSE 0
    END AS is_dup
  FROM base
)
SELECT
  sent_date,
  conversation_id,
  sender_user_id,
  SUM(is_dup) AS duplicate_message_count
FROM dupes
GROUP BY sent_date, conversation_id, sender_user_id
HAVING SUM(is_dup) > 0
ORDER BY sent_date, conversation_id, sender_user_id;

________________________________________
SQL #6 (Medium) — Debugging/Data Quality: Detect Duplicate Ad Clicks (data quality + aggregation)
Problem statement
Your ads team suspects duplicate click logging. Identify (ad_id, user_id, click_date) combinations where the same user generated multiple clicks on the same ad within a 5-second window (likely duplicates). Output the number of suspicious click pairs per day.
Table schema(s)
ad_clicks
•	click_id STRING
•	ad_id BIGINT
•	user_id BIGINT
•	click_time TIMESTAMP
•	placement STRING
Required output columns
•	click_date (DATE)
•	ad_id
•	suspicious_user_count -- distinct users with duplicates that day for that ad
•	suspicious_click_events -- count of clicks that are part of a suspicious 5s window
Clarifying assumptions (pick 1–2)
•	Treat clicks as duplicates if there exists another click by the same (ad_id, user_id) within ±5 seconds (or only within +5 seconds forward—choose one).
•	Ignore users with high-frequency clicking patterns beyond 1 minute (or do not ignore—choose one).

