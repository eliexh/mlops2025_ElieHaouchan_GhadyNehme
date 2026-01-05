from sagemaker.workflow.steps import TransformStep
from sagemaker.transformer import Transformer

# 1. Setup Transformer
transformer = Transformer(
    model_name="your-trained-model-name", # You get this from the training output
    instance_count=1,
    instance_type="ml.m5.large",
    strategy="MultiRecord",
    assemble_with="Line",
    output_path="s3://your-bucket/predictions/",
    base_transform_job_name="Batch-Inference"
)

# 2. Define Transform Step
step_inference = TransformStep(
    name="BatchInference",
    transformer=transformer,
    inputs=sagemaker.inputs.TransformInput(data="s3://your-bucket/input/raw_to_predict.csv")
)

# 3. Create Pipeline
pipeline_inf = Pipeline(name="MLOps-Inference-Pipeline", steps=[step_inference])
pipeline_inf.upsert(role_arn=role)
pipeline_inf.start()