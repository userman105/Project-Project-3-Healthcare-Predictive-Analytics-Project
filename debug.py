import joblib

# Load your trained model
model = joblib.load("ml_model/diabetes_model.pkl")

# Get feature names used during training
train_cols = model.booster_.feature_name()

print("Columns expected by the model (in order):")
for i, col in enumerate(train_cols, 1):
    print(f"{i}. {col}")

print(f"\nTotal columns: {len(train_cols)}")
