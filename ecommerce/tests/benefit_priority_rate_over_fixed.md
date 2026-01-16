POST /user
{"id":"U1","tier":"BRONZE","point":{"balance":0}}

POST /product
{"id":"P1","name":"Prod","benefits":[{"id":"B_RATE","type":"RATE","rate":0.10,"startAt":"2025-01-01","endAt":"2025-12-31","combinableWithCoupons":true},{"id":"B_FIXED","type":"FIXED","amount":5000,"startAt":"2025-01-01","endAt":"2025-12-31","combinableWithCoupons":true}],"variants":[{"id":"A","sku":"A","price":25000,"stock":10},{"id":"B","sku":"B","price":15000,"stock":10}]}

POST /order
{"id":"O1","userId":"U1","items":[{"variantId":"A","quantity":1},{"variantId":"B","quantity":1}]}

GET /order/O1
>>> {"id":"O1","itemSubtotalBeforeDiscount":40000,"benefitDiscount":4000,"couponDiscount":0,"pointsUsed":0,"shippingFee":0,"totalAmount":36000,"appliedBenefit":{"type":"RATE","discountAmount":4000}}
