-- Total log count
SELECT COUNT(*) FROM processed_logs;

-- Total errors (status_code = 500)
SELECT COUNT(*) AS error_count
FROM processed_logs
WHERE status_code = 500;

-- Most accessed endpoints
SELECT endpoint, COUNT(*) AS hits
FROM processed_logs
GROUP BY endpoint
ORDER BY hits DESC;

-- Users with most failures
SELECT user_id, COUNT(*) AS failures
FROM processed_logs
WHERE status_code >= 400
GROUP BY user_id
ORDER BY failures DESC;
