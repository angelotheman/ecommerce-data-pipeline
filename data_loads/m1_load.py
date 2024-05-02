#!/usr/bin/python3
"""
This module loads the csv file into postgres database
"""
import psycopg2
import os


# Set the env variables
user = os.getenv('POSTGRES_USER')
password = os.getenv('POSTGRES_PWD')
host = os.getenv('POSTGRES_HOST')   
database = os.getenv('POSTGRES_DB')
port = os.getenv('POSTGRES_PORT')


# Connect to the database
conn = psycopg2.connect(
        dbname=database,
        user=user,
        password=password,
        host=host,
        port=port
    )

# Open cursor
cur = conn.cursor()
"""
Order ID,Order Status,Category Name,SKU,Quantity,Unit Price,Cost Price,Total Cost Price,Total Price,Order Total,Sub Total,Payment Method,Currency Symbol,Customer ID,Merchant ID,Description,Distance (in km),Order Time,Pickup Time,Delivery Time,Consumed Loyalty Points
11265015,ORDERED,Cooking Fat & Oil,KKCO0487,1,4400,4250,4250,4400,4350.0,4400,CASH,KSh,3755460,893555,Not Available,10.9,2022-02-17T16:36:27.000Z,2022-02-17T16:37:16.000Z,2022-02-18T08:00:00.000Z,-
11264651,ORDERED,Cleaning & Hygiene,KKPT280100,1,180,130,130,180,7255.0,7255,CASH,KSh,4541187,893555,Urgently deliver by 9.30am in the morning,6.99,2022-02-17T16:19:05.000Z,2022-02-17T16:19:53.000Z,2022-02-18T09:00:00.000Z,-"""
table_queries = [
        """
        CREATE TABLE IF NOT EXISTS m1_customers (
            id INTEGER,
            last_used_platform VARCHAR(10),
            is_blocked INTEGER,
            created_at TIMESTAMP,
            language VARCHAR(5),
            outstanding_amount INTEGER,
            loyalty_points INTEGER
            number_of_employees NUMERIC
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS m1_orders (
            id INTEGER,
            status VARCHAR(15),
            category_name TEXT,
            sku VARCHAR(20),
            quantity INTEGER,
            unit_price NUMERIC,
            cost_price NUMERIC,
            total_cost_price NUMERIC,
            total_price NUMERIC,
            order_total NUMERIC,
            sub_total NUMERIC,
            payment_method VARCHAR(20),
            currency_symbol VARCHAR(6),
            customer_id INTEGER,
            merchant_id INTEGER,
            description TEXT,
            distance_km NUMERIC,
            order_time TIMESTAMP,
            pickup_time TIMESTAMP,
            delivery_time TIMESTAMP,
            consumed_loyalty_points NUMERIC
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS m1_deliveries (
            id INTEGER,
            order_id INTEGER,
            relationship TEXT,
            team_name TEXT,
            task_type TEXT,


