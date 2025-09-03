from graphviz import Digraph

# Tạo sơ đồ ERD
dot = Digraph(comment="Keansburg Park ERD - Updated", format="png")
dot.attr(rankdir="LR", size="30,30")  # canvas rộng ngang
dot.attr("node", shape="record", fontsize="14", fontname="Arial")

entities = {
    "Users": [
        "PK: user_id", "username", "password_hash", "full_name", "date_of_birth",
        "email", "phone", "role", "created_at"
    ],
    "Zones": [
        "PK: zone_id", "zone_name", "description", "zone_type"
    ],
    "Attractions": [
        "PK: attraction_id", "FK: zone_id", "name", "description", "image_url"
    ],
    "Restaurants": [
        "PK: restaurant_id", "FK: zone_id", "name", "description", "image_url"
    ],
    "Gallery": [
        "PK: image_id", "title", "description", "image_url" #them bang gallery
    ],
    "Tickets": [
        "PK: ticket_id", "date", "price"
    ],
    "Bookings": [
        "PK: booking_id", "FK: user_id", "booking_code", "guest_name", "guest_email", "guest_phone", "total_price", "status", "created_at" #khong can guest info (vi co user_id)
    ],
    "BookingDetails": [
        "PK: booking_detail_id", "FK: booking_id", "FK: ticket_id", "using_date",
        "quantity", "unit_price", "total_price"
    ],
    "Payments": [ #them bang payment
        "PK: payment_id", "FK: booking_id", "payment_method",
        "payment_date", "amount", "status", "created_at"
    ],
    "Reviews": [
        "PK: review_id", "FK: user_id", "rating", "comment", "created_at" #phai dang nhap de review
    ],
}

# Vẽ node cho từng entity
for entity, fields in entities.items():
    field_str = "\\l".join(fields) + "\\l"
    label = f"{{{entity}|{field_str}}}"
    dot.node(entity, label=label)

# Quan hệ (Relationships)
relations = [
    ("Zones", "Attractions", "1", "N"),
    ("Zones", "Restaurants", "1", "N"),
    ("Users", "Bookings", "1", "N"),
    ("Bookings", "BookingDetails", "1", "N"),
    ("Tickets", "BookingDetails", "1", "N"),
    ("Bookings", "Payments", "1", "N"),
    ("Users", "Reviews", "1", "N"),
]

# Thêm quan hệ vào sơ đồ
for src, dst, card1, card2 in relations:
    dot.edge(src, dst, label=f"{card1}..{card2}")

# Xuất file ảnh
output_path = r"D:\DOWNLOAD\Py with diagram\keansburg_park_erd"
rendered_path = dot.render(output_path, cleanup=True)
rendered_path
