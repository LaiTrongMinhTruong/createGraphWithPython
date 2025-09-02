from graphviz import Digraph
import os

# Tạo sơ đồ ERD
dot = Digraph(comment="Keansburg Park ERD", format="png")
dot.attr(rankdir="LR", size="8")

# Các thực thể (Entities)
entities = {
    "Users": ["user_id (PK)", "username", "password_hash", "full_name", "email", "phone", "role"],
    "Zones": ["zone_id (PK)", "zone_name", "description", "zone_type"],
    "Attractions": ["attraction_id (PK)", "zone_id (FK)", "name", "description", "image_url"],
    
    "Restaurants": ["restaurant_id (PK)", "zone_id (FK)", "name", "description", "image_url"],
    
    "Tickets": ["ticket_id (PK)", "ticket_name", "description"],
    "TicketPrices": ["price_id (PK)", "ticket_id (FK)", "day_type", "price", "valid_from", "valid_to"],
    "Bookings": ["booking_id (PK)", "user_id (FK)", "ticket_id (FK)", "quantity", "total_price", "status"],
    "Reviews": ["review_id (PK)", "user_id (FK)", "attraction_id (FK)", "rating", "comment"],
    "Gallery": ["image_id (PK)", "zone_id (FK)", "title", "description", "image_url"],
    "VisitorLogs": ["visit_id (PK)", "ip_address", "visit_time", "location"],
    "ContactQueries": ["query_id (PK)", "user_id (FK)", "message", "status"]
}

# Vẽ node cho từng entity
for entity, fields in entities.items():
    field_str = "\\l".join(fields) + "\\l"
    label = f"{{{entity}|{field_str}}}"
    dot.node(entity, shape="record", label=label)

# Quan hệ (Relationships)
relations = [
    ("Zones", "Attractions", "1", "N"),
    ("Zones", "Restaurants", "1", "N"),
    ("Attractions", "Reviews", "1", "N"),
    ("Restaurants", "Reviews", "1", "N"),
    ("Zones", "Gallery", "1", "N"),
    ("Users", "Bookings", "1", "N"),
    ("Tickets", "Bookings", "1", "N"),
    ("Tickets", "TicketPrices", "1", "N"),
    ("Users", "Reviews", "1", "N"),
    ("Users", "ContactQueries", "1", "N")
]

# Thêm quan hệ vào sơ đồ
for src, dst, card1, card2 in relations:
    dot.edge(src, dst, label=f"{card1}..{card2}")

# Xuất file ảnh (chỉnh lại path Windows)
output_path = r"D:\DOWNLOAD\Py with diagram\keansburg_park_erd"

# render trả về path file .png
rendered_path = dot.render(output_path, cleanup=True)

print("Ảnh ERD đã được lưu tại:", rendered_path)
print("Thư mục hiện tại khi chạy script là:", os.getcwd())
