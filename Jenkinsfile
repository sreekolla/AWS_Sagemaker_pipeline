pipeline {
    agent any

    environment {
        AWS_REGION = 'us-east-1'
        ROLE_ARN   = 'arn:aws:iam::084719916966:role/SageMakerExecutionRole'
    }

    stages {
        stage('Install Dependencies') {
            steps {
                sh """
                python -m venv venv
                source venv/bin/activate
                pip install --upgrade pip
                pip install boto3 pandas scikit-learn joblib
                """
            }
        }

        stage('Run SageMaker Training') {
            steps {
                sh """
                source venv/bin/activate
                python sagemaker_pipeline.py
                """
            }
        }
    }
}
