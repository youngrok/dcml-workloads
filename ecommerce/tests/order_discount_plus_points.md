POST /user
{"id":"U1","tier":"BRONZE","point":{"balance":50000}}

POST /product
{"id":"P1","name":"Prod","benefits":[],"variants":[{"id":"A","sku":"A","price":18000,"stock":10},{"id":"B","sku":"B","price":9000,"stock":10}]}

POST /coupon
{"id":"C_ORDER","code":"ORDER","couponType":"ORDER_DISCOUNT","discountType":"FIXED","amount":3000,"combinable":true,"active":true,"startAt":"2025-01-01","endAt":"2025-12-31"}

POST /order
{"id":"O1","userId":"U1","items":[{"variantId":"A","quantity":1},{"variantId":"B","quantity":1}],"couponIds":["C_ORDER"],"pointAmount":2000}

GET /order/O1
>>> {"id":"O1","itemSubtotalBeforeDiscount":27000,"benefitDiscount":0,"couponDiscount":3000,"pointsUsed":2000,"shippingFee":5000,"totalAmount":27000,"appliedCoupons":[{"couponType":"ORDER_DISCOUNT","discountAmount":3000}]}
