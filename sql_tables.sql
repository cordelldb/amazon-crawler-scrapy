CREATE TABLE currency (
    id INT PRIMARY KEY AUTO_INCREMENT,
    currency_code CHAR(3) NOT NULL,
    currency_symbol CHAR(4) NOT NULL,
    full_name VARCHAR(255) NOT NULL,
    numeric_code INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
); 



CREATE TABLE listing (
    id INT PRIMARY KEY AUTO_INCREMENT,
    url VARCHAR(255) NOT NULL,
    product_id INT NOT NULL,
    marketplace_id VARCHAR(128) NOT NULL,
    base_url VARCHAR(128) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE country (
    code varchar(11) PRIMARY KEY,
    full_name varchar(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE platform ( 
    name varchar(100) PRIMARY KEY,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP 
);

CREATE TABLE seller (
    id int PRIMARY KEY AUTO_INCREMENT,
    name varchar(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE merchant (
    id int PRIMARY KEY AUTO_INCREMENT,
    marketplace_id int,
    seller_id int,
    external_id varchar(100),
    phone varchar(15),
    email varchar(255),
    address varchar(255),
    name varchar(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE product (
    id int PRIMARY KEY AUTO_INCREMENT,
    name varchar(255),
    upc bigint,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE listing (
    id int PRIMARY KEY AUTO_INCREMENT,
    url varchar(255),
    product_id int,
    marketplace_id int,
    external_id varchar(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE crawl_type (
    name varchar(255) PRIMARY KEY,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE crawl (
    id int PRIMARY KEY AUTO_INCREMENT,
    client_crawl_schedule_id int,
    crawl_type varchar(255),
    marketplace_id int,
    started timestamp,
    finished timestamp,
    params json,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE listing_snapshot (
    id int PRIMARY KEY AUTO_INCREMENT,
    buy_box_offer_id int,
    crawl_id int,
    listing_id int,
    time timestamp DEFAULT (now()),
    title varchar(255),
    description varchar(255),
    images json,
    rank int,
    rating float,
    marketplace_attrs json,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE merchant_snapshot (
    crawl_id int,
    merchant_id int,
    time timestamp DEFAULT (now()),
    rank int,
    rating float,
    marketplace_attrs json,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE offer (
    id int PRIMARY KEY AUTO_INCREMENT,
    listing_snapshot_id int,
    merchant_id int,
    time timestamp DEFAULT (now()),
    price float,
    condition varchar(255),
    buy_box_winner bool,
    rank int,
    marketplace_attrs json,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE client (
    id int PRIMARY KEY AUTO_INCREMENT,
    name varchar(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE scheduled_crawl (
    id int PRIMARY KEY AUTO_INCREMENT,
    marketplace_id int,
    client_id int,
    crawl_type varchar(255),
    params json,
    frequency varchar(10),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

INSERT INTO currency (currency_code, currency_symbol, full_name) VALUES 
('USD', '$', 'US Dollar'),
('CAD', 'C$', 'Canadian Dollar'),
('MXN', '₱', 'Mexican Peso');

INSERT INTO currency (currency_code, currency_symbol, full_name) VALUES 
('SGD', 'S$', 'Singapore Dolllar'),
('MYR', 'RM', 'Malaysian Ringgit'),
('IDR', 'Rp', 'Indonesian Rupiah'),
('THB', '฿', 'Thai Baht'),
('VND', '₫', 'Vietnamese Dong'),
('PHP', '₱', 'Philippine peso'),
('MMK', 'K', 'Myanma Kyat')

INSERT INTO currency (currency_code, currency_symbol, full_name) VALUES 
('EUR', '€', 'Euro'),
('GBP', '£', 'British pound'),
('CHF', 'Fr', 'Swiss Franc'),
('SEK', 'kr', 'Swedish Krona'),
('NOK', 'kr', 'Norwegian Krone'),
('DKK', 'kr', 'Danish Krone'),
('CZK', 'Kč', 'Czech Koruna'),
('PLN', 'zł', 'Polish Zloty'),
('ISK', 'kr', 'Icelandic Krona');

