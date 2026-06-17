create schema final_project2;
USE final_project2;

DROP TABLE IF EXISTS traffic;
DROP TABLE IF EXISTS weather;

CREATE TABLE weather (
    datetime     DATE,
    temp         DOUBLE,
    precip       DOUBLE,
    preciptype   VARCHAR(50),
    conditions   VARCHAR(100),
    weather_id   INT NOT NULL AUTO_INCREMENT,
    PRIMARY KEY (weather_id)
);

CREATE TABLE traffic (
    OBJECTID              BIGINT NOT NULL,
    ISSUE_DATE            DATETIME,
    ISSUE_TIME            VARCHAR(10),
    ISSUING_AGENCY_NAME   VARCHAR(100),
    VIOLATION_PROCESS_DESC VARCHAR(255),
    FINE_AMOUNT           DECIMAL(10,2),
    ACCIDENT_INDICATOR    CHAR(1),
    weather_weather_id    INT,
    PRIMARY KEY (OBJECTID),
    FOREIGN KEY (weather_weather_id) REFERENCES weather(weather_id)
);











