from models import Base, engine

# Initialize tables
Base.metadata.create_all(bind=engine)

print("Database initialized successfully.")
