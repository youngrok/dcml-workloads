POST /user
{"id":"U1","tier":"BRONZE","point":{"balance":10000}}

POST /product
{"id":"P1","name":"Prod","benefits":[],"variants":[{"id":"A","sku":"A","price":18000,"stock":10},{"id":"B","sku":"B","price":12000,"stock":10}]}

POST /coupon
{"id":"C_ORDER","code":"ORDER","couponType":"ORDER_DISCOUNT","discountType":"FIXED","amount":2000,"combinable":true,"active":true,"startAt":"2025-01-01","endAt":"2025-12-31"}

POST /order
{"id":"O1","userId":"U1","items":[{"variantId":"A","quantity":1},{"variantId":"B","quantity":1}],"couponIds":["C_ORDER"],"pointAmount":3000}

GET /order/O1
>>> {"id":"O1","itemSubtotalBeforeDiscount":30000,"benefitDiscount":0,"couponDiscount":2000,"pointsUsed":3000,"shippingFee":0,"totalAmount":25000,"appliedCoupons":[{"couponType":"ORDER_DISCOUNT","discountAmount":2000}]}
