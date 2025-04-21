ALTER TABLE PESTDATA
ADD COLUMN IF NOT EXISTS TEMP_DIFF FLOAT;

-- Updating the TEMP_DIFF column with the difference between MaxT and MinT
UPDATE PESTDATA
SET TEMP_DIFF = MAXT - MINT
WHERE TEMP_DIFF IS NULL;

-- Analyzing the average pest value for different ranges of temperature difference
SELECT
    CASE
        WHEN TEMP_DIFF < 5 THEN 'Less than 5°C'
        WHEN TEMP_DIFF >= 5 AND TEMP_DIFF < 10 THEN '5-10°C'
        WHEN TEMP_DIFF >= 10 AND TEMP_DIFF < 15 THEN '10-15°C'
        WHEN TEMP_DIFF >= 15 THEN 'Greater than or equal to 15°C'
        ELSE 'Unknown'
    END AS temperature_difference_range,
    AVG(PESTVALUE) AS average_pest_value,
    COUNT(*) AS number_of_observations
FROM PESTDATA
GROUP BY temperature_difference_range
ORDER BY
    CASE temperature_difference_range
        WHEN 'Less than 5°C' THEN 1
        WHEN '5-10°C' THEN 2
        WHEN '10-15°C' THEN 3
        WHEN 'Greater than or equal to 15°C' THEN 4
        ELSE 5
    END;

-- Further analysis: Temperature difference and pest value by season
SELECT
    S.SEASON,
    CASE
        WHEN P.TEMP_DIFF < 5 THEN 'Less than 5°C'
        WHEN P.TEMP_DIFF >= 5 AND P.TEMP_DIFF < 10 THEN '5-10°C'
        WHEN P.TEMP_DIFF >= 10 AND P.TEMP_DIFF < 15 THEN '10-15°C'
        WHEN P.TEMP_DIFF >= 15 THEN 'Greater than or equal to 15°C'
        ELSE 'Unknown'
    END AS temperature_difference_range,
    AVG(P.PESTVALUE) AS average_pest_value,
    COUNT(*) AS number_of_observations
FROM PESTDATA P
JOIN (SELECT DISTINCT SEASON FROM PESTDATA) S
ON 1=1 -- Cross join to get all season combinations
WHERE P.SEASON = S.SEASON
GROUP BY S.SEASON, temperature_difference_range
ORDER BY S.SEASON,
    CASE temperature_difference_range
        WHEN 'Less than 5°C' THEN 1
        WHEN '5-10°C' THEN 2
        WHEN '10-15°C' THEN 3
        WHEN 'Greater than or equal to 15°C' THEN 4
        ELSE 5
    END;
