Test Scenarios (11)

Scenario 1: Benefit vs Fixed Benefit, Free Shipping + Item Coupon + Points
- Items: A 25,000; B 15,000 (Subtotal 40,000)
- Benefits: 10% off items vs 4,000 off items -> apply 10%
- Coupons: Free shipping (non-combinable), Item coupon 2,000 off B (combinable)
- Points: 3,000
Calculation:
  - Non-combinable coupon applied -> benefits NOT applied
  - Subtotal remains 40,000
  - Free shipping: Shipping 0
  - Points: 40,000 - 3,000 = 37,000
Result:
  - Items 37,000; Shipping 0; Total 37,000

Scenario 2: No Benefit, Order Discount Coupon, Points
- Items: A 18,000; B 9,000 (Subtotal 27,000)
- Coupon: Order discount 3,000
- Points: 2,000
Calculation:
  - After coupon: 24,000
  - After points: 22,000
  - Shipping: 5,000 (subtotal before discounts < 30,000)
Result:
  - Items 22,000; Shipping 5,000; Total 27,000

Scenario 3: Benefit Applied, Threshold Just Met
- Items: A 20,000; B 12,000 (Subtotal 32,000)
- Benefit: 5% off items
Calculation:
  - After benefit: A 19,000; B 11,400 (Subtotal 30,400)
  - Shipping: 0 (>= 30,000)
Result:
  - Items 30,400; Shipping 0; Total 30,400

Scenario 4: Free Shipping Coupon Persists After Refund
- Items: A 12,000; B 8,000 (Subtotal 20,000)
- Coupon: Free shipping (non-combinable)
- Refund: cancel B
Original:
  - Shipping: 0 (coupon)
Refund calculation:
  - Remaining subtotal: 12,000
Result:
  - Free shipping coupon remains valid
  - Shipping remains 0
  - Refund = 8,000

Scenario 5: Item Coupon Only (No Benefit)
- Items: A 10,000; B 10,000 (Subtotal 20,000)
- Coupon: Item discount 3,000 off B
Calculation:
  - B 10,000 -> 7,000 (Subtotal 17,000)
  - Shipping: 5,000
Result:
  - Items 17,000; Shipping 5,000; Total 22,000

Scenario 6: Order Coupon + Points, Threshold Exactly Met
- Items: A 18,000; B 12,000 (Subtotal 30,000)
- Coupon: Order discount 2,000
- Points: 3,000
Calculation:
  - After coupon: 28,000
  - After points: 25,000
  - Shipping: 0 (threshold evaluated on item subtotal 30,000)
Result:
  - Items 25,000; Shipping 0; Total 25,000

Scenario 7: Non-combinable Coupon Overrides Benefit
- Items: A 15,000; B 20,000 (Subtotal 35,000)
- Benefit: 3,000 off items
- Coupon: Order discount 5,000 (non-combinable)
Calculation:
  - Benefit skipped (non-combinable coupon applied)
  - After coupon: 30,000
  - Shipping: 0
Result:
  - Items 30,000; Shipping 0; Total 30,000

Scenario 8: Partial Refund Recomputes Shipping (No Points)
- Items: A 25,000; B 10,000 (Subtotal 35,000)
- Coupon: Order discount 5,000
- Refund: cancel B
Original:
  - After coupon: 30,000; Shipping 0; Total 30,000
Refund calculation:
  - Order discount allocated by item net amounts (before coupon)
    - A share: 25,000/35,000 = 5/7 -> discount 5,000 * 5/7 = 3,571 (floor)
    - B share: 10,000/35,000 = 2/7 -> discount 5,000 * 2/7 = 1,428 (floor)
    - Leftover 1 KRW assigned to refunded item B
    - Final discount: A 3,571; B 1,429
  - B net before refund: 10,000 - 1,429 = 8,571
  - Remaining subtotal (A): 25,000 - 3,571 = 21,429
  - Shipping becomes 5,000
Result:
  - Refund = 8,571 - 5,000 = 3,571

Scenario 9: Partial Refund with Item Coupon and Points
- Items: A 22,000; B 12,000 (Subtotal 34,000)
- Coupon: Item discount 2,000 off B
- Points: 4,000
- Refund: cancel B
Original:
  - After item coupon: A 22,000; B 10,000 (Subtotal 32,000)
  - Points allocation (by item net):
    - B share: 10,000 / 32,000 = 0.3125
    - Points on B: floor(4,000 * 0.3125) = 1,250
  - Shipping: 0 (subtotal before discount 34,000)
Refund calculation:
  - B refund base: 10,000 - 1,250 = 8,750
  - Remaining subtotal (A): 22,000
  - Shipping becomes 5,000
Result:
  - Refund = 8,750 - 5,000 = 3,750

Scenario 10: Refund Less Than New Shipping Fee (No Extra Charge)
- Items: A 26,000; B 4,000 (Subtotal 30,000)
- Coupons: none
- Refund: cancel B
Original:
  - Shipping: 0 (subtotal >= 30,000)
Refund calculation:
  - Remaining subtotal: 26,000 < 30,000
  - Shipping becomes 5,000
  - Item refund: 4,000
  - Calculated refund: 4,000 - 5,000 = -1,000
Result:
  - Refund floored at 0; no additional charge is collected

Scenario 11: Benefit Priority - Rate Over Fixed
- Items: A 25,000; B 15,000 (Subtotal 40,000)
- Benefits: 10% rate (4,000 discount) vs 5,000 fixed
- No coupons, no points
Calculation:
  - Priority: rate % > amount > start date
  - 10% rate benefit selected (even though 5,000 fixed gives more discount)
  - Discount: 40,000 * 10% = 4,000
  - Shipping: 0 (>= 30,000)
Result:
  - Items 36,000; Shipping 0; Total 36,000
