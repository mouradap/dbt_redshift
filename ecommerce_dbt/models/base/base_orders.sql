{{ config(materialized='view') }}

select
    order_id,
    customer_id,
    product_id,
    cast(order_date as date) as order_date,
    quantity,
    cast(total_amount as decimal(10, 2)) as total_amount
from {{ source('public', 'orders') }}
