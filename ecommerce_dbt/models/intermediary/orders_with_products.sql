{{ config(materialized='view') }}

select
    o.order_id,
    o.customer_id,
    o.product_id,
    p.product_name,
    p.category,
    o.order_date,
    o.quantity,
    o.total_amount
from {{ ref('base_orders') }} o
join {{ ref('base_products') }} p
    on o.product_id = p.product_id
