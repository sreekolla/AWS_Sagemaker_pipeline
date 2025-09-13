import boto3
import time

AWS_REGION = 'us-east-1'
ROLE_ARN = 'arn:aws:iam::084719916966:role/SageMakerExecutionRole'

sm = boto3.client('sagemaker', region_name=AWS_REGION)

training_job_name = 'jenkins-local-synthetic-' + str(int(time.time()))
training_image = '683313688378.dkr.ecr.us-east-1.amazonaws.com/sklearn-training:2.0-cpu-py39-ubuntu20.04'

# Note: InputDataConfig can be empty or use File mode with no S3
response = sm.create_training_job(
    TrainingJobName=training_job_name,
    AlgorithmSpecification={
        'TrainingImage': training_image,
        'TrainingInputMode': 'File'  # File mode reads data inside container
    },
    RoleArn=ROLE_ARN,
    InputDataConfig=[],  # No S3 input
    OutputDataConfig={
        'S3OutputPath': f's3://dummy-output-bucket/'  # Required by SageMaker, but can be ignored
    },
    ResourceConfig={
        'InstanceType': 'ml.m4.xlarge',
        'InstanceCount': 1,
        'VolumeSizeInGB': 5
    },
    StoppingCondition={
        'MaxRuntimeInSeconds': 3600
    },
    HyperParameters={
        'script': 'training.py'
    }
)

print(f"Training job {training_job_name} started successfully.")
