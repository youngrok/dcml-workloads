Shop Policy (Draft)

Core Principles
- Under no circumstances should customers or the shop incur unreasonable losses.
- All policies must be applied consistently without conflicts.

Purpose
- Define consistent rules for benefits, coupons, points, shipping fees, and refunds.

1) Benefits
- For a single order (or a single item), apply **only one** benefit from the available set.
- If multiple benefits are eligible, choose in this priority order:
  1) Highest discount rate (%)
  2) Highest discount amount
  3) Earliest start date
- Whether benefits can be combined with coupons is controlled by a flag.
  - Default: benefits and coupons are combinable.

2) Coupons
- Coupons can be combinable or non-combinable.
  - Non-combinable: only one coupon per order.
  - Combinable: may be used together, but if a non-combinable coupon is applied, **no other coupon can be applied**.
- If a coupon excludes other coupons, the UI must clearly disclose the restriction before application.
- If a non-combinable coupon is applied, **benefits are not applied**.
- Coupon types:
  1) Free shipping coupon (FREE_SHIPPING)
  2) Item discount coupon (ITEM_DISCOUNT)
  3) Order total discount coupon (ORDER_DISCOUNT)
- Application order (within one order):
  1) Free shipping coupon
  2) Item discount coupon
  3) Order total discount coupon
- Order total discount coupons apply **only to the item subtotal**, excluding shipping.

3) Points
- Points are deducted from the order total.
- Points apply after coupons.
- Even if the order total becomes zero, shipping fees may remain.

4) Shipping Fee
- Free shipping when item subtotal (before any benefit/coupon/point) is **>= 30,000 KRW**.
- Otherwise, a **5,000 KRW** shipping fee applies.
- If a free shipping coupon is applied, shipping is 0 regardless of the threshold.
- The free-shipping threshold is evaluated on the pre-discount item subtotal and must be shown to users at checkout.

5) Refunds
- Refunds are **item-level**.
- For partial refunds, recompute discounts/coupons/points/shipping by these rules:
  1) Recompute shipping based on the remaining item subtotal before any benefit/coupon/point after refund
  2) Item discount coupons are prorated by the refunded items based on item net amounts
  3) Order total discount coupons are prorated by item net amounts
  4) Threshold-based free shipping may be revoked if the remaining subtotal drops below 30,000 KRW; free shipping coupons remain valid
  5) Used points are refunded proportionally by item net amounts
- If a refund calculation would require additional payment from the customer (e.g., newly applied shipping exceeds refundable item value), the refund is floored at 0 and **no extra charge is collected**.
- Refund amount is floored at 0; negative refunds are not allowed.

6) Rounding / Precision
- All monetary amounts are integer KRW.
- For percentage discounts, round down.
- For proportional allocations, round down each item, then assign the leftover KRW to the refunded item(s) first; if none, assign to the lowest-priced remaining item.

Scenarios are documented in `test-scenario.md`.
