pipeline {
    agent any

    environment {
        AWS_REGION = 'us-east-1'
        ROLE_ARN   = 'arn:aws:iam::084719916966:role/SageMakerExecutionRole'
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup AWS Credentials') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'aws_cred', usernameVariable: 'AWS_ACCESS_KEY_ID', passwordVariable: 'AWS_SECRET_ACCESS_KEY')]) {
                    bat '''
                    if not exist %USERPROFILE%\\.aws mkdir %USERPROFILE%\\.aws
                    echo [default] > %USERPROFILE%\\.aws\\credentials
                    echo aws_access_key_id=%AWS_ACCESS_KEY_ID% >> %USERPROFILE%\\.aws\\credentials
                    echo aws_secret_access_key=%AWS_SECRET_ACCESS_KEY% >> %USERPROFILE%\\.aws\\credentials
                    echo region=%AWS_REGION% >> %USERPROFILE%\\.aws\\credentials
                    '''
                }
            }
        }


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
