
-- Clear all tables
DROP TABLE IF EXISTS Schedules;
DROP TABLE IF EXISTS Policy;
DROP TABLE IF EXISTS News;
DROP TABLE IF EXISTS Products;
DROP TABLE IF EXISTS Category;
DROP TABLE IF EXISTS Login_Attempts;
DROP TABLE IF EXISTS Session_Data;
DROP TABLE IF EXISTS Users;

-- Users
CREATE TABLE Users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    phone_no VARCHAR(20) UNIQUE,
    email VARCHAR(255),
    password VARCHAR(255),
    experience_in_farming INT
);

-- Transactions
CREATE TABLE Transactions(
    transaction_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    action VARCHAR(255),
    action_time TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

-- Session Data
CREATE TABLE activity_log (
    activity_id INT AUTO_INCREMENT PRIMARY KEY,
    session_key VARCHAR(255),
    user_id INT,
    activity VARCHAR(255),
    activity_time TIMESTAMP,
    ip_address VARCHAR(255),
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

-- Login Attempts
CREATE TABLE Login_Attempts (
    attempt_id INT AUTO_INCREMENT PRIMARY KEY,
    ip_address VARCHAR(255),
    attempt_time TIMESTAMP,
    user_id INT,
    used_password VARCHAR(255),
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

-- Market Place
-- Categories
CREATE TABLE Category (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    image_url TEXT
);

-- Products
CREATE TABLE Products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    category_id INT,
    price_per_unit DECIMAL(10, 2),
    unit_of_measurement VARCHAR(50),
    contact_info VARCHAR(255),
    available_units INT,
    owner_id INT,
    basic_description TEXT,
    image_url TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES Category(category_id),
    FOREIGN KEY (owner_id) REFERENCES Users(user_id)
);

-- News
CREATE TABLE News (
    news_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    description TEXT,
    link VARCHAR(255),
    picture TEXT,
    language VARCHAR(50),    
    date TIMESTAMP
);

-- Government Schemes
CREATE TABLE Policy (
    scheme_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    issued_by VARCHAR(255),
    eligibility TEXT,
    process TEXT,
    basic_description TEXT,
    link VARCHAR(255),
    time TIMESTAMP
);

-- Schedules
CREATE TABLE Schedules (
    schedule_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    crop_id INT,
    crop_name VARCHAR(255),
    start_date TIMESTAMP,
    end_date TIMESTAMP,
    area INT,
    owner_id INT,
    basic_description TEXT,
    FOREIGN KEY (owner_id) REFERENCES Users(user_id)
);
