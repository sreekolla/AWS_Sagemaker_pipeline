# sagemaker_pipeline.py
import sagemaker
from sagemaker.sklearn.estimator import SKLearn
import time
import os

AWS_REGION = 'us-east-1'
ROLE_ARN = 'arn:aws:iam::084719916966:role/SageMakerExecutionRole'

sess = sagemaker.Session()
timestamp = str(int(time.time()))

# Dummy S3 output (mandatory by SageMaker, input is synthetic so ignored)
S3_OUTPUT = f's3://dummy-bucket/output/'

sklearn_estimator = SKLearn(
    entry_point='training.py',       # <-- entry point script
    role=ROLE_ARN,
    instance_type='ml.m4.xlarge',
    instance_count=1,
    framework_version='2.0-1',
    py_version='py39',
    base_job_name=f'jenkins-synthetic-{timestamp}',
    output_path=S3_OUTPUT,
    sagemaker_session=sess
)

# Launch the training job
sklearn_estimator.fit()  # training.py runs automatically inside SageMaker
print("SageMaker training job started successfully!")
