{{ config(materialized='view') }}

select
    o.order_id,
    o.customer_id,
    c.customer_name,
    c.email,
    c.phone,
    c.signup_date,
    o.product_id,
    o.order_date,
    o.quantity,
    o.total_amount
from {{ ref('base_orders') }} o
join {{ ref('base_customers') }} c
    on o.customer_id = c.customer_id
