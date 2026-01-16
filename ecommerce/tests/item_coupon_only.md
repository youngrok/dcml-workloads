POST /user
{"id":"U1","tier":"BRONZE","point":{"balance":0}}

POST /product
{"id":"P1","name":"Prod","benefits":[],"variants":[{"id":"A","sku":"A","price":10000,"stock":10},{"id":"B","sku":"B","price":10000,"stock":10}]}

POST /coupon
{"id":"C_ITEM","code":"ITEM","couponType":"ITEM_DISCOUNT","discountType":"FIXED","amount":3000,"combinable":true,"targetVariantId":"B","active":true,"startAt":"2025-01-01","endAt":"2025-12-31"}

POST /order
{"id":"O1","userId":"U1","items":[{"variantId":"A","quantity":1},{"variantId":"B","quantity":1}],"couponIds":["C_ITEM"]}

GET /order/O1
>>> {"id":"O1","itemSubtotalBeforeDiscount":20000,"benefitDiscount":0,"couponDiscount":3000,"pointsUsed":0,"shippingFee":5000,"totalAmount":22000,"appliedCoupons":[{"couponType":"ITEM_DISCOUNT","discountAmount":3000}]}
