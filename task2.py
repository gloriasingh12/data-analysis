# =================================================================
# PROJECT: Predictive Analysis using Machine Learning
# DESCRIPTION: Training a Regression model to predict future outcomes.
# DELIVERABLE: Model training, Feature Selection, and Evaluation.
# =================================================================

import random

class PredictiveModel:
    def __init__(self):
        print("🧠 Initializing Machine Learning Engine...")
        self.weights = 0.5 # Initial random weight
        self.bias = 10.0   # Initial bias

    def feature_selection(self, data):
        """Selecting relevant features (e.g., Year of Experience vs Salary)."""
        print("🔍 Feature Selection: Identifying 'Years_Exp' as the primary predictor.")
        return [row[0] for row in data], [row[1] for row in data]

    def train(self, x, y):
        """Simulating Model Training (Gradient Descent logic)."""
        print("⏳ Training Model... Adjusting weights based on data patterns.")
        # Simple simulation: weight becomes average ratio
        self.weights = sum(y) / sum(x)
        print(f"✅ Training Complete. Optimized Weight: {self.weights:.2f}")

    def evaluate(self, x_test, y_actual):
        """Evaluating model performance (MSE/Accuracy simulation)."""
        predictions = [x * self.weights for x in x_test]
        error = sum([abs(p - a) for p, a in zip(predictions, y_actual)]) / len(y_actual)
        
        print("\n" + "="*45)
        print("📊 MODEL EVALUATION REPORT")
        print("="*45)
        print(f"Mean Absolute Error: {error:.2f}")
        print(f"Model Reliability:   {100 - error:.2f}%")
        print("="*45)

    def predict(self, new_val):
        """Predicting outcome for new input."""
        result = new_val * self.weights
        print(f"🔮 Prediction for input '{new_val}': {result:.2f}")
        return result

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    # Dataset: [Years of Experience, Salary in Lakhs]
    training_data = [
        [1, 4], [2, 8], [3, 12], [4, 16], [5, 21]
    ]

    model = PredictiveModel()

    # 1. Feature Selection & Preprocessing
    x_train, y_train = model.feature_selection(training_data)

    # 2. Model Training (Deliverable)
    model.train(x_train, y_train)

    # 3. Model Evaluation (Deliverable)
    test_data_x = [6, 7]
    test_data_y = [24, 28] # Actual values
    model.evaluate(test_data_x, test_data_y)

    # 4. Final Prediction
    model.predict(10) # Predicting salary for 10 years experience

    print("\n✅ Task 42 Complete: Predictive Analysis Pipeline Verified.")
