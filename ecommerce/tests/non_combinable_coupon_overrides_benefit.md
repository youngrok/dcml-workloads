POST /user
{"id":"U1","tier":"BRONZE","point":{"balance":0}}

POST /product
{"id":"P1","name":"Prod","benefits":[{"id":"B3","type":"FIXED","amount":3000,"startAt":"2025-01-01","endAt":"2025-12-31","combinableWithCoupons":true}],"variants":[{"id":"A","sku":"A","price":15000,"stock":10},{"id":"B","sku":"B","price":20000,"stock":10}]}

POST /coupon
{"id":"C_ORDER","code":"ORDER","couponType":"ORDER_DISCOUNT","discountType":"FIXED","amount":5000,"combinable":false,"active":true,"startAt":"2025-01-01","endAt":"2025-12-31"}

POST /order
{"id":"O1","userId":"U1","items":[{"variantId":"A","quantity":1},{"variantId":"B","quantity":1}],"couponIds":["C_ORDER"]}

GET /order/O1
>>> {"id":"O1","itemSubtotalBeforeDiscount":35000,"benefitDiscount":0,"couponDiscount":5000,"pointsUsed":0,"shippingFee":0,"totalAmount":30000,"benefitBlockedReason":"NON_COMBINABLE_COUPON_APPLIED","appliedCoupons":[{"couponType":"ORDER_DISCOUNT","discountAmount":5000}]}
