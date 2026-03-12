import os
import sys

import mlflow
from mlflow.sklearn import log_model

from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
from sklearn.pipeline import Pipeline

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from xgboost import XGBClassifier

from src.logger import logging
from src.exception import CustomException
from src.constants import MODEL_DIR, MODEL_FILE_NAME
from src.utils.utils import save_object


class ModelTrainer:

    def __init__(self, X, y, preprocessor):

        self.X = X
        self.y = y
        self.preprocessor = preprocessor



    def get_models(self):

        return {

            "logistic_regression": LogisticRegression(max_iter=1000),

            "decision_tree": DecisionTreeClassifier(),

            "random_forest": RandomForestClassifier(),

            "gradient_boosting": GradientBoostingClassifier(),

            "xgboost": XGBClassifier(eval_metric="logloss")
        }


    def train(self):

        try:

            logging.info("Starting model training")

            X_train, X_test, y_train, y_test = train_test_split(
                self.X,
                self.y,
                test_size=0.2,
                random_state=42
            )

            models = self.get_models()

            mlflow.set_experiment("churn_prediction")

            best_model = None
            best_score = 0
            best_model_name = None

            for name, model in models.items():

                with mlflow.start_run(run_name=name):

                    logging.info(f"Training {name}")

                    model.fit(X_train, y_train)

                    preds = model.predict(X_test)

                    score = roc_auc_score(y_test, preds)

                    mlflow.log_param("model_name", name)
                    mlflow.log_metric("roc_auc", float(score))

                    log_model(model, artifact_path=name)

                    logging.info(f"{name} ROC-AUC: {score}")

                    if score > best_score:

                        best_score = score
                        best_model = model
                        best_model_name = name

            final_pipeline = Pipeline(
                steps=[
                    ("preprocessor", self.preprocessor),
                    ("model", best_model)
                ]
            )

            logging.info(f"Best model: {best_model_name} with score {best_score}")

            os.makedirs(MODEL_DIR, exist_ok=True)

            model_path = os.path.join(MODEL_DIR, MODEL_FILE_NAME)

            save_object(model_path, best_model)

            logging.info("Best model saved")

            return best_model

        except Exception as e:

            raise CustomException(e, sys)