POST /user
{"id":"U1","tier":"BRONZE","point":{"balance":0}}

POST /product
{"id":"P1","name":"Prod","benefits":[{"id":"B5","type":"RATE","rate":0.05,"startAt":"2025-01-01","endAt":"2025-12-31","combinableWithCoupons":true}],"variants":[{"id":"A","sku":"A","price":20000,"stock":10},{"id":"B","sku":"B","price":12000,"stock":10}]}

POST /order
{"id":"O1","userId":"U1","items":[{"variantId":"A","quantity":1},{"variantId":"B","quantity":1}]}

GET /order/O1
>>> {"id":"O1","itemSubtotalBeforeDiscount":32000,"benefitDiscount":1600,"couponDiscount":0,"pointsUsed":0,"shippingFee":0,"totalAmount":30400,"appliedBenefit":{"type":"RATE","discountAmount":1600}}
