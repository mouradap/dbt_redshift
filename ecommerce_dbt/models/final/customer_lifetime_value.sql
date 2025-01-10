{{ config(materialized='table') }}

select
    c.customer_id,
    c.customer_name,
    c.email,
    sum(o.total_amount) as lifetime_value,
    count(o.order_id) as total_orders,
    min(o.order_date) as first_order_date,
    max(o.order_date) as last_order_date
from {{ ref('orders_with_customers') }} o
join {{ ref('base_customers') }} c
    on o.customer_id = c.customer_id
group by c.customer_id, c.customer_name, c.email
