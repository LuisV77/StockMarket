from database_manager import create_database, save_price

create_database()

save_price("AAPL", "2026-08-05 09:30:00", 210.50)
save_price("MSFT", "2026-08-05 09:30:00", 418.25)
save_price("GOOGL", "2026-08-05 09:30:00", 348.32)
save_price("AVGO", "2026-08-05 09:30:00", 178.67)



print("Practice prices saved.")
