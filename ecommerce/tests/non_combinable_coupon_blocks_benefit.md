POST /user
{"id":"U1","tier":"BRONZE","point":{"balance":100000}}

POST /product
{"id":"P1","name":"Prod","benefits":[{"id":"B10","type":"RATE","rate":0.10,"startAt":"2025-01-01","endAt":"2025-12-31","combinableWithCoupons":true},{"id":"B4K","type":"FIXED","amount":4000,"startAt":"2025-01-01","endAt":"2025-12-31","combinableWithCoupons":true}],"variants":[{"id":"A","sku":"A","price":25000,"stock":10},{"id":"B","sku":"B","price":15000,"stock":10}]}

POST /coupon
{"id":"C_FREE","code":"FREE","couponType":"FREE_SHIPPING","discountType":"FIXED","amount":0,"combinable":false,"active":true,"startAt":"2025-01-01","endAt":"2025-12-31"}

POST /coupon
{"id":"C_ITEM","code":"ITEM","couponType":"ITEM_DISCOUNT","discountType":"FIXED","amount":2000,"combinable":true,"targetVariantId":"B","active":true,"startAt":"2025-01-01","endAt":"2025-12-31"}

POST /order
{"id":"O1","userId":"U1","items":[{"variantId":"A","quantity":1},{"variantId":"B","quantity":1}],"couponIds":["C_FREE","C_ITEM"],"pointAmount":3000}

GET /order/O1
>>> {"id":"O1","itemSubtotalBeforeDiscount":40000,"benefitDiscount":0,"couponDiscount":0,"pointsUsed":3000,"shippingFee":0,"totalAmount":37000,"benefitBlockedReason":"NON_COMBINABLE_COUPON_APPLIED","appliedCoupons":[{"couponType":"FREE_SHIPPING","discountAmount":0}]}
