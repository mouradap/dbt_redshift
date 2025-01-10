{{ config(materialized='table') }}

select
    p.category,
    count(distinct o.order_id) as total_orders,
    sum(o.quantity) as total_quantity,
    sum(o.total_amount) as total_revenue
from {{ ref('orders_with_products') }} o
join {{ ref('base_products') }} p
    on o.product_id = p.product_id
group by p.category
order by total_revenue desc
