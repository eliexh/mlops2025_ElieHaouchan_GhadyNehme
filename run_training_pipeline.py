import sagemaker
from sagemaker.workflow.pipeline import Pipeline
from sagemaker.workflow.steps import TrainingStep
from sagemaker.estimator import Estimator

# 1. Setup
session = sagemaker.Session()
role = "arn:aws:iam::123456789012:role/service-role/AmazonSageMaker-ExecutionRole-..." 
image_uri = "123456789012.dkr.ecr.us-east-1.amazonaws.com/mlops-project-repo:latest"

# 2. Define the Estimator (The "Container Runner")
estimator = Estimator(
    image_uri=image_uri,
    role=role,
    instance_count=1,
    instance_type="ml.m5.large", # Cheap instance for testing
    entry_point="scripts/train.py", # This is the script inside your Docker
    output_path="s3://your-bucket/models/"
)

# 3. Define the Training Step
step_train = TrainingStep(
    name="TrainModel",
    estimator=estimator,
    inputs={"training": "s3://your-bucket/data/raw.csv"}
)

# 4. Create and Start Pipeline
pipeline = Pipeline(name="MLOps-Training-Pipeline", steps=[step_train])
pipeline.upsert(role_arn=role)
pipeline.start()